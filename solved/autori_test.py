from solved.autori import autori


if __name__ == "__main__":
	all_passing = True
	for n, answer in [("Knuth-Morris-Pratt", "KMP"), ("Mirko-Slavko", "MS"), ("Pasko-Patak", "PP")]:
		out = autori(n)
		if out != answer:
			print(f"wrong answer for input {n}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
