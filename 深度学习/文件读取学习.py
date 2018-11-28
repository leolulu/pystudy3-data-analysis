import tensorflow as tf
import os

file_list = [os.path.join(os.getcwd(), i) for i in os.listdir('./csv_data')]

reader = tf.train.string_input_producer(file_list)

text_reader = tf.TextLineReader()

key, value = text_reader.read(reader)

l1, l2 = tf.decode_csv(value, record_defaults=[['None'], ['None']])

with tf.Session() as sess:

    coord = tf.train.Coordinator()

    thread = tf.train.start_queue_runners(sess, coord)

    print(
        sess.run([l1, l2])
    )

    coord.request_stop()
    coord.join(thread)
