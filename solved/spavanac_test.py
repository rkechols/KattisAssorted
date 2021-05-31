from solved.spavanac import spavanac


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		((10, 10), (9, 25)),
		((0, 30), (23, 45)),
		((23, 40), (22, 55))
	]:
		out = spavanac(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}:")
			print(f"actual:\n{out}")
			print(f"expected:\n{answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
