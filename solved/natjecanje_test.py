from solved.natjecanje import natjecanje


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		(([1, 3, 6, 7, 9, 11, 12, 13], [0, 2, 4, 5, 8, 10, 15, 16]), 3),
		(([2, 4], [1, 3, 5]), 0),
		(([2, 4], [3]), 1)
	]:
		out = natjecanje(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}:")
			print(f"actual:\n{out}")
			print(f"expected:\n{answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
