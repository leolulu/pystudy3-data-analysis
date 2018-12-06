import tensorflow as tf

# q = tf.FIFOQueue(1000, tf.float32)

var = tf.Variable(0.0)

add = tf.assign_add(var, 1)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(
        sess.run(add)
    )
    print(
        sess.run(add)
    )
    print(
        sess.run(var)
    )
