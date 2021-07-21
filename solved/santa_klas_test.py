from santa_klas import santa_klas


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		((30, 270), 30),
		((1, 180), None)
	]:
		out = santa_klas(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
