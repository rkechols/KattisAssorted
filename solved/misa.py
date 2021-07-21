from typing import List, Tuple, Union


EMPTY = "."
PERSON = "o"


def count_neighbors(chapel: List[List[str]], r: int, c: int) -> int:
	n_rows = len(chapel)
	n_cols = len(chapel[0])
	neighbor_count = 0
	for r_shift in [-1, 0, 1]:
		r_neighbor = r + r_shift
		if not 0 <= r_neighbor < n_rows:
			continue
		for c_shift in [-1, 0, 1]:
			if r_shift == 0 and c_shift == 0:
				continue
			c_neighbor = c + c_shift
			if not 0 <= c_neighbor < n_cols:
				continue
			if chapel[r_neighbor][c_neighbor] == PERSON:
				neighbor_count += 1
	return neighbor_count


def find_best_seat(chapel: List[List[str]]) -> Union[Tuple[int, int], None]:
	best_r = None
	best_c = None
	best_count = None
	for r, row in enumerate(chapel):
		for c, seat in enumerate(row):
			if seat == PERSON:
				continue
			neighbor_count = count_neighbors(chapel, r, c)
			if best_count is None or best_count < neighbor_count:
				best_r = r
				best_c = c
				best_count = neighbor_count
	if best_r is None or best_c is None:
		return None
	return best_r, best_c


def misa(chapel: List[str]) -> int:
	chapel = [[c for c in row] for row in chapel]
	best_seat = find_best_seat(chapel)
	if best_seat is not None:
		chapel[best_seat[0]][best_seat[1]] = PERSON
	# count handshakes
	n_rows = len(chapel)
	n_cols = len(chapel[0])
	shakes = 0
	for r in range(n_rows):
		for c in range(n_cols):
			if chapel[r][c] == PERSON:
				shakes += count_neighbors(chapel, r, c)
				chapel[r][c] = EMPTY
	return shakes


if __name__ == "__main__":
	R, S = tuple(map(int, input().split()))
	rows = list()
	for _ in range(R):
		rows.append(input())
	answer = misa(rows)
	print(answer)
