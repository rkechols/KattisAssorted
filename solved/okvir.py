from typing import List


HASH = "#"
DOT = "."


def okvir(up: int, left: int, right: int, down: int, content: List[str]) -> List[str]:
	m = len(content)
	n = len(content[0])
	shape_0 = up + m + down
	shape_1 = left + n + right
	arr = list()
	for i in range(shape_0):
		row = list()
		for j in range(shape_1):
			if (i + j) % 2 == 0:
				row.append(HASH)
			else:
				row.append(DOT)
		arr.append(row)
	for i, row in enumerate(content, start=up):
		for j, char in enumerate(row, start=left):
			arr[i][j] = char
	to_return = ["".join(arr[i]) for i in range(shape_0)]
	return to_return


if __name__ == "__main__":
	M, N = (int(v) for v in input().split())
	U, L, R, D = (int(v) for v in input().split())
	values = list()
	for _ in range(M):
		line = input()
		assert len(line) == N
		values.append(line)
	answer = okvir(U, L, R, D, values)
	for line in answer:
		print(line)
