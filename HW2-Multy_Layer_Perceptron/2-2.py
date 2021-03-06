# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""A deep MNIST classifier using convolutional layers.

See extensive documentation at
https://www.tensorflow.org/get_started/mnist/pros
"""
# Disable linter warnings to maintain consistency with tutorial.
# pylint: disable=invalid-name
# pylint: disable=g-bad-import-order

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import tempfile

# Load data
## Import for read data
from tensorflow.examples.tutorials.mnist import input_data

# Initialize Parameter
## Import tensorflow
import tensorflow as tf

FLAGS = None


def deepnn(x):
  with tf.name_scope('reshape'):
    # Design 2 Layer CNN model
    x_image = tf.reshape(x, [-1, 28, 28, 1])

  with tf.name_scope('conv1'):
    # Initialize Parameter
    ## Initialize weight
    W_conv1 = weight_variable([5, 5, 1, 32])
    ## Initialize bias
    b_conv1 = bias_variable([32])
    # Design 2 Layer CNN model
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)

  with tf.name_scope('pool1'):
    # Design 2 Layer CNN model
    h_pool1 = max_pool_2x2(h_conv1)

  with tf.name_scope('conv2'):
    # Design 2 Layer CNN model
    W_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)

  with tf.name_scope('pool2'):
    # Design 2 Layer CNN model
    h_pool2 = max_pool_2x2(h_conv2)

  with tf.name_scope('fc1'):
    # Fully Connected Layer for Classification
    W_fc1 = weight_variable([7 * 7 * 64, 1024])
    b_fc1 = bias_variable([1024])

    h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

  with tf.name_scope('dropout'):
    keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

  with tf.name_scope('fc2'):
    W_fc2 = weight_variable([1024, 10])
    b_fc2 = bias_variable([10])
    ## y_conv = h_fc1_drop*W_fc2 + b_fc2
    y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2
  return y_conv, keep_prob

# 2D-Convolution
def conv2d(x, W):
  ## input: x / filter: W / move filter as (1, 1) /
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

# Pooling
def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# Initialize Parameter
## Initialize weight as random number which is following truncated normal distribution
def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)
## Initialize bias as 0.1
def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)


def main(_):
  # Load data
  ## Read data from data_dir, using input_data function from tensorflow.examples.tutorials.mnist
  mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

  # Initialize Parameter
  ## Declare new placeholder, which data-type is tf.float32, and size is [None, 784]
  x = tf.placeholder(tf.float32, [None, 784])
  ## Declare new placeholder, which data-type is tf.float32, and size is [None, 10]
  y_ = tf.placeholder(tf.float32, [None, 10])

  y_conv, keep_prob = deepnn(x)

  with tf.name_scope('loss'):
    # Cost Function
    ## Declare cross_entropy: create cross-entropy loss with logits
    cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv)
  ## Declare cross_entropy: and calculate it's mean
  cross_entropy = tf.reduce_mean(cross_entropy)

  with tf.name_scope('adam_optimizer'):
    # Cost Function
    ## Declare train_step: train to minimize cross_entropy, with AdamOptimizer as 1e-4
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

  with tf.name_scope('accuracy'):
    # Optimization
    ## Compare y and y_
    correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
    correct_prediction = tf.cast(correct_prediction, tf.float32)
  ## Calculate accuracy
  accuracy = tf.reduce_mean(correct_prediction)

  graph_location = tempfile.mkdtemp()
  print('Saving graph to: %s' % graph_location)
  train_writer = tf.summary.FileWriter(graph_location)
  train_writer.add_graph(tf.get_default_graph())

  with tf.Session() as sess:
    # Batch
    ## Initialize global variables to make environments to run
    sess.run(tf.global_variables_initializer())
    for i in range(20000): # change
      ## batch size = 50
      batch = mnist.train.next_batch(50)
      ## Measure accuracy every 100 datas
      if i % 100 == 0:
        train_accuracy = accuracy.eval(feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0})
        print('step %d, training accuracy %g' % (i, train_accuracy))
      train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

    print('test accuracy %g' % accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dir', type=str,
                      default='/tmp/tensorflow/mnist/input_data',
                      help='Directory for storing input data')
  FLAGS, unparsed = parser.parse_known_args()
  ## Run model
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)

