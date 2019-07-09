Search.setIndex({docnames:["api","index","readme","source/stheno.autograd","source/stheno.eis","source/stheno.field","source/stheno.function_field","source/stheno.graph","source/stheno.input","source/stheno.kernel","source/stheno.lazy","source/stheno.matrix","source/stheno.mean","source/stheno.mokernel","source/stheno.momean","source/stheno.random","source/stheno.tensorflow","source/stheno.torch","source/stheno.util"],envversion:{"sphinx.domains.c":1,"sphinx.domains.changeset":1,"sphinx.domains.cpp":1,"sphinx.domains.javascript":1,"sphinx.domains.math":2,"sphinx.domains.python":1,"sphinx.domains.rst":1,"sphinx.domains.std":1,"sphinx.ext.todo":1,"sphinx.ext.viewcode":1,sphinx:56},filenames:["api.rst","index.rst","readme.rst","source/stheno.autograd.rst","source/stheno.eis.rst","source/stheno.field.rst","source/stheno.function_field.rst","source/stheno.graph.rst","source/stheno.input.rst","source/stheno.kernel.rst","source/stheno.lazy.rst","source/stheno.matrix.rst","source/stheno.mean.rst","source/stheno.mokernel.rst","source/stheno.momean.rst","source/stheno.random.rst","source/stheno.tensorflow.rst","source/stheno.torch.rst","source/stheno.util.rst"],objects:{"":{stheno:[0,0,0,"-"]},"stheno.eis":{AdditiveComponentKernel:[4,1,1,""],ComponentKernel:[4,1,1,""],NoisyKernel:[4,1,1,""]},"stheno.graph":{AbstractObservations:[7,1,1,""],GP:[7,1,1,""],Graph:[7,1,1,""],Obs:[7,3,1,""],Observations:[7,1,1,""],SparseObs:[7,3,1,""],SparseObservations:[7,1,1,""],model:[7,4,1,""]},"stheno.graph.AbstractObservations":{posterior_kernel:[7,2,1,""],posterior_mean:[7,2,1,""]},"stheno.graph.GP":{"var":[7,3,1,""],condition:[7,3,1,""],diff:[7,2,1,""],diff_approx:[7,2,1,""],display:[7,2,1,""],kernel:[7,3,1,""],length_scale:[7,3,1,""],mean:[7,3,1,""],name:[7,3,1,""],period:[7,3,1,""],select:[7,2,1,""],shift:[7,2,1,""],stationary:[7,3,1,""],stretch:[7,2,1,""],transform:[7,2,1,""]},"stheno.graph.Graph":{add_independent_gp:[7,2,1,""],condition:[7,3,1,""],cross:[7,2,1,""],diff:[7,2,1,""],logpdf:[7,3,1,""],mul:[7,3,1,""],name:[7,3,1,""],sample:[7,3,1,""],select:[7,2,1,""],shift:[7,2,1,""],stretch:[7,2,1,""],sum:[7,3,1,""],transform:[7,2,1,""]},"stheno.graph.Observations":{K_x:[7,3,1,""],posterior_kernel:[7,2,1,""],posterior_mean:[7,2,1,""]},"stheno.graph.SparseObservations":{A:[7,3,1,""],K_z:[7,3,1,""],elbo:[7,3,1,""],mu:[7,3,1,""],posterior_kernel:[7,2,1,""],posterior_mean:[7,2,1,""]},"stheno.input":{At:[8,3,1,""],Component:[8,1,1,""],Input:[8,1,1,""],Latent:[8,3,1,""],Observed:[8,3,1,""],Unique:[8,1,1,""]},"stheno.input.Input":{get:[8,2,1,""]},"stheno.kernel":{DecayingKernel:[9,1,1,""],Delta:[9,1,1,""],DerivativeKernel:[9,1,1,""],EQ:[9,1,1,""],Exp:[9,1,1,""],FixedDelta:[9,1,1,""],Kernel:[9,1,1,""],Linear:[9,1,1,""],LogKernel:[9,1,1,""],Matern12:[9,3,1,""],Matern32:[9,1,1,""],Matern52:[9,1,1,""],OneKernel:[9,1,1,""],RQ:[9,1,1,""],ScaledKernel:[9,1,1,""],ZeroKernel:[9,1,1,""]},"stheno.kernel.DecayingKernel":{display:[9,3,1,""],elwise:[9,3,1,""],period:[9,3,1,""]},"stheno.kernel.Delta":{"var":[9,3,1,""],elwise:[9,3,1,""],length_scale:[9,3,1,""],period:[9,3,1,""]},"stheno.kernel.DerivativeKernel":{elwise:[9,3,1,""]},"stheno.kernel.EQ":{"var":[9,3,1,""],elwise:[9,3,1,""],length_scale:[9,3,1,""],period:[9,3,1,""]},"stheno.kernel.Exp":{"var":[9,3,1,""],elwise:[9,3,1,""],length_scale:[9,3,1,""],period:[9,3,1,""]},"stheno.kernel.FixedDelta":{"var":[9,3,1,""],elwise:[9,3,1,""],length_scale:[9,3,1,""],period:[9,3,1,""]},"stheno.kernel.Kernel":{"var":[9,3,1,""],elwise:[9,3,1,""],length_scale:[9,3,1,""],period:[9,3,1,""],periodic:[9,2,1,""],stationary:[9,3,1,""]},"stheno.kernel.Linear":{elwise:[9,3,1,""],period:[9,3,1,""]},"stheno.kernel.LogKernel":{"var":[9,3,1,""],display:[9,3,1,""],elwise:[9,3,1,""],length_scale:[9,3,1,""],period:[9,3,1,""]},"stheno.kernel.Matern32":{"var":[9,3,1,""],elwise:[9,3,1,""],length_scale:[9,3,1,""],period:[9,3,1,""]},"stheno.kernel.Matern52":{"var":[9,3,1,""],elwise:[9,3,1,""],length_scale:[9,3,1,""],period:[9,3,1,""]},"stheno.kernel.OneKernel":{"var":[9,3,1,""],elwise:[9,3,1,""],length_scale:[9,3,1,""],period:[9,3,1,""]},"stheno.kernel.RQ":{"var":[9,3,1,""],display:[9,3,1,""],elwise:[9,3,1,""],length_scale:[9,3,1,""],period:[9,3,1,""]},"stheno.kernel.ScaledKernel":{"var":[9,3,1,""],elwise:[9,3,1,""],length_scale:[9,3,1,""],period:[9,3,1,""]},"stheno.kernel.ZeroKernel":{"var":[9,3,1,""],elwise:[9,3,1,""],length_scale:[9,3,1,""],period:[9,3,1,""]},"stheno.matrix":{Constant:[11,1,1,""],Dense:[11,1,1,""],Diagonal:[11,1,1,""],LowRank:[11,1,1,""],One:[11,1,1,""],UniformlyDiagonal:[11,1,1,""],Woodbury:[11,1,1,""],Zero:[11,1,1,""],dense:[11,3,1,""],matrix:[11,3,1,""]},"stheno.matrix.Constant":{from_:[11,5,1,""]},"stheno.matrix.Dense":{T:[11,3,1,""]},"stheno.matrix.One":{from_:[11,5,1,""]},"stheno.matrix.UniformlyDiagonal":{from_:[11,5,1,""]},"stheno.matrix.Zero":{from_:[11,5,1,""]},"stheno.mean":{DerivativeMean:[12,1,1,""],TensorProductMean:[12,1,1,""]},"stheno.mokernel":{MultiOutputKernel:[13,1,1,""]},"stheno.mokernel.MultiOutputKernel":{elwise:[13,3,1,""]},"stheno.momean":{MultiOutputMean:[14,1,1,""]},"stheno.random":{Normal1D:[15,1,1,""],Normal:[15,1,1,""]},"stheno.random.Normal":{"var":[15,3,1,""],dim:[15,3,1,""],dtype:[15,3,1,""],entropy:[15,2,1,""],get:[15,2,1,""],kl:[15,3,1,""],lmatmul:[15,2,1,""],logpdf:[15,2,1,""],m2:[15,3,1,""],marginals:[15,2,1,""],mean:[15,3,1,""],rmatmul:[15,2,1,""],sample:[15,2,1,""],w2:[15,3,1,""]},stheno:{autograd:[3,0,0,"-"],eis:[4,0,0,"-"],field:[5,0,0,"-"],function_field:[6,0,0,"-"],graph:[7,0,0,"-"],input:[8,0,0,"-"],kernel:[9,0,0,"-"],lazy:[10,0,0,"-"],matrix:[11,0,0,"-"],mean:[12,0,0,"-"],mokernel:[13,0,0,"-"],momean:[14,0,0,"-"],random:[15,0,0,"-"],tensorflow:[16,0,0,"-"],torch:[17,0,0,"-"],util:[18,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","attribute","Python attribute"],"4":["py","data","Python data"],"5":["py","classmethod","Python class method"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:attribute","4":"py:data","5":"py:classmethod"},terms:{"50_000":2,"abstract":7,"case":2,"class":[2,4,7,8,9,11,12,13,14,15],"default":[2,7,9,11,15],"export":2,"final":2,"float":9,"function":[1,7,9,13,15],"import":2,"int":[2,7,11,15],"new":2,"return":[2,7,9,11,15],"true":[2,11],"var":[2,7,9,15],Adding:2,And:2,For:2,GPs:1,Its:1,Obs:[2,7],One:[8,11],The:[2,7,11,15],Then:2,Uses:4,__add__:2,__init__:2,__or__:2,_without_:2,about:[1,8],abstractobserv:7,accept:2,accord:7,act:15,adamoptim:2,add:[2,7,15],add_independent_gp:7,added:[2,7,9],addit:[2,4,7],additivecomponentkernel:4,alia:[7,8,9],all:2,allow:2,alpha:[2,9],also:[2,15],altern:[2,7],alternative_prior:2,alwai:2,amount:7,anaconda:2,ani:2,append:2,appli:2,applic:1,approxim:[1,7,9],arang:2,arg:[2,7],argument:[2,7],arrai:2,attach:7,autograd:[0,1],automat:2,axi:2,base:[4,7,8,9,11,12,13,14,15],basi:1,basic:2,bayesian:1,befor:2,begin:2,behav:2,behaviour:15,besid:2,beta:[2,9],between:[1,4,7],bit:2,black:2,block:2,blue:2,bool:11,both:2,bound:[2,15],brew:2,broadcast:15,build:2,call:2,callabl:2,can:[2,7,9,15],cannot:8,carlo:2,cartesian:[2,7],cdot:2,central:[2,15],choic:2,classmethod:11,col:11,collect:[2,7],column:[2,11,15],combin:2,come:2,compar:2,compat:2,compon:[2,4,8],componentkernel:4,comput:[2,15],concat:2,conda:2,condit:[2,7],consid:2,consist:[2,4],const_1:2,constant:[2,9,11],construct:[2,7,11,15],constructor:[2,7],constuct:2,contain:[2,15],contrib:2,conveni:[2,7,15],correct:7,correspond:2,cos:2,credibl:[2,15],cross:[2,7],current:2,data:[7,11,15],dddf:2,ddf:2,decai:9,decayingkernel:[2,9],decomposit:1,def:2,defin:2,definit:[2,11],delta:[2,9],dens:[2,11,15],deriv:[2,7,9,12],derivativefunct:[9,12],derivativekernel:9,derivativemean:12,descript:2,design:1,determin:[2,9,15],diag:11,diag_scal:11,diagon:[9,11],dict:4,dictionari:2,diff:[2,7],diff_approx:[2,7],differ:[2,7],differenti:7,dim:[2,7,15],dimens:[2,7],dimension:[1,15],direct:2,directli:2,dispatch:2,displai:[7,9],distanc:9,distribut:[1,7,9,15],doc:2,draw:2,dtype:[2,11,15],e_exp:2,e_indep:2,each:2,effici:2,eis:[0,1,2],elbo:[2,7],element:[2,11],els:2,elwis:[2,9,13],end:2,ensur:2,ensure_at:7,entropi:15,enumer:2,epsilon:[2,9],equal:9,estim:[2,7],evalu:15,everi:[2,15],evid:2,exampl:1,exp:[2,9],experiment:2,exponenti:[2,9],extend:2,extent:7,extract:2,f1_posterior:2,f1_true:2,f2_posterior:2,f2_true:2,f_1:2,f_2:2,f_gp_rnn:2,f_linear:2,f_period:2,f_posterior:2,f_prod:2,f_rnn:2,f_smooth:2,f_sum:2,f_true:2,f_true_linear:2,f_true_period:2,f_true_smooth:2,f_true_wiggli:2,f_wiggli:2,factor:2,fals:2,featur:[1,7],field:[0,1,11],figsiz:2,figur:2,finit:[1,7],first:[2,7],fix:2,fixeddelta:9,flatten:15,flexibl:2,float32:2,float64:2,fluctuat:2,follow:2,form:1,format:[2,7],formatt:[2,7],four:2,frac:2,from:[2,7,15],from_:11,fs_true:2,full:11,function_field:[0,1,9,12],functiontyp:2,further:7,furthermor:2,gamma:9,gaussian:[2,7],gcc:2,gener:[2,13,14],get:[2,7,8,15],gfortran:2,give:2,given:9,global_variables_initi:2,govern:9,gpar:1,graph:[0,1,2,13,14],green:2,gru:2,handi:2,have:2,henceforth:2,here:2,hyperparamet:2,ident:9,implement:[2,15],in_class:2,incorpor:1,independ:[2,4,7],index:[1,2,4],inds2:2,inds_ob:2,induc:[1,7],infer:1,init:2,initialis:2,input:[0,1,2,4,7,9,15],instal:1,instanc:[2,7,13,14,15],instead:2,int32:2,integr:1,intercept:2,interfac:1,interpret:2,interv:15,its:2,jointli:2,k_f:4,k_n:4,k_u:2,k_x:7,k_z:7,keep:2,kernel:[0,1,4,7,13],kind:[8,15],knowledg:1,kroneck:[2,9],kw_arg:[2,7],label:2,lambda:[2,7],latent:[2,4,8],layer:2,lazi:[0,1],learn:[1,8],left:[2,11],legend:2,len:2,length:[2,7,9,11],length_scal:[2,7,9],let:2,like:2,linear:[1,9],linspac:2,list:[4,7,15],lmatmul:[2,15],lml1:2,lml2:2,lml:2,lml_gp_rnn:2,lml_rnn:2,locat:[2,7],log:15,logarithm:9,logkernel:9,logpdf:[2,7,15],low:11,lower1:2,lower2:2,lower:[2,15],lowrank:11,lr_pd:11,mai:2,make:[2,4,13,14],mani:2,manual:1,map:9,margin:[2,15],mat:11,matern12:[2,9],matern32:[2,9],matern52:[2,9],matern:[2,9],math:2,matplotlib:2,matric:2,matrix:[0,1,2,7,9,15],mean1:2,mean2:2,mean:[0,1,7,14,15],method:[2,7,9,13,15],middl:11,minim:2,moar:2,model:[1,7],modul:[0,1],mokernel:[0,1,2],momean:[0,1,2],moment:15,mont:2,more:2,much:2,mul:7,multi:[1,13,14],multioutputkernel:[2,13],multioutputmean:[2,14],multipl:[1,4],multipli:[2,9],must:[2,9,15],name:[1,7],ndarrai:2,necessarili:2,newli:7,nice:2,nois:[2,4,7,8,9,15],noisi:4,noisykernel:[2,4],none:[2,4,11,15],nonlinear:1,nonparametr:1,normal1d:[2,15],normal:[2,15],normalis:2,note:2,now:2,nudg:2,num:15,number:[11,15],numer:2,numpi:1,object:[2,7,8],obs:2,observ:[2,4,7,8],offer:2,one:[2,15],oneel:11,onefunct:9,onekernel:9,ones:11,onli:[2,9,15],oper:2,opt:2,opt_jointli:2,opt_rnn:2,optim:7,optimis:2,option:[2,4,7,9,11,15],orang:2,order:[2,7],other:[2,15],otherwis:2,ouput:1,outer:11,output:[2,13,14],over:9,p_i:7,p_j:7,packag:2,page:1,pair:2,paramet:[2,4,7,8,9,11,13,14,15],parametr:[8,15],part:11,particular:[2,8,15],pdf:15,per:2,percentil:2,period:[2,7,9],permut:2,pip:2,pleas:2,plot:2,plot_predict:2,plt:2,plum:[2,4,7,8,9,11,12,13,14,15],point:[1,7,8,15],pos:2,posit:[9,11,15],possibl:2,posterior:[2,7],posterior_kernel:7,posterior_mean:7,pred:2,pred_f:2,pred_if:2,pred_iif:2,pred_iiif:2,pred_linear:2,pred_period:2,pred_smooth:2,pred_wiggli:2,predict:[1,15],pretti:2,print:2,prior:[1,9],process:[2,4,7,13,14,15],produc:9,product:[2,7,11],program:1,provid:[2,7],pyplot:2,python:2,pytorch:1,quadrat:[2,9],queri:2,randn:2,random:[0,1,2,7],randomprocess:7,randomvector:15,rang:2,rank:[2,11,15],rate:9,ration:[2,9],read:2,readabl:2,red:2,ref:[7,11],refer:[2,7],referenti:[2,4,7,9,11,12,13,14,15],region:2,regress:1,render:2,represent:2,requir:2,resolv:[4,7,9,11,12,13,14,15],respect:[2,7],result:2,revers:2,right:[2,9,11],rmatmul:15,rnn:1,rnn_constructor:2,row:[2,11],run:2,sai:2,sampl:[1,7,15],scalar:[2,7,9,11,15],scale:[2,7,9,11],scaledfunct:9,scaledkernel:9,scatter:2,scipyoptimizerinterfac:2,search:1,second:[1,7,15],see:[2,7],select:[2,7],self:2,separ:2,session:2,shape:[2,9],shift:[2,7],shorthand:[2,7],show:2,sig1:2,sig2:2,simpl:1,simpli:2,sin:2,singl:[2,15],slope:2,smooth:1,soi:2,sole:2,sourc:[4,7,8,9,11,12,13,14,15],space:[2,9],spars:1,sparseob:[2,7],sparseobserv:7,specif:7,specifi:[2,11,15],split:2,sqrt:2,squar:9,squeez:2,stack:2,stationar:[2,7,9],stationari:[2,7,9],std:2,stheno:[0,1],storag:2,str:7,stretch:[2,7],string:[2,7],structur:2,subplot:2,subtract:2,sum:[2,7,11],support:2,symmetr:11,syntax:2,tab:2,tail:9,take:[2,7],tensor:[2,7,8,9,11,15],tensorflow:[0,1],tensorproductfunct:12,tensorproductkernel:2,tensorproductmean:[2,12],term:2,text:2,thereon:2,thi:[2,8,15],thing:2,third:2,three:2,through:7,titl:2,toler:9,torch:[0,1,2],track:2,train:2,transform:[2,7],translat:2,transpos:11,true_intercept:2,true_slop:2,tupl:[4,7,15],two:[2,7],type:[2,4,7,8,9,11,15],underli:2,undiscuss:1,uniformli:11,uniformlydiagon:11,uniqu:8,unspecifi:2,unwrap:[2,11],upper1:2,upper2:2,upper:[2,15],use:2,used:[2,15],user:2,util:[0,1],val:2,valid:7,valu:[2,7,13,14,15],var_list:2,variabl:[2,15],varianc:[2,7,9,15],variou:[2,4],vars64:2,vector:[2,9,11,15],version:[2,9,15],vgp:2,via:[2,11],vs1:2,vs2:2,vs_gp:2,vs_rnn:2,wai:2,want:2,wbml:2,weight:[2,9],when:2,where:2,which:[2,7,15],wiggli:2,window:2,wise:2,wish:2,woodburi:11,work:2,wrap:[2,8],x_ind:2,x_ob:2,x_obs1:2,x_obs2:2,y1_ob:2,y2_ob:2,y_gp_rnn:2,y_ob:2,y_rnn:2,y_true:2,you:2,your:2,ys_ob:2,zero:[7,11,15],zeroel:11,zerofunct:9,zerokernel:9,zip:2},titles:["Application Programming Interface","Welcome","Stheno","stheno.autograd module","stheno.eis module","stheno.field module","stheno.function_field module","stheno.graph module","stheno.input module","stheno.kernel module","stheno.lazy module","stheno.matrix module","stheno.mean module","stheno.mokernel module","stheno.momean module","stheno.random module","stheno.tensorflow module","stheno.torch module","stheno.util module"],titleterms:{"function":2,GPs:2,Its:2,about:2,applic:0,approxim:2,autograd:3,avail:2,basi:2,bayesian:2,between:2,composit:2,decomposit:2,design:2,dimension:2,displai:2,distribut:2,eis:4,exampl:2,featur:2,field:5,finit:2,form:2,function_field:6,gpar:2,graph:7,incorpor:2,indic:1,induc:2,infer:2,input:8,instal:2,integr:2,interfac:0,kernel:[2,9],knowledg:2,lazi:10,learn:2,linear:2,manual:2,matrix:11,mean:[2,12],model:2,modul:[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],mokernel:13,momean:14,multi:2,multipl:2,name:2,nonlinear:2,nonparametr:2,numpi:2,ouput:2,point:2,predict:2,prior:2,program:0,properti:2,pytorch:2,random:15,regress:2,rnn:2,sampl:2,second:2,simpl:2,smooth:2,spars:2,stheno:[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],tabl:1,tensorflow:[2,16],torch:17,undiscuss:2,util:18,welcom:1}})