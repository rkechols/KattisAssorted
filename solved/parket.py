from math import sqrt
from typing import Tuple


def parket(border_squares: int, inner_squares: int) -> Tuple[int, int]:
	total_squares = border_squares + inner_squares
	for edge_1 in range(3, 1 + int(sqrt(total_squares))):
		if total_squares % edge_1 != 0:
			continue  # not divisible
		edge_2 = total_squares // edge_1
		inner_squares_maybe = (edge_1 - 2) * (edge_2 - 2)
		if inner_squares_maybe != inner_squares:
			continue
		border_squares_maybe = (edge_1 * 2) + 2 * (edge_2 - 2)
		if border_squares_maybe != border_squares:
			continue
		return edge_2, edge_1  # they want the bigger one first
	raise ValueError("no answer found")


if __name__ == "__main__":
	R, B = tuple(map(int, input().split()))
	answer = parket(R, B)
	print(f"{answer[0]} {answer[1]}")
