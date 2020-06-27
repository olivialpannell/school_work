# Olivia Pannell
# Homework 2

import sys

def main():
	#get the number of vertices
	nodes = sys.stdin.readline()
	nodes = int(nodes)

	#get the number of edges
	edges = sys.stdin.readline()
	edges = int(edges)

	#create an empty matrix
	adjmatrix = []
	for i in range(nodes):
		arr = []
		for j in range(nodes):
			arr.append(0)
		adjmatrix.append(arr)

	#read the edges
	for i in range(edges):
		edge = sys.stdin.readline()
		l = edge.strip().split(' ')
		#print(l)
		n = int(l[0])
		#print(n)
		m = int(l[1])
		adjmatrix[n-1][m-1] = 1

	# print(adjmatrix)

	#The following is based off of dijkstra's algorithm

	#Finds the shortest path
	shortest = [0]*(nodes + 1)
	shortest[0] = 0
	paths = [0]*(nodes + 1)
	paths[0] = 1
	

	for i in range(1, nodes+1):
		shortest[i] = float('inf')

	for i in range(2, nodes + 1):
		paths[i] = 0

	print(paths)
	for i in range(nodes):
		for j in range(nodes):
			if(adjmatrix[i][j] == 1):
				if((shortest[i]+1) < shortest[j]):
					shortest[j] = shortest[i] + 1
					paths[j] = paths[i]
				elif(shortest[i] + 1 == shortest[j]):
					paths[j] = paths[j] + paths[i]


	print('Shortest path: ', end = ' ')
	print(shortest[nodes -1])

	print('Number of shortest paths: ', end = ' ')
	print(paths[nodes - 1])
	print(paths)


	#Finds the longest path
	longest = [0]*(nodes + 1)
	longest[0] = 0
	
	#reset paths
	for i in range(1, nodes + 1):
		paths[i] = 0
	paths[0] = 1

	for i in range(1, nodes+1):
		longest[i] = float('-inf')

	# print(longest)

	for i in range(nodes):
		for j in range(nodes):
			if(adjmatrix[i][j] == 1):
				if(i != j):
					if((longest[i]+1) > longest[j]):
						longest[j] = longest[i] + 1
						paths[j] = paths[i]
					elif(longest[i] + 1 == longest[j]):
						paths[j] = paths[j] + paths[i]


	print('Longest path: ', end = ' ')
	print(longest[nodes -1])

	print('Number of Longest paths:', end = ' ')
	print(paths[nodes - 1])


	return 0


if __name__ == "__main__":
    main()
