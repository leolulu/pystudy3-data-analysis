import tensorflow as tf

q = tf.FIFOQueue(1000, tf.float32)

var1 = tf.Variable(0.0, dtype=tf.float32)

add = tf.assign_add(var1, 1.0)

enq = q.enqueue(add)
deq = q.dequeue()

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for i in range(10):
        sess.run(enq)

    for i in range(q.size().eval()):
        print(
            sess.run(deq)
        )
