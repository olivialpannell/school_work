#!/usr/bin/python
#
# CIS 472/572 - Perceptron Template Code
#
# Author: Daniel Lowd <lowd@cs.uoregon.edu>
# Date:   2/9/2020
#
# Please use this code as the template for your solution.
#

import argparse
import numpy as np

import re
from math import log
from math import exp


# Process arguments for perceptron
def handle_args():
    parser = argparse.ArgumentParser(description=
                 'Fit perceptron model and make predictions on test data.')
    parser.add_argument('--maxiter', type=int,   default=100, help='Maximum number of iterations')
    parser.add_argument('--model',  help='File for saving model parameters')
    parser.add_argument('train',    help='Training data file')
    parser.add_argument('test',     help='Test data file')

    return parser.parse_args()

# Load data from a file
def read_data(filename):
  f = open(filename, 'r')
  p = re.compile(',')
  header = f.readline().strip()
  varnames = p.split(header)
  f.close()

  # Read data
  data = np.genfromtxt(filename, delimiter=',', skip_header=1)
  x = data[:, 0:-1]
  y = data[:, -1]
  return ((x, y), varnames)


# Learn weights using the perceptron algorithm
def train_perceptron(train_x, train_y, maxiter=100):
  # Initialize weight vector and bias
  '''
  Check whether or not a point is correctly classified
  If it is: 
    Do nothing
  If it is not: 
    Figure out which weight (wi) is affected it most and adjust by accordingly.


  '''
  numvars = len(train_x[0])
  numex = len(train_x)
  w = np.array([0.0] * numvars)
  b = 0.0

  # YOUR CODE HERE!
  for m in range(maxiter):
    for i in range(numex):
      a = np.dot(w, train_x[i]) + b #Compute activation

      a = a * train_y[i]
      # print(a)
      if a <= 0: # There is something wrong, we need to update. 

        # Iterate through w, add the product of xj and yj
        for j in range(numvars):
          update = np.dot(train_y[i], train_x[i][j])
          w[j] = w[j] + update

        b = b + train_y[i] # Update the bias
        
      # Else: No update needed (correct prediction)

  # print((w,b))
  return (w,b)


# Compute the activation for input x.
# (NOTE: This should be a real-valued number, not simply +1/-1.)
def predict_perceptron(model, x):
  (w,b) = model

  # YOUR CODE HERE!
  a = 0
  for i in range(len(x)):
    a += w[i]*x[i]

  a += b
  return a


# Load train and test data.  Learn model.  Report accuracy.
def main():
  # Process command line arguments.
  # (You shouldn't need to change this.)
  args = handle_args()

  ((train_x, train_y), varnames) = read_data(args.train)
  ((test_x,  test_y), testvarnames) = read_data(args.test)

  # Train model
  (w,b) = train_perceptron(train_x, train_y, maxiter=args.maxiter)

  # Write model file
  # (You shouldn't need to change this.)
  if args.model:
    f = open(args.model, "w+")
    f.write('%f\n' % b)
    for i in range(len(w)):
      f.write('%s %f\n' % (varnames[i], w[i]))

  # Make predictions, compute accuracy
  correct = 0
  for (x,y) in zip(test_x, test_y):
    activation = predict_perceptron( (w,b), x )
    if activation * y > 0:
      correct += 1
  acc = float(correct)/len(test_y)
  print("Accuracy: ",acc)

if __name__ == "__main__":
  main()
