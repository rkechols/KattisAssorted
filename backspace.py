BACKSPACE = "<"


def backspace(text: str) -> str:
	stack = list()
	delete_count = 0
	for c in reversed(text):
		if c == BACKSPACE:
			delete_count += 1
		else:
			if delete_count > 0:
				delete_count -= 1
			else:
				stack.append(c)
	return "".join(reversed(stack))


if __name__ == "__main__":
	line = input()
	answer = backspace(line)
	print(answer)
