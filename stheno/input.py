from plum import parametric, kind

__all__ = ['Input',
           'Observed',
           'Latent',
           'Component',
           'At',
           'Unique',
           'WeightedUnique']


class Input:
    """Input type.

    Args:
        *xs (tensor): Inputs to type.
    """

    def __init__(self, *xs):
        self._xs = xs

    def get(self):
        """Get the wrapped input."""
        return self._xs[0] if len(self._xs) == 1 else self._xs


@parametric
class Component(Input):
    """A particular component.

    This is a parametric type.
    """


class MultiInput(Input):
    """Multiple inputs."""

    def get(self):
        return self._xs


class Unique(Input):
    """One cannot learn about noise at these inputs."""


class WeightedUnique(Unique):
    """One cannot learn about noise at these inputs.

    Args:
        x (tensor): Input.
        w (tensor): Weights.
    """

    def __init__(self, x, w):
        self.w = w
        Unique.__init__(self, x)


Observed = Component('observed')  #: Observed points
Latent = Component('latent')  #: Latent points

#: A generic parametric type used to specify locations at a particular process.
At = kind(Input)
