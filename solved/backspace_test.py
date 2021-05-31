from backspace import backspace


if __name__ == "__main__":
	all_passing = True
	for in_value, answer in [
		("a<bc<", "b"),
		("foss<<rritun", "forritun"),
		("a<a<a<aa<<", "")
	]:
		out = backspace(in_value)
		if out != answer:
			print(f"wrong answer for input {in_value}:")
			print(f"actual:\n{out}")
			print(f"expected:\n{answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
