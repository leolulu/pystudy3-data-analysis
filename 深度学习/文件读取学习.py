import tensorflow as tf
import os

file_list = [os.path.join(os.getcwd(), 'csv_data', i) for i in os.listdir('./csv_data')]

reader = tf.train.string_input_producer(file_list)

text_reader = tf.TextLineReader()

key, value = text_reader.read(reader)

l1, l2 = tf.decode_csv(value, record_defaults=[['None'], ['None']])

l1, l2 = tf.train.batch([l1, l2], batch_size=9, num_threads=1, capacity=10)

with tf.Session() as sess:
    coord = tf.train.Coordinator()

    thread = tf.train.start_queue_runners(sess, coord=coord)

    print(
        l1,
        sess.run([l1])
    )

    coord.request_stop()
    coord.join(thread)
