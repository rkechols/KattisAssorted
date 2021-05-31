from akcija import akcija


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		([3, 2, 3, 2], 8),
		([6, 4, 5, 5, 5, 5], 21)
	]:
		out = akcija(in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
