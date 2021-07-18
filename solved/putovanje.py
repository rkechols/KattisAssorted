from typing import List


def putovanje(capacity: int, values: List[int]) -> int:
	n = len(values)
	consumed_count = [0] * n
	consumed_weight = [0] * n
	for i, val in enumerate(values):
		for j in range(n):
			if i >= j:
				if consumed_weight[j] + val <= capacity:
					consumed_weight[j] += val
					consumed_count[j] += 1
	return max(consumed_count)


if __name__ == "__main__":
	N, C = tuple(map(int, input().split()))
	weights = list(map(int, input().split()))
	answer = putovanje(C, weights)
	print(answer)
