from zamka import zamka


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		((1, 100, 4), (4, 40)),
		((100, 500, 12), (129, 480)),
		((1, 10000, 1), (1, 10000))
	]:
		out = zamka(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
