# Olivia Pannell
# Lab 0
# This program which will read a series of pairs of integers X and
# Y and print pairs X + Y and X * Y
from sys import stdin


def main():
    #get the first line
    count = stdin.read(2)

    # read the however many series of numbers comes next
    # seperate each line and print out the sum and products
    for i in range(int(count)):
		num = stdin.readline()
		num = num.strip()
		num = num.split(' ')
		mult = int(num[0]) * int(num[1])
		add = int(num[0]) + int(num[1])
		print(add),
		print(mult)


if __name__ == "__main__":
    main()
