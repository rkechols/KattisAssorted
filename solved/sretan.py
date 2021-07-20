LOW_DIGIT = "4"
HIGH_DIGIT = "7"


def sretan(i: int) -> int:
	remainder = i - 1
	power = 2
	depth = 1
	while remainder >= power:
		remainder -= power
		power *= 2
		depth += 1
	binary_str = format(remainder, "b")
	padding_count = depth - len(binary_str)
	if padding_count > 0:
		binary_str = ("0" * padding_count) + binary_str
	digits = list()
	for c in binary_str:
		if c == "0":
			digits.append(LOW_DIGIT)
		else:  # c == "1"
			digits.append(HIGH_DIGIT)
	return int("".join(digits))


if __name__ == "__main__":
	in_val = int(input())
	answer = sretan(in_val)
	print(answer)
