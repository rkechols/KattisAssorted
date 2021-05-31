from vauvau import vauvau


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		((2, 2, 3, 3, [1, 3, 4]), [2, 1, 0]),
		((2, 3, 4, 5, [4, 9, 5]), [1, 0, 0])
	]:
		out = vauvau(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
