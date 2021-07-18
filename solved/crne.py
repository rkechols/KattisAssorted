def crne(cuts: int) -> int:
	cuts_per_direction = cuts // 2
	pieces = (cuts_per_direction + 1) ** 2
	if cuts % 2 != 0:
		pieces += (cuts_per_direction + 1)
	return pieces


if __name__ == "__main__":
	N = int(input())
	answer = crne(N)
	print(answer)
