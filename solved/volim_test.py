from volim import volim


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		((1, [(20, "T"), (50, "T"), (80, "T"), (50, "T"), (30, "T")]), 5),
		((3, [(100, "T"), (100, "N"), (100, "T"), (100, "T"), (100, "N")]), 4),
		((5, [(70, "T"), (50, "P"), (30, "N"), (50, "T"), (30, "P"), (80, "T")]), 7)
	]:
		out = volim(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
