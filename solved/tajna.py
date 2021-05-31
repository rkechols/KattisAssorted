from typing import Tuple


def factorize_best(x: int) -> Tuple[int, int]:
	for r in reversed(range(1, int(x ** 0.5) + 1)):
		if x % r == 0:  # it's a factor
			c = x // r
			return r, c
	return -1, -1  # never happens since r ends up as 1


def tajna(encrypted: str) -> str:
	n = len(encrypted)
	r, c = factorize_best(n)
	to_return = list()
	for row in range(r):
		for col in range(c):
			to_return.append(encrypted[row + (col * r)])
	return "".join(to_return)


if __name__ == "__main__":
	encrypted_message = input()
	answer = tajna(encrypted_message)
	print(answer)
