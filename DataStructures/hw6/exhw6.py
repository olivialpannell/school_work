# Olivia Pannell
# Homework 6

import sys
from collections import defaultdict

class knapSack():
 
	# Initializes knapsacks variables 
	# fills the count with 0's and table with -1
	def __init__(self, n, W):
		self.n = n
		self.W = W	
		self.count = []				
		self.food = defaultdict(list)
		self.table = {}

		for i in range(n + 1):
			self.count.append(0)
			self.food[i] = {}

		for i in range(self.W + 1):
			self.table[i] = [-1, -1]

	# Adds to Food which holds each cost, cal, and name of food
	def add(self, i, cost, cal, foodname):
		self.food[i][0] = cost
		self.food[i][1] = cal
		self.food[i][2] = foodname

	# Increase our count
	def upcount(self):
		temp = self.W
		while (temp > 0):
			self.count[self.table[temp][1]] += 1
			temp = temp - self.food[self.table[temp][1]][0]

	def mcal(self, W):
		current = 0
		item = 0
		minimum = float('INF')

		# Checks if less then budget
		if (W < 0):
			return float('INF')
		elif (W == 0):
			return 0
		elif (self.table[W][0] != -1):
			return self.table[W][0]

		# Saves minimum and adds it to the table
		for i in range(0, self.n):
			current = self.mcal(W - self.food[i][0]) + self.food[i][1]
			if (current < minimum and current >= 0):
				minimum = current
				item = i

		self.table[W][0] = minimum
		self.table[W][1] = item

		return minimum

	def knap(self):
		# Calls mcal and gets the calorie minimum
		minimum = self.mcal(self.W)

		# Checks if possible and if yes prints out how many times and the food
		if(minimum == float('INF')):
			print("Not possible to spend exactly:", self.W)
		else:
			print("Possible to spend exactly:", self.W)
			print("Minimum calories:", minimum)
			self.upcount()
			for i in range(1, self.n):
				if (self.count[i] > 0):
					print(self.food[i][2], self.count[i])
		return 0

def main():
	#Gets the items
	items = sys.stdin.readline()
	items = int(items)

	# Gets the budget
	budget = sys.stdin.readline()
	budget = int(budget)

	# Set a recursion limit to allow it to work
	sys.setrecursionlimit(budget)

	# Initialize knap and finds the cost, calorie and food name
	# Then calls the add function in knapsack
	knap = knapSack(items, budget)
	for i in range(items):
		v, c, f = sys.stdin.readline().strip().split(" ")
		v = int(v)
		c = int(c)
		knap.add(i, v, c, f)

	knap.knap()
	return 0


if __name__ == "__main__":
	main()
