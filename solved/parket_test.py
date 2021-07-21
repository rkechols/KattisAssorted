from parket import parket


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		((8, 1), (3, 3)),
		((10, 2), (4, 3)),
		((24, 24), (8, 6))
	]:
		out = parket(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
