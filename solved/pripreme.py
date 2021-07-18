from typing import List


def pripreme(times: List[int]) -> int:
	from_max = max(times) * 2
	direct = sum(times)
	return max(from_max, direct)


if __name__ == "__main__":
	N = int(input())
	values = list(map(int, input().split()))
	answer = pripreme(values)
	print(answer)
