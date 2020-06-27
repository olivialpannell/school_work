import numpy as np

#(0.23, 8.7), (1.24, 1.25), (1.45, 4.3), (2.1, 9.8), (2.975, 2.6),
#	(3.543, 5.1), (4.134, 6.2), (5.742, 7.0), (6.37, 3.2), (7.123, 0.0)

# 1, 8, 5, 0, 7, 4, 3, 2, 6, 9
# in_arr = np.array([2.1, 0.23, 5.742, 7.60, 4.134, 6.2,
# 					 3.543, 5.1, 1.45, 4.3, 6.37, 3.2, 
# 					2.975, 2.6, 1.24, 1.25, 7.123, 0.01]) 

# print ("Input array: \n", in_arr)  
  
# print("something")
# a = in_arr[np.argpartition(in_arr, 6)[:6]]
# print(a)
# print(np.sort(in_arr, axis = 0))
# print("another something")
# print ("Output partitioned array indices :\n ", in_arr) 

# a = ([ 0.85017222,  0.19406266,  0.7879974 ,  0.40444978,  0.46057793,
#         0.51428578,  0.03419694,  0.47708   ,  0.73924536,  0.14437159])
# arr = a[np.argpartition(a,range())[:5]]
# print(arr)

arr = [[0.359019, 0.24821323, 0.07201894, 0.97489665, 0.24929536, 0.01746314,
  0.45757585, 0.18840514 ,0.74268375, 0.84679852, 0.27346101, 0.48473332,  0.93704202 ,0.18333306 ,0.44603605, 0.88593153, 0.22642658, 0.67146362,
  0.60526564, 0.83761349],
 [0.73720559, 0.47960462 ,0.26129573 ,0.70969554 ,0.01907278 ,0.25088898,
  0.32773477, 0.36459239, 0.390944,   0.50883866 ,0.55036588 ,0.83909274,
  0.21088708 ,0.61948276 ,0.67354312, 0.03917674, 0.15776862, 0.00319532, 0.44035091 ,0.54480457],
 [0.22099573 ,0.0408939,  0.07337047 ,0.86512951, 0.76438503, 0.33513425,
  0.00733385 ,0.52778009 ,0.95745485, 0.83990248, 0.10517529, 0.52089514,
  0.84497991, 0.81485779, 0.12539023 ,0.32027089, 0.17238572, 0.86533436,
  0.44269667 ,0.28191198]]
arr = np.array(arr)


mean = np.mean(arr, axis = 0)
dev = np.std(arr, axis = 0)
print("Arr length: ",len(arr))
print("Mean length: ", len(mean))
print("Dev Lenght: ", len(dev))
for i in range(len(arr)):
	arr[i] = (arr[i] - mean[i]) /dev[i]



print("---------Final:---------")
print(arr)

















# # Convert string column to float
# def str_column_to_float(dataset, column):
# 	for row in dataset:
# 		row[column] = float(row[column].strip())
 
# # Convert string column to integer
# def str_column_to_int(dataset, column):
# 	class_values = [row[column] for row in dataset]
# 	unique = set(class_values)
# 	lookup = dict()
# 	for i, value in enumerate(unique):
# 		lookup[value] = i
# 	for row in dataset:
# 		row[column] = lookup[row[column]]
# 	return lookup
 
# # Find the min and max values for each column
# def dataset_minmax(dataset):
# 	minmax = list()
# 	for i in range(len(dataset[0])):
# 		col_values = [row[i] for row in dataset]
# 		value_min = min(col_values)
# 		value_max = max(col_values)
# 		minmax.append([value_min, value_max])
# 	return minmax
 
# # Rescale dataset columns to the range 0-1
# def normalize_dataset(dataset, minmax):
# 	for row in dataset:
# 		for i in range(len(row)):
# 			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])
 
# # Split a dataset into k folds
# def cross_validation_split(dataset, n_folds):
# 	dataset_split = list()
# 	dataset_copy = list(dataset)
# 	fold_size = int(len(dataset) / n_folds)
# 	for _ in range(n_folds):
# 		fold = list()
# 		while len(fold) < fold_size:
# 			index = randrange(len(dataset_copy))
# 			fold.append(dataset_copy.pop(index))
# 		dataset_split.append(fold)
# 	return dataset_split
 
# # Calculate accuracy percentage
# def accuracy_metric(actual, predicted):
# 	correct = 0
# 	for i in range(len(actual)):
# 		if actual[i] == predicted[i]:
# 			correct += 1
# 	return correct / float(len(actual)) * 100.0
 
# # Evaluate an algorithm using a cross validation split
# def evaluate_algorithm(dataset, algorithm, n_folds, *args):
# 	folds = cross_validation_split(dataset, n_folds)
# 	scores = list()
# 	for fold in folds:
# 		train_set = list(folds)
# 		train_set.remove(fold)
# 		train_set = sum(train_set, [])
# 		test_set = list()
# 		for row in fold:
# 			row_copy = list(row)
# 			test_set.append(row_copy)
# 			row_copy[-1] = None
# 		predicted = algorithm(train_set, test_set, *args)
# 		actual = [row[-1] for row in fold]
# 		accuracy = accuracy_metric(actual, predicted)
# 		scores.append(accuracy)
# 	return scores
 
# # Calculate the Euclidean distance between two vectors
# def euclidean_distance(row1, row2):
# 	distance = 0.0
# 	for i in range(len(row1)-1):
# 		distance += (row1[i] - row2[i])**2
# 	return sqrt(distance)
 
# # Locate the most similar neighbors
# def get_neighbors(train, test_row, num_neighbors):
# 	distances = list()
# 	for train_row in train:
# 		dist = euclidean_distance(test_row, train_row)
# 		distances.append((train_row, dist))
# 	distances.sort(key=lambda tup: tup[1])
# 	neighbors = list()
# 	for i in range(num_neighbors):
# 		neighbors.append(distances[i][0])
# 	return neighbors
 
# # Make a prediction with neighbors
# def predict_classification(train, test_row, num_neighbors):
# 	neighbors = get_neighbors(train, test_row, num_neighbors)
# 	output_values = [row[-1] for row in neighbors]
# 	prediction = max(set(output_values), key=output_values.count)
# 	return prediction
 
# # kNN Algorithm
# def k_nearest_neighbors(train, test, num_neighbors):
# 	predictions = list()
# 	for row in test:
# 		output = predict_classification(train, row, num_neighbors)
# 		predictions.append(output)
# 	return(predictions)
 
# # Test the kNN on the Iris Flowers dataset
# seed(1)
# filename = 'iris.csv'
# dataset = load_csv(filename)
# for i in range(len(dataset[0])-1):
# 	str_column_to_float(dataset, i)
# # convert class column to integers
# str_column_to_int(dataset, len(dataset[0])-1)
# # evaluate algorithm
# n_folds = 5
# num_neighbors = 5
# scores = evaluate_algorithm(dataset, k_nearest_neighbors, n_folds, num_neighbors)
# print('Scores: %s' % scores)
# print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))