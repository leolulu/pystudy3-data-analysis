import tensorflow as tf

q = tf.FIFOQueue(capacity=5, dtypes=tf.float32)

enq_many = q.enqueue_many([[1.1, 2.2, 3.3], ])

de_q = q.dequeue()

en_q = q.enqueue(de_q + 1)

with tf.Session() as sess:
    sess.run(enq_many)

    for i in range(30):
        sess.run(en_q)

    for i in range(q.size().eval()):
        print(
            sess.run(de_q)
        )

    sess.run(de_q)
