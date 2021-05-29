from slatkisi import slatkisi


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		((184, 1), 180),
		((123450995, 1), 123451000),
		((182, 2), 200)
	]:
		out = slatkisi(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}:")
			print(f"actual:\n{out}")
			print(f"expected:\n{answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
