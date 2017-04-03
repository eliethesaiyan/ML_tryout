import numpy as np


class NearestNeighbor:
      def __init__(self):
          pass

      def train(self,X,y):
          """ X is in NxD where each row is an example .y is 1-dimension of Size of size N"""
          self.Xtr=X
          self.ytr=y

      def predict(self,X):
          """ X is N x D where each row is an example we wish to predict the label for """
          num_test=X.shape[0]
          ypred=np.zeros(num_test,dtype=self.ytr.dtype)
          
          for i in xrange(num_test):
              distances=np.sum(np.abs(self.Xtr-X[i,:]),axis=1)
              min_index=np.argmin(distances)
              ypred[i]=self.ytr[min_index]
          return ypred


ngb=NearestNeighbor()
X=np.array([[2],[3],[4],[4]])
y=np.array([[1],[1],[-1],[-1]])
x_test=np.array([[4],[2],[3],[7]])
ngb.train(X,y)
print ngb.predict(x_test)

