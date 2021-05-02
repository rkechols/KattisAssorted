from prva import prva


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		(["luka", "o#a#", "kula", "i#a#"], "kala"),  # multiple answers?
		(["luka", "o#a#", "kula", "i#as"], "as"),
		(["adaca", "da##b", "abb#b", "abbac"], "abb")  # wrong answer? what about "da"?
	]:
		out = prva(in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
		else:
			print(f"got it right: {answer}")
	if all_passing:
		print("all tests passed!")
