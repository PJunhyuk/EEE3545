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

"""A very simple MNIST classifier.

See extensive documentation at
https://www.tensorflow.org/get_started/mnist/beginners
"""
from __future__ import absolute_import       # for compatibility with both python 2, 3
from __future__ import division              # for compatibility with both python 2, 3
from __future__ import print_function        # for compatibility with both python 2, 3

import argparse
import sys

# Load data
## Import for read data
from tensorflow.examples.tutorials.mnist import input_data

# Initialize Parameter
## Import tensorflow
import tensorflow as tf

FLAGS = None


def main(_):
  # Load data
  ## Read data from data_dir, using input_data function from tensorflow.examples.tutorials.mnist
  mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

  # Initialize Parameter
  ## Declare new placeholder, which data-type is tf.float32, and size is [None, 784]
  x = tf.placeholder(tf.float32, [None, 784])
  ## Initialize W(weight) as 0
  W = tf.Variable(tf.zeros([784, 10]))
  ## Initialize b(bias) as 0
  b = tf.Variable(tf.zeros([10]))
  ## y = x*W + b
  y = tf.matmul(x, W) + b

  # Training - cross entropy
  ## Declare new placeholder, which data-type is tf.float32, and size is [None, 10]
  y_ = tf.placeholder(tf.float32, [None, 10])
  ## Declare cross_entropy: create cross-entropy loss with logits and calculate it's mean
  cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
  ## Declare train_step: train to minimize cross_entropy, with GradientDescentOptimizer as 0.5
  train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

  # Training - Batch
  ## Declare Session
  sess = tf.InteractiveSession()
  ## Initialize global variables to make environments to run
  tf.global_variables_initializer().run()
  ## Get first 1000 datas
  for _ in range(1000):
    ## Group 100 datas as 1 mini-batch
    batch_xs, batch_ys = mnist.train.next_batch(100)
    ## Run as train_step
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

  # Evaluate Model
  ## Compare y and y_
  correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
  ## Calculate accuracy
  accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
  ## Print accuracy of model
  print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
                      help='Directory for storing input data')
  FLAGS, unparsed = parser.parse_known_args()
  ## Run model
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)

