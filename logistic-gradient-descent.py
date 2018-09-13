import numpy as np
import math

height = np.random.uniform(low=150.0, high=205.0, size=(40,))
print("height", height)
weight = np.random.uniform(low=40.0, high=100.0, size=(40,))
print("Weight", weight)
y  = np.random.randint(2, size=(40,))
print("labels",y)
cost, dw1, dw2, db, lr, w1, w2, b = 0, 0, 0, 0, 0.01, 0, 0, 1


for i in range(0,len(height)):
     logits = w1 * height[i] + w2 * weight[i] + b
     act = 1/(1+ math.exp(-logits))
     cost  += -1*((y[i] * math.log(act)) + ((1 - y[i]) * math.log(1 - act)))
     dlogits = act - y[i]
     dw1 += height[i] * dlogits 
     dw2 += weight[i] * dlogits
     db += dlogits 
     print("cost is {} at {} iteration".format(cost,i+1))
     print("dw1 is {} at {} iteration".format(dw1,i+1))
     print("dw is {} at {} iteration".format(dw2,i+1))
     print("db is {} at {} iteration".format(db,i+1))

w1 = w1 - lr * (dw1/len(height))
w2 = w2 - lr * (dw2/len(weight))

print("final weight w1  :{}".format(w1))
print("final weight w2  :{}".format(w2))
print("final bias b  :{}".format(b))
print("cost function :{}".format(cost))




