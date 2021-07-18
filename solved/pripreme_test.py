from pripreme import pripreme


if __name__ == "__main__":
	all_passing = True
	for in_value, answer in [
		([2, 2, 2], 6),
		([4, 1, 2], 8),
		([1, 3, 2, 1], 7)
	]:
		out = pripreme(in_value)
		if out != answer:
			print(f"wrong answer for input {in_value}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
