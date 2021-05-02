from typing import List


def rot(text_grid: List[str], angle: int) -> str:
	pass  # TODO


if __name__ == "__main__":
	line = input().split()
	r = int(line[0])
	c = int(line[1])
	values = list()
	for _ in range(r):
		line = input()
		assert len(line) == c
		values.append(line)
	k = int(input())
	assert k % 45 == 0
	answer = rot(values, k)
	print(answer, end="")
