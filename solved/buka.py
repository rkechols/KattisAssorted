ADD = "+"
MULTIPLY = "*"


def buka(n1: int, op: str, n2: int) -> int:
	if op == ADD:
		return n1 + n2
	elif op == MULTIPLY:
		return n1 * n2
	else:
		raise ValueError(f"UNKNOWN OPERATOR: {op}")


if __name__ == "__main__":
	A = int(input())
	OP = input()
	B = int(input())
	answer = buka(A, OP, B)
	print(answer)
