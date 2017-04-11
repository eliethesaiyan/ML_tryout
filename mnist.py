
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

def main():
    print "hello"
    mnist=input_data.read_data_sets('MNIST_data',one_hot=True)
    print(mnist.train.num_examples)
    print(mnist.test.num_examples)
    sess=tf.InteractiveSession()
    X=tf.placeholder(tf.float32,shape=[None,784])
    y_=tf.placeholder(tf.float32,shape=[None,10])
    weights=tf.Variable(tf.zeros([784,10]))
    biases=tf.Variable(tf.zeros([10]))
    sess.run(tf.global_variables_initializer())
    
    raw_output=tf.matmul(X,weights)+biases
    cross_entropy=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_ ,logits=raw_output))
    learning_rate=0.5
    train_step=tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)
    batch_size=100
    step_count=1000
    for _ in range(step_count):
        batch=mnist.train.next_batch(batch_size)
        train_step.run(feed_dict={X:batch[0],y_:batch[1]})

    correct_prediction=tf.equal(tf.argmax(raw_output,1),tf.argmax(y_,1))
    accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    print accuracy.eval(feed_dict={X:mnist.test.images,y_:mnist.test.labels})
    


if __name__=="__main__":
   main()
