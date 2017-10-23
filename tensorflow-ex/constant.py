import tensorflow as tf


# intialize constants 

#constant with names
x1 = tf.constant([1,2,3,4], name = "x1")

#constant without a name
x2 = tf.constant([5,6,7,8])

#operation with name
product = tf.multiply(x1, x2, name = "product")
#operation without a name
summation=tf.add(x1, x2, name = "Addition")


print("results outside of session")
print(product)
print(summation)

sess = tf.Session()

print("results within  session") 
print(sess.run(product))
print(sess.run(summation))
sess.close()

print(" restarting a new session in interactive way")

with tf.Session() as sess:
      print("Interactive session")
      print("Product")
      print(sess.run(product))
      print("Addition") 
      sess.run(summation)
    
