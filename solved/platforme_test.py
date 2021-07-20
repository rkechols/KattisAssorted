from platforme import platforme


if __name__ == "__main__":
	all_passing = True
	for in_value, answer in [
		([(1, 5, 10), (3, 1, 5), (5, 3, 7)], 14),
		([
			(50, 50, 90),
			(40, 40, 80),
			(30, 30, 70),
			(20, 20, 60),
			(10, 10, 50)
		], 200)
	]:
		out = platforme(in_value)
		if out != answer:
			print(f"wrong answer for input {in_value}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
