import tensorflow as tf
import os

file_list = [os.path.join(os.getcwd(), 'images', i) for i in os.listdir('./images')]

file_queue = tf.train.string_input_producer(file_list)

reader = tf.WholeFileReader()
key, value = reader.read(file_queue)

image = tf.image.decode_jpeg(value)

image = tf.image.resize_images(image, [500, 500])
image.set_shape((500, 500, 3))

image = tf.train.batch([image], batch_size=2, num_threads=1, capacity=2)


with tf.Session() as sess:

    coord = tf.train.Coordinator()
    thread = tf.train.start_queue_runners(sess, coord)

    print(
        sess.run([image])
    )

    coord.request_stop()
    coord.join(thread)

