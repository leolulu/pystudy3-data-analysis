import tensorflow as tf

Q = tf.FIFOQueue(1000, tf.float32)

var1 = tf.Variable(0.0)

add = tf.assign_add(var1, 1.0)

enq = Q.enqueue(add)
deq = Q.dequeue()

init = tf.global_variables_initializer()
qr = tf.train.QueueRunner(Q, enqueue_ops=[enq] * 2)

with tf.Session() as sess:
    sess.run(init)

    coord = tf.train.Coordinator()
    thread1 = qr.create_threads(sess, coord=coord, start=True)

    for i in range(5):
        print(
            sess.run(deq)
        )

    coord.request_stop()
    coord.join(thread1)
