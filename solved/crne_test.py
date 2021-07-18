from crne import crne


if __name__ == "__main__":
	all_passing = True
	for in_value, answer in [
		(1, 2),
		(3, 6)
	]:
		out = crne(in_value)
		if out != answer:
			print(f"wrong answer for input {in_value}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
