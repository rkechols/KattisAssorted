from solved.rot import rot


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		((["damir", "marko", "darko"], 45), "  d\n m a\nd a m\n a r i\n  r k r\n   k o\n    o\n"),
		((["damir", "marko", "darko"], 90), "dmd\naaa\nrrm\nkki\noor\n"),
		((["abcde", "bcdef", "cdefg", "defgh", "efghi"], 315), "    e\n   d f\n  c e g\n b d f h\na c e g i\n b d f h\n  c e g\n   d f\n    e\n")
	]:
		out = rot(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}:")
			print(f"actual:\n{out}")
			print(f"expected:\n{answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
