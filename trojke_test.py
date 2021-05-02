from trojke import trojke


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		(["...D", "..C.", ".B..", "A..."], 4),
		(["..T..", "A....", ".FE.R", "....X", "S...."], 3),
		(["....AB....", "..C....D..", ".E......F.", "...G..H...", "I........J", "K........L", "...M..N...", ".O......P.", "..Q....R..", "....ST...."], 0)
	]:
		out = trojke(in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
		else:
			print(f"got it right: {answer}")
	if all_passing:
		print("all tests passed!")
