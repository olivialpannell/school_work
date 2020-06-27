#!/usr/bin/python
# 
# CIS 472/572 -- Programming Homework #1
#
# Starter code provided by Daniel Lowd, 1/20/2020
# Please use this template as a starting point, 
# to support autograding with Gradescope.
import argparse
import numpy as np


# Process arguments for k-NN classification
def handle_args():
    parser = argparse.ArgumentParser(description=
                 'Make predictions using the k-NN algorithms.')

    parser.add_argument('-k', type=int, default=1, help='Number of nearest neighbors to consider')
    parser.add_argument('--varnorm', action='store_true', help='Normalize features to zero mean and unit variance')
    parser.add_argument('--rangenorm', action='store_true', help='Normalize features to the range [-1,+1]')
    parser.add_argument('--exnorm', action='store_true', help='Normalize examples to unit length')
    parser.add_argument('train',  help='Training data file')
    parser.add_argument('test',   help='Test data file')

    return parser.parse_args()


# Load data from a file
def read_data(filename):
  data = np.genfromtxt(filename, delimiter=',', skip_header=1)
  x = data[:, 0:-1]
  y = data[:, -1]
  return (x,y)


# Distance between instances x1 and x2
def dist(x1, x2):
  distance = np.sqrt(np.sum(np.power(x1-x2, 2)))
  return distance

  
# Predict label for instance x, using k nearest neighbors in training data
def classify(train_x, train_y, k, x):
  k = 15
  p = 0
  li = list()
  for i in range(len(train_x)):
    d = dist(train_x[i], x)
    li.append(d)

  neighbors = np.argpartition(li, k) [:k] #gives indexes of rows from train_x
  # print("Neighbors:")
  # print(neighbors)

  for i in range(1, k):
    p = p + train_y[neighbors[i]]

  # print("P:", p)

  if p >= 0:
    return 1

  if p < 0:
    return -1

  return 0


# Process the data to normalize features and/or examples.
# NOTE: You need to normalize both train and test data the same way.
def normalize_data(train_x, test_x, rangenorm, varnorm, exnorm):
  #y = (x - min) / (max - min)

  if rangenorm:
    #normalize training data [-1, 1]
    t = ((train_x - train_x.min(axis = 0)) *2)
    b = train_x.max(axis = 0) - train_x.min(axis = 0)
    b[b == 0] = 1
    newtrain_x = -1 + (t/b)

    #normalize test data [-1, 1]
    t2 = ((test_x - test_x.min(axis = 0)) *2)
    b2 = test_x.max(axis = 0) - test_x.min(axis = 0)
    b2[b2 == 0] = 1
    newtest_x = -1 + (t2/b2)
    return newtrain_x, newtest_x

  if varnorm:
    #pass
    mean1 = np.mean(train_x, axis = 0)
    dev = np.std(train_x, axis = 0)
    for i in train_x:
      for j in range(len(i)):
        if dev[j] == 0:
          i[j] = 0
        else:
          i[j] = (i[j] - mean1[j]) / dev[j]

    mean2 = np.mean(test_x, axis = 0 )
    dev2 = np.std(test_x, axis = 0)
    for i in test_x:
      for j in range(len(i)):
        if dev2[j] == 0:
          i[j] = 0
        else:
          i[j] = (i[j] - mean2[j]) / dev2[j]

  if exnorm:
    for i in range(len(train_x)):
      train_x[i] = train_x[i]/ (np.sqrt(np.sum(np.power(train_x[i], 2))))

    for i in range(len(test_x)):
      test_x[i] = test_x[i]/ (np.sqrt(np.sum(np.power(test_x[i], 2))))

  return train_x, test_x


# Run classifier and compute accuracy
def runTest(test_x, test_y, train_x, train_y, k):
  correct = 0
  for (x,y) in zip(test_x, test_y):
    if classify(train_x, train_y, k, x) == y:
      correct += 1
  acc = float(correct)/len(test_x)
  return acc


# Load train and test data.  Learn model.  Report accuracy.
# (NOTE: You shouldn't need to change this.)
def main():

  args = handle_args()

  # Read in lists of examples.  Each example is a list of attribute values,
  # where the last element in the list is the class value.
  (train_x, train_y) = read_data(args.train)
  (test_x, test_y)   = read_data(args.test)

  # Normalize the training data
  (train_x, test_x) = normalize_data(train_x, test_x, 
                          args.rangenorm, args.varnorm, args.exnorm)
    
  acc = runTest(test_x, test_y,train_x, train_y,args.k)
  print("Accuracy: ",acc)

if __name__ == "__main__":
  main()
