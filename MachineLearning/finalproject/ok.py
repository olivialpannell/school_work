"""

"""
import re
import argparse
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix

def handle_args():
    parser = argparse.ArgumentParser(description=
                 'Fit perceptron model and make predictions on test data.')
    parser.add_argument('--rows', type=int,   default=6, help='Rows')
    parser.add_argument('--cols', type=int,   default=7, help='Columns')
    parser.add_argument('--team',  type=int, default=1, help='Team number')
    parser.add_argument('train',    help='Training data file')

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

def train_nn():
  # Read in data
  args = handle_args()
  ((x_train, y_train), varnames) = read_data(args.train)

  # Scale data
  scaler = StandardScaler()
  scaler.fit(x_train)
  StandardScaler(copy=True, with_mean=True, with_std=True)
  x_train = scaler.transform(x_train)

  # Train data
  np.seterr(divide='ignore', invalid='ignore')
  mlp = MLPClassifier(hidden_layer_sizes=(4,4), max_iter=500, activation='logistic')
  x_train[np.isnan(x_train)] = 0
  y_train[np.isnan(y_train)] = 0
  mlp = mlp.fit(x_train, y_train)
  print(mlp)
  return mlp

mlp = train_nn()

def test_agent_1(x_test, y_test):
  x_test2 = []
  x_test2.append(x_test)
  predictions = mlp.predict(x_test2)
  if predictions == 1.0:
    return 1
  return 0
  # print("ONEEEEEE:\t", confusion_matrix(y_test, predictions))
  # print("TWOOOOOOOO:\t", classification_report(y_test, predictions))
