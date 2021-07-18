from putovanje import putovanje


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		((5, [3, 1, 2, 1, 1]), 4),
		((5, [1, 5, 4, 3, 2, 1, 1]), 3),
		((10, [3, 2, 5, 4, 3]), 3)
	]:
		out = putovanje(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
