import tensorflow as tf

#source ops

a = tf.constant([5])
b = tf.constant([4])

c=tf.add(a,b)

with tf.Session() as sess:
    print(sess.run(c))

#Data Structure
Scalar = tf.constant([2])
Vector = tf.constant([5,2,3])
Matrix = tf.constant([[1,2,3],[2,3,4],[5,6,7]])
Tensor = tf.constant([ [[1,2,3],[2,3,4],[3,4,5]], [[4,5,6],[5,6,7],[6,7,8]], [[7,8,9],[8,9,10],[9,10,11]] ])
with tf.Session() as sess:
    result = sess.run(Scalar)
    print("Scalar (1 Entry):\n %s \n"% result)
    result = sess.run(Vector)
    print("Vector (3 Entry):\n %s \n"% result)
    result = sess.run(Matrix)
    print("Matrix  (3x3 Entry):\n %s \n"% result)
    result = sess.run(Tensor)
    print("Tensor (3x3x3 Entry):\n %s \n"% result)

#Operations vs Ops
Matrix_one = tf.constant([ [1,2,3], [2,3,4], [3,4,5] ])
Matrix_two = tf.constant([ [2,2,2], [2,2,2], [2,2,2] ])
first_operation = tf.add(Matrix_one, Matrix_two)
second_operation = Matrix_one + Matrix_two
third_operation = 

with tf.Session() as sess:
    result = sess.run(first_operation)
    print("Defined using TensorFlow function:")
    print(result) 
    result = sess.run(second_operation)
    print("Defined using normal Expression :")
    print(result)


# Variables 
state = tf.Variable(0)
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state,  new_value)
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run(state))
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))


# PlaceHolders

a = tf.placeholder(tf.float32)
b = a * 2

with tf.Session() as sess:
    result = sess.run(b,feed_dict={a:3.5})
    print("Using Place Holder")
    print(result)
    print("Passing a Matrix in feed_dict") result = sess.run(b,feed_dict={a:[[1,2,3],[2,3,4],[3,4,5]]}) print(result) 


   
