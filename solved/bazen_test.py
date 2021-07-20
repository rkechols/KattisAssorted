from bazen import bazen


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		((0, 0), (125.0, 125.0)),
		((230, 20), (0.0, 114.13)),
		((0, 40), (148.81, 101.19))
	]:
		out = bazen(*in_values)
		if not all(round(val, 2) == target for val, target in zip(out, answer)):
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
