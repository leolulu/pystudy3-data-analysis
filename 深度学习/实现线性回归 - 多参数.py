import tensorflow as tf

with tf.variable_scope('prepare_data'):
    x = tf.random_normal((100, 3), mean=1.75, stddev=30, name='x')
    y = tf.matmul(x, [[10.0], [20.0], [30.0]]) + 20.0

with tf.variable_scope('modeling'):
    weight = tf.Variable(tf.random_normal((3, 1), mean=5.0, stddev=5.0), name='weight')
    bias = tf.Variable(0.0, name='bias')
    y_predict = tf.matmul(x, weight) + bias

with tf.variable_scope('loss_calc'):
    loss = tf.reduce_mean(tf.square(y - y_predict))

with tf.variable_scope('sgd'):
    train_op = tf.train.GradientDescentOptimizer(0.001).minimize(loss)

tf.summary.scalar('loss', loss)
tf.summary.histogram('weight', weight)
tf.summary.histogram('bias', bias)
merge = tf.summary.merge_all()

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print('初始的weight和bias为', sess.run(weight), sess.run(bias))

    filewriter = tf.summary.FileWriter('./events', graph=sess.graph)

    for i in range(1500):
        sess.run(train_op)
        summary = sess.run(merge)
        filewriter.add_summary(summary, i)

        print('第{}次优化后的weight和bias为'.format(i), weight.eval().flatten(), sess.run(bias))
        # tf.summary.FileWriter('./events', graph=sess.graph)
