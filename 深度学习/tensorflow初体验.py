import tensorflow as tf

a = tf.constant([[1, 2], [3, 4]], name='a')

var1 = tf.Variable([1, 2, 3], name='var1')

var2 = tf.Variable(
    tf.random_normal((5, 5), mean=0, stddev=1),
    name='var2'
)

a = tf.constant(3)
b = tf.constant(4)

c = tf.add(a, b, name='myadd')

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    sess.run([c])
    tf.summary.FileWriter('./events/', graph=sess.graph)
