from typing import List


def rot(grid: List[str], angle: int) -> str:
	angle *= -1
	while angle < 0:
		angle += 360
	r = len(grid)
	c = len(grid[0])
	num_90 = angle // 90
	num_90 %= 4
	remainder = angle % 90
	if num_90 == 0:
		new_grid = grid
	elif num_90 == 1:
		new_grid = list()
		for index in range(c - 1, -1, -1):
			new_grid.append("".join([row[index] for row in grid]))
	elif num_90 == 2:
		new_grid = list()
		for row in reversed(grid):
			new_grid.append(row[::-1])
	elif num_90 == 3:
		new_grid = list()
		for index in range(c):
			new_grid.append("".join([row[index] for row in reversed(grid)]))
	else:
		raise ValueError("got a rotation that doesn't make sense")
	if remainder == 0:
		return "\n".join(new_grid) + "\n"
	assert remainder == 45
	r = len(new_grid)
	c = len(new_grid[0])
	# rotate the last 45 degrees
	s = ""
	for col in range(c - 1, -1, -1):
		for _ in range(col):
			s += " "
		temp = list()
		for row in range(r):
			if row + col >= c:
				break
			temp.append(new_grid[row][col + row])
		s += " ".join(temp)
		s += "\n"
	for row in range(1, r):
		for _ in range(row):
			s += " "
		temp = list()
		for col in range(c):
			if row + col >= r:
				break
			temp.append(new_grid[row + col][col])
		s += " ".join(temp)
		s += "\n"
	return s


if __name__ == "__main__":
	line = input().split()
	r_count = int(line[0])
	c_count = int(line[1])
	values = list()
	for _ in range(r_count):
		line = input()
		assert len(line) == c_count
		values.append(line)
	k = int(input())
	assert k % 45 == 0
	answer = rot(values, k)
	print(answer, end="")
