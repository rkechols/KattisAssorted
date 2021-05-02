from pet import pet


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		([[5, 4, 4, 5],
		[5, 4, 4, 4],
		[5, 5, 4, 4],
		[5, 5, 5, 4],
		[4, 4, 4, 5]], (4, 19)),

		([[4, 4, 3, 3],
		[5, 4, 3, 5],
		[5, 5, 2, 4],
		[5, 5, 5, 1],
		[4, 4, 4, 4]], (2, 17))
	]:
		out = pet(in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
