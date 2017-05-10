import subprocess
import os
import caffe
import lmdb
import math
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.cross_validation import StratifiedShuffleSplit

""" This example is based Joyofdata Jupiter file """
caffe.set_mode_gpu()
df=pd.read_csv("train.csv",sep=",")
features=df.ix[:,1:-1].as_matrix()
labels=df.ix[:,-1].as_matrix()

vec_log=np.vectorize(lambda x: math.log(x+1))
vec_int=np.vectorize(lambda str: int(str[-1])-1)

features=vec_log(features)
labels=vec_int(labels)
sss=StratifiedShuffleSplit(labels,1,test_size=0.2,random_state=0)
sss=list(sss)[0]
features_training = features[sss[0],]
labels_training = labels[sss[0],]
features_testing = features[sss[1],]
labels_testing = labels[sss[1],]


def load_data_into_lmdb(lmdb_name,features,labels=None):
    env=lmdb.open(lmdb_name,map_size=features.nbytes*2)
    features=features[:,:,None,None]
    for i in range(features.shape[0]):
        datum=caffe.proto.caffe_pb2.Datum()
        datum.channels=features.shape[1]
        datum.height=1
        datum.width=1
        
        if features.dtype==np.int:
           datum.data=features[i].tostring()
        elif features.dtype==np.float:
           datum.float_data.extend(features[i].flat)
        else:
           raise Exception("Features.dtype unkown")

        if labels is not None:
           datum.label=int(labels[i])
           
        str_id='{:08}'.format(i)
        with env.begin(write=True) as txn:
		txn.put(str_id,datum.SerializeToString())


#load_data_into_lmdb("/home/elie/data/train_data_lmdb",features_training,labels_training)
#load_data_into_lmdb("/home/elie/data/test_data_lmdb",features_training,labels_training)


def get_data_for_case_from_lmdb(lmdb_name,id):
    lmdb_env=lmdb.open(lmdb_name,readonly=True)
    lmdb_txn=lmdb_env.begin()


    raw_datum=lmdb_txn.get(id)
    datum=caffe.proto.caffe_pb2.Datum()
    datum.ParseFromString(raw_datum)
    feature=caffe.io.datum_to_array(datum)
    label=datum.label
    return (label,feature)

#get_data_for_case_from_lmdb("/home/elie/data/train_data_lmdb","00012345")
#proc=subprocess.Popen(["/home/elie/test/caffe-segnet-cudnn5/build/tools/caffe","train","--solver=config.prototxt"],stderr=subprocess.PIPE)
#res=proc.communicate()[1]

#print res

net=caffe.Net("model_prod.prototxt","./_iter_100000.caffemodel",caffe.TEST)
l,f=get_data_for_case_from_lmdb("/home/elie/data/test_data_lmdb","00001230")
out=net.forward(**{net.inputs[0]:np.asarray([f])})
print np.argmax(out["prob"][0])==l,"\n",out
plt.bar(range(9),out["prob"][0])



