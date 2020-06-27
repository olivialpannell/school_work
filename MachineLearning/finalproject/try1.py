"""
To be turned into a neural network
"""
import numpy as np

board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
pos = [0, 0]
empty = 0
team1 = "X"
team2 = "a"
win = "W"
your_team = team1
other_team = team2

def place():
	board[3][0] = team2
	board[4][0] = team2
	board[5][0] = team2

def horizontal_win(r, c, t, t2):
	if board[r][c + 2] == t and board[r][c + 3] == t and board[r][c + 1] == 0:
		if r == 5 or board[r + 1][c + 1] == t or board[r + 1][c + 1] == t2:
			pos[0] = r
			pos[1] = c + 1
			print("Case:", 1)
			return 1
	if board[r][c + 1] == t and board[r][c + 3] == t and board[r][c + 2] == 0:
		if r == 5 or board[r + 1][c + 2] == t or board[r + 1][c + 2] == t2:
			pos[0] = r
			pos[1] = c + 2
			print("Case:", 2)
			return 1
	if board[r][c + 1] == t and board[r][c + 2] == t and board[r][c + 3] == 0:
		if r == 5 or board[r + 1][c + 3] == t or board[r + 1][c + 3] == t2:
			pos[0] = r
			pos[1] = c + 3
			print("Case:", 3)
			return 1

	if board[r][c + 1] == t and board[r][c + 2] == t and board[r][c - 1] == 0:
		if r == 5 or board[r + 1][c - 1] == t or board[r + 1][c - 1] == t2:
			pos[0] = r
			pos[1] = c - 1
			print("Case:", 4)
			return 1
	if board[r][c - 1] == t and board[r][c + 2] == t and board[r][c + 1] == 0:
		if r == 5 or board[r + 1][c + 1] == t or board[r + 1][c + 1] == t2:
			pos[0] = r
			pos[1] = c + 1
			print("Case:", 5)
			return 1
	if board[r][c - 1] == t and board[r][c + 1] == t and board[r][c + 2] == 0:
		if r == 5 or board[r + 1][c + 2] == t or board[r + 1][c + 2] == t2:
			pos[0] = r
			pos[1] = c + 2
			print("Case:", 6)
			return 1

	if board[r][c - 1] == t and board[r][c + 1] == t and board[r][c - 2] == 0:
		if r == 5 or board[r + 1][c - 2] == t or board[r + 1][c - 2] == t2:
			pos[0] = r
			pos[1] = c - 2
			print("Case:", 7)
			return 1
	if board[r][c - 2] == t and board[r][c + 1] == t and board[r][c - 1] == 0:
		if r == 5 or board[r + 1][c - 1] == t or board[r + 1][c - 1] == t2:
			pos[0] = r
			pos[1] = c - 1
			print("Case:", 8)
			return 1
	if board[r][c - 2] == t and board[r][c - 1] == t and board[r][c + 1] == 0:
		if r == 5 or board[r + 1][c + 1] == t or board[r + 1][c + 1] == t2:
			pos[0] = r
			pos[1] = c + 1
			print("Case:", 9)
			return 1

	if board[r][c - 2] == t and board[r][c - 1] == t and board[r][c - 3] == 0:
		if r == 5 or board[r + 1][c - 3] == t or board[r + 1][c - 3] == t2:
			pos[0] = r
			pos[1] = c - 3
			print("Case:", 10)
			return 1
	if board[r][c - 3] == t and board[r][c - 1] == t and board[r][c - 2] == 0:
		if r == 5 or board[r + 1][c - 2] == t or board[r + 1][c - 2] == t2:
			pos[0] = r
			pos[1] = c - 2
			print("Case:", 11)
			return 1
	if board[r][c - 3] == t and board[r][c - 2] == t and board[r][c - 1] == 0:
		if r == 5 or board[r + 1][c - 1] == t or board[r + 1][c - 1] == t2:
			pos[0] = r
			pos[1] = c - 1
			print("Case:", 12)
			return 1

	return 0

def vertical_win(r, c, t):
	if board[r - 1][c] == t and board[r - 2][c] == t and board[r - 3][c] == 0:
		pos[0] = r - 3
		pos[1] = c
		print("Case:", 13)
		return 1

	return 0

def diagonal_win(r, c, t, t2):
	return 0

def could_win(t, t2):
	for row in range(len(board)):
		for col in range(len(board[0])):
			if board[row][col] == t:
				if horizontal_win(row, col, t, t2):
					return 1
				if vertical_win(row, col, t):
					return 1
				if diagonal_win(row, col, t, t2):
					return 1
	return 0

def main():
	place()
	if could_win(your_team, other_team):
		board[pos[0]][pos[1]] = win
	if could_win(other_team, your_team):
		board[pos[0]][pos[1]] = your_team
	for i in range(6):
		print("+---+---+---+---+---+---+---+")
		print("|", board[i][0], "|", board[i][1], "|", board[i][2],
			"|", board[i][3], "|", board[i][4], "|", board[i][5], "|",
			board[i][6], "|")
	print("+---+---+---+---+---+---+---+")

if __name__ == "__main__":
	main()