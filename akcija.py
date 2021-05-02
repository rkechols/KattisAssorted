from typing import List


def akcija(prices: List[int]) -> int:
	removable = len(prices) // 3
	prices.sort()
	return sum(prices[removable:])


if __name__ == "__main__":
	n = int(input())
	values = list()
	for _ in range(n):
		values.append(int(input()))
	answer = akcija(values)
	print(answer)
