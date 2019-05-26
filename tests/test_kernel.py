# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import numpy as np
import pytest
import tensorflow as tf
from lab.tensorflow import B

from stheno.input import Observed, Unique
from stheno.kernel import (
    EQ,
    RQ,
    Matern12,
    Matern32,
    Matern52,
    Delta,
    FixedDelta,
    Kernel,
    Linear,
    OneKernel,
    ZeroKernel,
    PosteriorKernel,
    ShiftedKernel,
    TensorProductKernel,
    CorrectiveKernel,
    DecayingKernel,
    LogKernel
)
from stheno.matrix import matrix, dense, Zero, One, UniformlyDiagonal
from .util import allclose


def standard_kernel_tests(k, shapes=None):
    if shapes is None:
        shapes = [((10, 2), (5, 2)),
                  ((10, 1), (5, 1)),
                  ((10,), (5,)),
                  ((10,), ()),
                  ((), (5,)),
                  ((), ())]

    # Check various shapes of arguments.
    for shape1, shape2 in shapes:
        x1 = B.randn(*shape1)
        x2 = B.randn(*shape2)

        # Check that the kernel computes.
        allclose(k(x1, x2), k(x2, x1).T)

        # Check `elwise`.
        x2 = B.randn(*shape1)

        allclose(k.elwise(x1, x2)[:, 0], B.diag(k(x1, x2)))
        allclose(k.elwise(x1, x2), Kernel.elwise(k, x1, x2))
        # The element-wise computation is more accurate, which is why we allow
        # a discrepancy a bit larger than the square root of the machine
        # epsilon.
        allclose(k.elwise(x1)[:, 0], B.diag(k(x1)),
                 desc='', atol=1e-6, rtol=1e-6)
        allclose(k.elwise(x1), Kernel.elwise(k, x1))


def test_corner_cases():
    with pytest.raises(RuntimeError):
        Kernel()(1.)


def test_construction():
    k = EQ()

    x = np.random.randn(10, 1)

    k(x)
    k(x, x)

    k(Observed(x))
    k(Observed(x), Observed(x))
    k(x, Observed(x))
    k(Observed(x), x)

    k.elwise(x)
    k.elwise(x, x)

    k.elwise(Observed(x))
    k.elwise(Observed(x), Observed(x))
    k.elwise(x, Observed(x))
    k.elwise(Observed(x), x)


def test_basic_arithmetic():
    k1 = EQ()
    k2 = RQ(1e-1)
    k3 = Matern12()
    k4 = Matern32()
    k5 = Matern52()
    k6 = Delta()
    k7 = Linear()
    xs1 = np.random.randn(10, 2), np.random.randn(20, 2)
    xs2 = np.random.randn(), np.random.randn()

    allclose(k6(xs1[0]), k6(xs1[0], xs1[0]))
    allclose((k1 * k2)(*xs1), k1(*xs1) * k2(*xs1))
    allclose((k1 * k2)(*xs2), k1(*xs2) * k2(*xs2))
    allclose((k3 + k4)(*xs1), k3(*xs1) + k4(*xs1))
    allclose((k3 + k4)(*xs2), k3(*xs2) + k4(*xs2))
    allclose((5. * k5)(*xs1), 5. * k5(*xs1))
    allclose((5. * k5)(*xs2), 5. * k5(*xs2))
    allclose((5. + k7)(*xs1), 5. + k7(*xs1))
    allclose((5. + k7)(*xs2), 5. + k7(*xs2))
    allclose(k1.stretch(2.)(*xs1), k1(xs1[0] / 2., xs1[1] / 2.))
    allclose(k1.stretch(2.)(*xs2), k1(xs2[0] / 2., xs2[1] / 2.))
    allclose(k1.periodic(1.)(*xs1), k1.periodic(1.)(xs1[0], xs1[1] + 5.))
    allclose(k1.periodic(1.)(*xs2), k1.periodic(1.)(xs2[0], xs2[1] + 5.))


def test_reversal():
    x1 = np.random.randn(10, 2)
    x2 = np.random.randn(5, 2)
    x3 = np.random.randn()

    # Test with a stationary and non-stationary kernel.
    for k in [EQ(), Linear()]:
        allclose(k(x1), reversed(k)(x1))
        allclose(k(x3), reversed(k)(x3))
        allclose(k(x1, x2), reversed(k)(x1, x2))
        allclose(k(x1, x2), reversed(k)(x2, x1).T)

        # Test double reversal does the right thing.
        allclose(k(x1), reversed(reversed(k))(x1))
        allclose(k(x3), reversed(reversed(k))(x3))
        allclose(k(x1, x2), reversed(reversed(k))(x1, x2))
        allclose(k(x1, x2), reversed(reversed(k))(x2, x1).T)

    # Verify that the kernel has the right properties.
    k = reversed(EQ())
    assert k.stationary
    assert k.var == 1
    assert k.length_scale == 1
    assert k.period == np.inf

    k = reversed(Linear())
    assert not k.stationary
    with pytest.raises(RuntimeError):
        k.var
    with pytest.raises(RuntimeError):
        k.length_scale
    assert k.period == np.inf
    assert str(k) == 'Reversed(Linear())'

    # Check equality.
    assert reversed(Linear()) == reversed(Linear())
    assert reversed(Linear()) != Linear()
    assert reversed(Linear()) != reversed(EQ())
    assert reversed(Linear()) != reversed(DecayingKernel(1, 1))

    # Standard tests:
    standard_kernel_tests(k)


def test_delta():
    k = Delta()

    # Verify that the kernel has the right properties.
    assert k.stationary
    assert k.var == 1
    assert k.length_scale == 0
    assert k.period == np.inf
    assert str(k) == 'Delta()'

    # Check equality.
    assert Delta() == Delta()
    assert Delta() != Delta(epsilon=k.epsilon * 10)
    assert Delta() != EQ()


@pytest.mark.parametrize('x1_x2', [(np.array(0), np.array(1)),
                                   (B.randn(10), B.randn(5)),
                                   (B.randn(10, 1), B.randn(5, 1)),
                                   (B.randn(10, 2), B.randn(5, 2))])
def test_delta_evaluations(x1_x2):
    k = Delta()
    x1, x2 = x1_x2
    n1 = B.shape(B.uprank(x1))[0]
    n2 = B.shape(B.uprank(x2))[0]

    # Check uniqueness checks.
    allclose(k(x1), B.eye(n1))
    allclose(k(x1, x2), B.zeros(n1, n2))

    # Standard tests:
    standard_kernel_tests(k)

    # Test `Unique` inputs.
    assert isinstance(k(Unique(x1), Unique(x1.copy())), Zero)
    assert isinstance(k(Unique(x1), Unique(x1)), UniformlyDiagonal)
    assert isinstance(k(Unique(x1), x1), Zero)
    assert isinstance(k(x1, Unique(x1)), Zero)

    assert isinstance(k.elwise(Unique(x1), Unique(x1.copy())), Zero)
    assert isinstance(k.elwise(Unique(x1), Unique(x1)), One)
    assert isinstance(k.elwise(Unique(x1), x1), Zero)
    assert isinstance(k.elwise(x1, Unique(x1)), Zero)


def test_fixed_delta():
    noises = B.rand(3)
    k = FixedDelta(noises)

    # Verify that the kernel has the right properties.
    assert k.stationary
    assert k.var == 1
    assert k.length_scale == 0
    assert k.period == np.inf
    assert str(k) == 'FixedDelta()'

    # Check equality.
    assert FixedDelta(noises) == FixedDelta(noises)
    assert FixedDelta(noises) != FixedDelta(2 * noises)
    assert FixedDelta(noises) != EQ()

    # Standard tests:
    standard_kernel_tests(k)

    # Check correctness.
    x1 = B.randn(5)
    x2 = B.randn(5)
    allclose(k(x1), B.zeros(5, 5))
    allclose(k.elwise(x1), B.zeros(5, 1))
    allclose(k(x1, x2), B.zeros(5, 5))
    allclose(k.elwise(x1, x2), B.zeros(5, 1))

    x1 = B.randn(3)
    x2 = B.randn(3)
    allclose(k(x1), B.diag(noises))
    allclose(k.elwise(x1), B.uprank(noises))
    allclose(k(x1, x2), B.zeros(3, 3))
    allclose(k.elwise(x1, x2), B.zeros(3, 1))


def test_eq():
    k = EQ()

    # Verify that the kernel has the right properties.
    assert k.stationary
    assert k.var == 1
    assert k.length_scale == 1
    assert k.period == np.inf
    assert str(k) == 'EQ()'

    # Test equality.
    assert EQ() == EQ()
    assert EQ() != Linear()

    # Standard tests:
    standard_kernel_tests(k)


def test_rq():
    k = RQ(1e-1)

    # Verify that the kernel has the right properties.
    assert k.alpha == 1e-1
    assert k.stationary
    assert k.var == 1
    assert k.length_scale == 1
    assert k.period == np.inf
    assert str(k) == 'RQ(0.1)'

    # Test equality.
    assert RQ(1e-1) == RQ(1e-1)
    assert RQ(1e-1) != RQ(2e-1)
    assert RQ(1e-1) != Linear()

    # Standard tests:
    standard_kernel_tests(k)


def test_exp():
    k = Matern12()

    # Verify that the kernel has the right properties.
    assert k.stationary
    assert k.var == 1
    assert k.length_scale == 1
    assert k.period == np.inf
    assert str(k) == 'Exp()'

    # Test equality.
    assert Matern12() == Matern12()
    assert Matern12() != Linear()

    # Standard tests:
    standard_kernel_tests(k)


def test_mat32():
    k = Matern32()

    # Verify that the kernel has the right properties.
    assert k.stationary
    assert k.var == 1
    assert k.length_scale == 1
    assert k.period == np.inf
    assert str(k) == 'Matern32()'

    # Test equality.
    assert Matern32() == Matern32()
    assert Matern32() != Linear()

    # Standard tests:
    standard_kernel_tests(k)


def test_mat52():
    k = Matern52()

    # Verify that the kernel has the right properties.
    assert k.stationary
    assert k.var == 1
    assert k.length_scale == 1
    assert k.period == np.inf
    assert str(k) == 'Matern52()'

    # Test equality.
    assert Matern52() == Matern52()
    assert Matern52() != Linear()

    # Standard tests:
    standard_kernel_tests(k)


def test_one():
    k = OneKernel()

    x1 = np.random.randn(10, 2)
    x2 = np.random.randn(5, 2)

    # Test that the kernel computes correctly.
    allclose(k(x1, x2), np.ones((10, 5)))

    # Verify that the kernel has the right properties.
    assert k.stationary
    assert k.var == 1
    assert k.length_scale == 0
    assert k.period == 0
    assert str(k) == '1'

    # Test equality.
    assert OneKernel() == OneKernel()
    assert OneKernel() != Linear()

    # Standard tests:
    standard_kernel_tests(k)


def test_zero():
    k = ZeroKernel()
    x1 = np.random.randn(10, 2)
    x2 = np.random.randn(5, 2)

    # Test that the kernel computes correctly.
    allclose(k(x1, x2), np.zeros((10, 5)))

    # Verify that the kernel has the right properties.
    assert k.stationary
    assert k.var == 0
    assert k.length_scale == 0
    assert k.period == 0
    assert str(k) == '0'

    # Test equality.
    assert ZeroKernel() == ZeroKernel()
    assert ZeroKernel() != Linear()

    # Standard tests:
    standard_kernel_tests(k)


def test_linear():
    k = Linear()

    # Verify that the kernel has the right properties.
    assert not k.stationary
    with pytest.raises(RuntimeError):
        k.var
    with pytest.raises(RuntimeError):
        k.length_scale
    assert k.period == np.inf
    assert str(k) == 'Linear()'

    # Test equality.
    assert Linear() == Linear()
    assert Linear() != EQ()

    # Standard tests:
    standard_kernel_tests(k)


def test_decaying_kernel():
    k = DecayingKernel(3.0, 4.0)

    assert not k.stationary
    with pytest.raises(RuntimeError):
        k.length_scale
    with pytest.raises(RuntimeError):
        k.var
    assert k.period == np.inf
    assert str(k) == 'DecayingKernel(3.0, 4.0)'

    # Standard tests:
    standard_kernel_tests(k)

    # Test equality.
    assert DecayingKernel(3.0, 4.0) == DecayingKernel(3.0, 4.0)
    assert DecayingKernel(3.0, 4.0) != DecayingKernel(3.0, 5.0)
    assert DecayingKernel(3.0, 4.0) != DecayingKernel(4.0, 4.0)
    assert DecayingKernel(3.0, 4.0) != EQ()


def test_log_kernel():
    k = LogKernel()

    # Verify that the kernel has the right properties.
    assert k.stationary
    assert k.var == 1
    assert k.length_scale == np.inf
    assert k.period == np.inf
    assert str(k) == 'LogKernel()'

    # Test equality.
    assert LogKernel() == LogKernel()
    assert LogKernel() != EQ()

    # Standard tests:
    standard_kernel_tests(k)


def test_posterior_kernel():
    k = PosteriorKernel(
        EQ(), EQ(), EQ(),
        np.random.randn(5, 2), matrix(EQ()(np.random.randn(5, 1)))
    )

    # Verify that the kernel has the right properties.
    assert not k.stationary
    with pytest.raises(RuntimeError):
        k.var
    with pytest.raises(RuntimeError):
        k.length_scale
    with pytest.raises(RuntimeError):
        k.period
    assert str(k) == 'PosteriorKernel()'

    # Standard tests:
    standard_kernel_tests(k, shapes=[((10, 2), (5, 2))])


def test_corrective_kernel():
    a, b = np.random.randn(3, 3), np.random.randn(3, 3)
    a, b = a.dot(a.T), b.dot(b.T)
    z = np.random.randn(3, 2)
    k = CorrectiveKernel(EQ(), EQ(), z, a, matrix(b))

    # Verify that the kernel has the right properties.
    assert not k.stationary
    with pytest.raises(RuntimeError):
        k.var
    with pytest.raises(RuntimeError):
        k.length_scale
    with pytest.raises(RuntimeError):
        k.period
    assert str(k) == 'CorrectiveKernel()'

    # Standard tests:
    standard_kernel_tests(k, shapes=[((10, 2), (5, 2))])


def test_sum():
    k1 = EQ().stretch(2)
    k2 = 3 * RQ(1e-2).stretch(5)
    k = k1 + k2

    assert k.stationary
    allclose(k.length_scale, (1 * 2 + 3 * 5) / 4)
    assert k.period == np.inf
    assert k.var == 4

    allclose((EQ() + EQ()).length_scale, 1)
    allclose((EQ().stretch(2) + EQ().stretch(2)).length_scale, 2)

    assert EQ() + Linear() == EQ() + Linear()
    assert EQ() + Linear() == Linear() + EQ()
    assert EQ() + Linear() != EQ() + RQ(1e-1)
    assert EQ() + Linear() != RQ(1e-1) + Linear()

    # Standard tests:
    standard_kernel_tests(k)


def test_stretched():
    k = EQ().stretch(2)

    assert k.stationary
    assert k.length_scale == 2
    assert k.period == np.inf
    assert k.var == 1

    # Test equality.
    assert EQ().stretch(2) == EQ().stretch(2)
    assert EQ().stretch(2) != EQ().stretch(3)
    assert EQ().stretch(2) != Matern12().stretch(2)

    # Standard tests:
    standard_kernel_tests(k)

    k = EQ().stretch(1, 2)

    assert not k.stationary
    with pytest.raises(RuntimeError):
        k.length_scale
    with pytest.raises(RuntimeError):
        k.period
    assert k.var == 1

    # Check passing in a list.
    k = EQ().stretch(np.array([1, 2]))
    k(np.random.randn(10, 2))


def test_periodic():
    k = EQ().stretch(2).periodic(3)

    assert k.stationary
    assert k.length_scale == 2
    assert k.period == 3
    assert k.var == 1

    # Test equality.
    assert EQ().periodic(2) == EQ().periodic(2)
    assert EQ().periodic(2) != EQ().periodic(3)
    assert Matern12().periodic(2) != EQ().periodic(2)

    # Standard tests:
    standard_kernel_tests(k)

    k = 5 * k.stretch(5)

    assert k.stationary
    assert k.length_scale == 10
    assert k.period == 15
    assert k.var == 5

    # Check passing in a list.
    k = EQ().periodic(np.array([1, 2]))
    k(np.random.randn(10, 2))


def test_scaled():
    k = 2 * EQ()

    assert k.stationary
    assert k.length_scale == 1
    assert k.period == np.inf
    assert k.var == 2

    # Test equality.
    assert 2 * EQ() == 2 * EQ()
    assert 2 * EQ() != 3 * EQ()
    assert 2 * EQ() != 2 * Matern12()

    # Standard tests:
    standard_kernel_tests(k)


def test_shifted():
    k = ShiftedKernel(2 * EQ(), 5)

    assert k.stationary
    assert k.length_scale == 1
    assert k.period == np.inf
    assert k.var == 2

    # Test equality.
    assert Linear().shift(2) == Linear().shift(2)
    assert Linear().shift(2) != Linear().shift(3)
    assert Linear().shift(2) != DecayingKernel(1, 1).shift(2)

    # Standard tests:
    standard_kernel_tests(k)

    k = (2 * EQ()).shift(5, 6)

    assert not k.stationary
    with pytest.raises(RuntimeError):
        k.length_scale
    assert k.period == np.inf
    assert k.var == 2

    # Check computation.
    x1 = np.random.randn(10, 2)
    x2 = np.random.randn(5, 2)
    k = Linear()
    allclose(k.shift(5)(x1, x2), k(x1 - 5, x2 - 5))

    # Check passing in a list.
    k = Linear().shift(np.array([1, 2]))
    k(np.random.randn(10, 2))


def test_product():
    k = (2 * EQ().stretch(10)) * (3 * RQ(1e-2).stretch(20))

    assert k.stationary
    assert k.length_scale == 10
    assert k.period == np.inf
    assert k.var == 6

    # Test equality.
    assert EQ() * Linear() == EQ() * Linear()
    assert EQ() * Linear() == Linear() * EQ()
    assert EQ() * Linear() != EQ() * RQ(1e-1)
    assert EQ() * Linear() != RQ(1e-1) * Linear()

    # Standard tests:
    standard_kernel_tests(k)


def test_selection():
    k = (2 * EQ().stretch(5)).select(0)

    assert k.stationary
    assert k.length_scale == 5
    assert k.period == np.inf
    assert k.var == 2

    # Test equality.
    assert EQ().select(0) == EQ().select(0)
    assert EQ().select(0) != EQ().select(1)
    assert EQ().select(0) != Matern12().select(0)

    # Standard tests:
    standard_kernel_tests(k)

    k = (2 * EQ().stretch(5)).select([2, 3])

    assert k.stationary
    assert k.length_scale == 5
    assert k.period == np.inf
    assert k.var == 2

    k = (2 * EQ().stretch(np.array([1, 2, 3]))).select([0, 2])

    assert k.stationary
    allclose(k.length_scale, [1, 3])
    allclose(k.period, [np.inf, np.inf])
    assert k.var == 2

    k = (2 * EQ().periodic(np.array([1, 2, 3]))).select([1, 2])

    assert k.stationary
    allclose(k.length_scale, [1, 1])
    allclose(k.period, [2, 3])
    assert k.var == 2

    k = (2 * EQ().stretch(np.array([1, 2, 3]))).select([0, 2], [1, 2])

    assert not k.stationary
    with pytest.raises(RuntimeError):
        k.length_scale
    with pytest.raises(RuntimeError):
        k.period
    assert k.var == 2

    k = (2 * EQ().periodic(np.array([1, 2, 3]))).select([0, 2], [1, 2])

    assert not k.stationary
    assert k.length_scale == 1
    with pytest.raises(RuntimeError):
        k.period
    assert k.var == 2

    # Test that computation is valid.
    k1 = EQ().select([1, 2])
    k2 = EQ()
    x = np.random.randn(10, 3)
    allclose(k1(x), k2(x[:, [1, 2]]))


def test_input_transform():
    k = Linear().transform(lambda x: x - 5)

    assert not k.stationary
    with pytest.raises(RuntimeError):
        k.length_scale
    with pytest.raises(RuntimeError):
        k.var
    with pytest.raises(RuntimeError):
        k.period

    def f1(x):
        return x

    def f2(x):
        return x ** 2

    # Test equality.
    assert EQ().transform(f1) == EQ().transform(f1)
    assert EQ().transform(f1) != EQ().transform(f2)
    assert EQ().transform(f1) != Matern12().transform(f1)

    # Standard tests:
    standard_kernel_tests(k)

    # Test computation of the kernel.
    k = Linear()
    x1, x2 = np.random.randn(10, 2), np.random.randn(10, 2)

    k2 = k.transform(lambda x: x ** 2)
    k3 = k.transform(lambda x: x ** 2, lambda x: x - 5)

    allclose(k(x1 ** 2, x2 ** 2), k2(x1, x2))
    allclose(k(x1 ** 2, x2 - 5), k3(x1, x2))


def test_tensor_product():
    k = TensorProductKernel(lambda x: B.sum(x ** 2, axis=1))

    assert not k.stationary
    with pytest.raises(RuntimeError):
        k.length_scale
    with pytest.raises(RuntimeError):
        k.var
    with pytest.raises(RuntimeError):
        k.period

    # Check equality.
    assert k == k
    assert k != TensorProductKernel(lambda x: x)
    assert k != EQ()

    # Standard tests:
    standard_kernel_tests(k)

    # Check computation of kernel.
    k = TensorProductKernel(lambda x: x)
    x1 = np.linspace(0, 1, 100)[:, None]
    x2 = np.linspace(0, 1, 50)[:, None]

    allclose(k(x1), x1 * x1.T)
    allclose(k(x1, x2), x1 * x2.T)

    k = TensorProductKernel(lambda x: x ** 2)

    allclose(k(x1), x1 ** 2 * (x1 ** 2).T)
    allclose(k(x1, x2), (x1 ** 2) * (x2 ** 2).T)


def test_derivative():
    # First, check properties.
    k = EQ().diff(0)

    assert not k.stationary
    with pytest.raises(RuntimeError):
        k.length_scale
    with pytest.raises(RuntimeError):
        k.var
    with pytest.raises(RuntimeError):
        k.period

    # Test equality.
    assert EQ().diff(0) == EQ().diff(0)
    assert EQ().diff(0) != EQ().diff(1)
    assert Matern12().diff(0) != EQ().diff(0)

    with pytest.raises(RuntimeError):
        EQ().diff(None, None)(1)

    # Third, check computation.
    s = tf.Session()

    # Test derivative of kernel EQ.
    k = EQ()
    x1 = tf.constant(np.random.randn(10, 1))
    x2 = tf.constant(np.random.randn(5, 1))

    # Test derivative with respect to first input.
    ref = s.run(-dense(k(x1, x2)) * (x1 - B.transpose(x2)))
    allclose(s.run(dense(k.diff(0, None)(x1, x2))), ref)
    ref = s.run(-dense(k(x1)) * (x1 - B.transpose(x1)))
    allclose(s.run(dense(k.diff(0, None)(x1))), ref)

    # Test derivative with respect to second input.
    ref = s.run(-dense(k(x1, x2)) * (B.transpose(x2) - x1))
    allclose(s.run(dense(k.diff(None, 0)(x1, x2))), ref)
    ref = s.run(-dense(k(x1)) * (B.transpose(x1) - x1))
    allclose(s.run(dense(k.diff(None, 0)(x1))), ref)

    # Test derivative with respect to both inputs.
    ref = s.run(dense(k(x1, x2)) * (1 - (x1 - B.transpose(x2)) ** 2))
    allclose(s.run(dense(k.diff(0, 0)(x1, x2))), ref)
    allclose(s.run(dense(k.diff(0)(x1, x2))), ref)
    ref = s.run(dense(k(x1)) * (1 - (x1 - B.transpose(x1)) ** 2))
    allclose(s.run(dense(k.diff(0, 0)(x1))), ref)
    allclose(s.run(dense(k.diff(0)(x1))), ref)

    # Test derivative of kernel Linear.
    k = Linear()
    x1 = tf.constant(np.random.randn(10, 1))
    x2 = tf.constant(np.random.randn(5, 1))

    # Test derivative with respect to first input.
    ref = s.run(B.ones(tf.float64, 10, 5) * B.transpose(x2))
    allclose(s.run(dense(k.diff(0, None)(x1, x2))), ref)
    ref = s.run(B.ones(tf.float64, 10, 10) * B.transpose(x1))
    allclose(s.run(dense(k.diff(0, None)(x1))), ref)

    # Test derivative with respect to second input.
    ref = s.run(B.ones(tf.float64, 10, 5) * x1)
    allclose(s.run(dense(k.diff(None, 0)(x1, x2))), ref)
    ref = s.run(B.ones(tf.float64, 10, 10) * x1)
    allclose(s.run(dense(k.diff(None, 0)(x1))), ref)

    # Test derivative with respect to both inputs.
    ref = s.run(B.ones(tf.float64, 10, 5))
    allclose(s.run(dense(k.diff(0, 0)(x1, x2))), ref)
    allclose(s.run(dense(k.diff(0)(x1, x2))), ref)
    ref = s.run(B.ones(tf.float64, 10, 10))
    allclose(s.run(dense(k.diff(0, 0)(x1))), ref)
    allclose(s.run(dense(k.diff(0)(x1))), ref)

    s.close()
