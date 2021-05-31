def sjecista(n: int) -> int:
	count = 0
	existing_lines = list()
	for i in range(n):
		for j in range(i + 2, n):
			if i + n - j == 1:
				continue  # outside edges don't intersect with anything
			for other_i, other_j in existing_lines:
				if i == other_i or i == other_j or j == other_i or j == other_j:
					continue  # distinct diagonals that share a vertex can't intersect
				if other_i < i < other_j < j:  # they cross
					count += 1
			existing_lines.append((i, j))
	return count


if __name__ == "__main__":
	N = int(input())
	answer = sjecista(N)
	print(answer)
