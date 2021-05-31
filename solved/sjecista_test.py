from sjecista import sjecista


if __name__ == "__main__":
	all_passing = True
	for in_value, answer in [
		(3, 0),
		(4, 1),
		(5, 5),
		(6, 15)
	]:
		out = sjecista(in_value)
		if out != answer:
			print(f"wrong answer for input {in_value}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
