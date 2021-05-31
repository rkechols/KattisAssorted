from sibice import sibice


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		((3, 4, [3, 4, 5, 6, 7]), ["DA", "DA", "DA", "NE", "NE"]),
		((12, 17, [21, 20]), ["NE", "DA"])
	]:
		out = sibice(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
