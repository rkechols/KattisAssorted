from ptice import ptice


if __name__ == "__main__":
	all_passing = True
	for in_value, answer in [
		("BAACC", (3, {"Bruno"})),
		("AAAABBBBB", (4, {"Adrian", "Bruno", "Goran"})),
	]:
		out = ptice(in_value)
		if out != answer:
			print(f"wrong answer for input {in_value}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
