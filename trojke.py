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
	# forward diagonals
	for offset in range((-1 * size) + 1, size):
		s = ""
		for i in range(size):
			j = i + offset
			if 0 <= i < size and 0 <= j < size:  # on the board:
				s += board[i][j]
		assert s != ""
		count += count_from_line(s)
	# backward diagonals
	for offset in range((-1 * size) + 1, size):
		s = ""
		for i in range(size):
			j = (size - 1) + offset - i
			if 0 <= i < size and 0 <= j < size:  # on the board:
				s += board[i][j]
		assert s != ""
		count += count_from_line(s)
	return count


if __name__ == "__main__":
	n = int(input())
	values = list()
	for _ in range(n):
		line = input()
		assert len(line) == n
		values.append(line)
	answer = trojke(values)
	print(answer)
