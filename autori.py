def autori(line: str) -> str:
	to_return = list()
	for c in line:
		if c.isupper():
			to_return.append(c)
	return "".join(to_return)


if __name__ == "__main__":
	in_line = input()
	answer = autori(in_line)
	print(answer)
