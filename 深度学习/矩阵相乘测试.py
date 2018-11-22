import tensorflow as tf

a = tf.constant(1, shape=(10, 2))

c = tf.matmul(a, [[5], [2]])

with tf.Session() as sess:
    print(
        sess.run([a, c])
    )
