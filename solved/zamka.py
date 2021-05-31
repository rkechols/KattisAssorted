from typing import Tuple


def sum_digits_matches(to_sum: int, val: int) -> bool:
	remaining = to_sum
	total = 0
	while remaining > 0:
		total += (remaining % 10)
		remaining = (remaining // 10)
		if total > val:
			return False
	return total == val


def zamka(lower: int, upper: int, x: int) -> Tuple[int, int]:
	first = None
	for attempt in range(lower, upper + 1, 1):
		if sum_digits_matches(attempt, x):
			first = attempt
			break
	second = None
	for attempt in range(upper, lower - 1, -1):
		if sum_digits_matches(attempt, x):
			second = attempt
			break
	return first, second


if __name__ == "__main__":
	low = int(input())
	high = int(input())
	target = int(input())
	n, m = zamka(low, high, target)
	print(n)
	print(m)
