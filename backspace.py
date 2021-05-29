BACKSPACE = "<"


def backspace(text: str) -> str:
	stack = list()
	for c in text:
		if c == BACKSPACE:
			stack.pop(-1)
		else:
			stack.append(c)
	return "".join(stack)


if __name__ == "__main__":
	line = input()
	answer = backspace(line)
	print(answer)
