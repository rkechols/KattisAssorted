from sok import sok


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		(([10, 10, 10], [3, 3, 3]), [0.0, 0.0, 0.0]),
		(([9, 9, 9], [3, 2, 1]), [0.0, 3.0, 6.0]),
		(([10, 15, 18], [3, 4, 1]), [0.0, 1.666667, 14.666667])
	]:
		out = sok(*in_values)
		diff = [abs(o - a) for o, a in zip(out, answer)]
		if not all([d < 10e-4 for d in diff]):
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
