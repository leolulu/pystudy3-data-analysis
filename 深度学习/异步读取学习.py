import tensorflow as tf

q = tf.FIFOQueue(1000, tf.float32)

var = tf.Variable(0.0)

data = tf.assign_add(var, 1.0)

enq = q.enqueue(data)
ouq = q.dequeue()

init = tf.global_variables_initializer()
qr = tf.train.QueueRunner(q, enqueue_ops=[enq] * 2)

with tf.Session() as sess:
    sess.run(init)

    coord = tf.train.Coordinator()
    thread1 = qr.create_threads(sess, start=True, coord=coord)

    for i in range(5):
        print(
            sess.run(ouq)
        )

    coord.request_stop()
    coord.join(thread1)
