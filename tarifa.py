from typing import List


def tarifa(allowance: int, history: List[int]) -> int:
	remaining = 0
	for val in history:
		remaining += allowance
		remaining -= val
	return remaining + allowance


if __name__ == "__main__":
	x = int(input())
	n = int(input())
	values = list()
	for _ in range(n):
		values.append(int(input()))
	answer = tarifa(x, values)
	print(answer)
