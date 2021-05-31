from solved.tarifa import tarifa


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		((10, [4, 6, 2]), 28),
		((10, [10, 2, 12]), 16),
		((15, [15, 10, 20]), 15)
	]:
		out = tarifa(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
