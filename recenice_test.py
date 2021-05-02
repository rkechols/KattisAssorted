from recenice import recenice


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		(["this", "sentence", "has", "$", "letters"], "this sentence has thirtyone letters "),
		(["$", "is", "the", "number", "of", "letters", "here"], "thirty is the number of letters here "),
		(["the", "letters", "are", "$", "potato"], "the letters are twentynine potato ")
	]:
		out = recenice(in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}:")
			print(f"actual:\n{out}")
			print(f"expected:\n{answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
