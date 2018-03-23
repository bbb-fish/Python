
#https://developers.google.com/machine-learning/crash-course/prereqs-and-prework#low-level-tensorflow-basics


##How to do some simple things, EXAMPLE COMMANDS

#x = tf.constant(5.2)

#y = tf.Variable([5])

#y = tf.Variable([0])
#y = y.assign([5])

#with tf.Session() as sess:
  #initialization = tf.global_variables_initializer()
  #print y.eval()

#####################################

import tensorflow as tf

import tensorflow as tf

# Create a graph.
g = tf.Graph()

# Establish the graph as the "default" graph.
with g.as_default():
  # Assemble a graph consisting of the following three operations:
  #   * Two tf.constant operations to create the operands.
  #   * One tf.add operation to add the two operands.
  x = tf.constant(8, name="x_const")
  y = tf.constant(5, name="y_const")
  my_sum = tf.add(x, y, name="x_y_sum")


  # Now create a session.
  # The session will run the default graph.
  with tf.Session() as sess:
    print my_sum.eval()

#######################################

#Exercise - add a z constant and add it 

import tensorflow as tf

# Create a graph.
g = tf.Graph()

# Establish the graph as the "default" graph.
with g.as_default():
  # Assemble a graph consisting of the following three operations:
  #   * Two tf.constant operations to create the operands.
  #   * One tf.add operation to add the two operands.
  x = tf.constant(8, name="x_const")
  y = tf.constant(5, name="y_const")
  z = tf.constant(69, name="z_const")
  my_sum = tf.add(x, y, name="x_y_sum")
  my_big_sum = tf.add(my_sum, z, name="big_sum")


  # Now create a session.
  # The session will run the default graph.
  with tf.Session() as sess:
    print my_sum.eval()
    print my_big_sum.eval()

##########################################

#CREATING AND MANIPULATING TENSORS

import tensorflow as tf

with tf.Graph().as_default():
  # Create a six-element vector (1-D tensor).
  primes = tf.constant([2, 3, 5, 7, 11, 13], dtype=tf.int32)

  # Create another six-element vector. Each element in the vector will be
  # initialized to 1. The first argument is the shape of the tensor (more
  # on shapes below).
  ones = tf.ones([6], dtype=tf.int32)

  # Add the two vectors. The resulting tensor is a six-element vector.
  just_beyond_primes = tf.add(primes, ones)

  # Create a session to run the default graph.
  with tf.Session() as sess:
    print just_beyond_primes.eval()

################################

#Shapes of the tensors

with tf.Graph().as_default():
  # A scalar (0-D tensor).
  scalar = tf.zeros([])

  # A vector with 3 elements.
  vector = tf.zeros([3])

  # A matrix with 2 rows and 3 columns.
  matrix = tf.zeros([2, 3])

  with tf.Session() as sess:
    print 'scalar has shape', scalar.get_shape(), 'and value:\n', scalar.eval()
    print 'vector has shape', vector.get_shape(), 'and value:\n', vector.eval()
    print 'matrix has shape', matrix.get_shape(), 'and value:\n', matrix.eval()