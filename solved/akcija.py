from typing import List


def akcija(prices: List[int]) -> int:
	prices.sort(reverse=True)
	total = 0
	for i, p in enumerate(prices, start=1):
		if i % 3 != 0:
			total += p
	return total


if __name__ == "__main__":
	n = int(input())
	values = list()
	for _ in range(n):
		values.append(int(input()))
	answer = akcija(values)
	print(answer)
