import tensorflow as tf
import numpy as np

a = tf.Variable(
    np.array([1, 2, 3]).reshape(1, 3),
    # np.array([1, 2, 3]).reshape(3, 1),
    name='a'
)

b = tf.Variable(
    np.array([2] * 3).reshape(3, 1),
    name='b'
)

c = tf.matmul(a, b)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(a))
    print(sess.run(b))
    print(
        sess.run(c)
    )
    tf.summary.FileWriter('./events', graph=sess.graph)
