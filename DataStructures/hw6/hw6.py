# Olivia Pannell
# Homework 6

import sys

class knapSack():
 
	# Initialize items and mcal lists
	def __init__(self, n, W, v, c, f):
		self.n = n
		self.W = W	
		self.v = v	
		self.c = c
		self.f = f			
		self.items = [0]*(n + 1)
		self.items[0] = 0
		for i in range(1, n+1):
			self.items[i] = 0

		self.cal = [0]*(W + 1)
		for i in range(1,W):
			self.cal[i] = float('INF')
		self.cal[0] = 0

		self.number = [0]*(W+1)

	def mcal(self, W, n):
		# Find the minimum amount of cals 
		# while not going past W
		for i in range(1, W + 1):
			minimum = float('INF')
			for j in range(0, n):
				temp = 0
				if((i - self.v[j]) < 0):
					temp = float('INF')
				else:
					temp = self.cal[i - self.v[j]] + self.c[j]
				if(temp < minimum):
					minimum = temp
					self.number[i] = j
					self.items[j] += 1
			self.cal[i] = minimum

		return self.cal[W]

	def knap(self):
		# Calls mcal and gets the calorie minimum
		minimum = self.mcal(self.W, self.n)

		# Check if possible
		if(self.cal[self.W] == float('INF')):
			print("Not possible to spend exactly:", self.W)
			return 0
		else:
			print("Possible to spend exactly:", self.W)
			print("Minimum Calories:", self.cal[self.W])

		# Is possible and find which foods were used
		# Prints out how many times and the food
		value = self.W
		result = [0]*(self.n)
		for i in range(0,self.n):
			result[i] = 0
		while(value != 0):
			temp = self.number[value]
			result[temp] = result[temp] + 1
			value = value - self.v[temp]

		for i in range(0, self.n):
			if(result[i] != 0):
				print(self.f[i], result[i])

def main():
	#Gets the items
	items = sys.stdin.readline()
	items = int(items)

	# Gets the budget
	budget = sys.stdin.readline()
	budget = int(budget)

	# Set a recursion limit to allow it to work
	sys.setrecursionlimit(budget)

	#Holds each in a list
	cost = []
	cal = []
	food = []

	# Initialize knap and finds the cost, calorie and food name
	# Then calls the add function in knapsack
	for i in range(items):
		v, c, f = sys.stdin.readline().strip().split(" ")
		v = int(v)
		c = int(c)
		cost.append(v)
		cal.append(c)
		food.append(f)

	knap = knapSack(items, budget, cost, cal, food)
	knap.knap()
	return 0


if __name__ == "__main__":
	main()
