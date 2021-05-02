import math
from typing import List


BLOCK = "."
FAC3 = math.factorial(3)


def combinations3(x: int) -> int:
	return math.factorial(x) // (FAC3 * math.factorial(x - 3))


def count_non_block(s: str) -> int:
	count = 0
	for c in s:
		if c != BLOCK:
			count += 1
	return count


def count_from_line(s: str) -> int:
	non_block = count_non_block(s)
	if non_block == 3:
		return 1
	elif non_block < 3:
		return 0
	else:
		return combinations3(non_block)


def trojke(board: List[str]) -> int:
	size = len(board)
	count = 0
	# rows
	for row in board:
		count += count_from_line(row)
	# columns
	for index in range(len(board[0])):  # every row is the same size, so the first is fine:
		col = "".join([row[index] for row in board])
		count += count_from_line(col)
	# diagonals at all slopes
	used_slopes = dict()
	for row_step in range(1, (size // 2) + 1):
		for col_step in range(1, (size // 2) + 1):
			gcd = math.gcd(row_step, col_step)
			row_step = row_step // gcd
			col_step = col_step // gcd
			this_slope = (row_step, col_step)
			if this_slope in used_slopes:
				continue
			used_slopes[this_slope] = set()
			shortest_row_delta = 2 * row_step
			shortest_col_delta = 2 * col_step
			start_row = 0
			while start_row + shortest_row_delta < size:
				start_col = 0
				while start_col + shortest_col_delta < size:
					if (start_row, start_col) in used_slopes[this_slope]:
						start_col += 1
						continue  # we've already done this line
					# use the determined slope and start location to pull a line out
					s1 = ""
					s2 = ""  # also do a 90-degree rotation so we get "negative" slopes
					r = start_row
					c = start_col
					# print(f"slope {this_slope} at ({r}, {c})")
					while 0 <= r < size and 0 <= c < size:
						used_slopes[this_slope].add((r, c))
						s1 += board[r][c]
						s2 += board[size - (c + 1)][r]
						r += row_step
						c += col_step
					# check how many things we get out of the line
					count += count_from_line(s1)
					count += count_from_line(s2)
					# go to the next line
					start_col += 1
				start_row += 1
	return count


if __name__ == "__main__":  # TODO: not all tests are passing
	n = int(input())
	values = list()
	for _ in range(n):
		line = input()
		assert len(line) == n
		values.append(line)
	answer = trojke(values)
	print(answer)
