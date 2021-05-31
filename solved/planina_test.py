from solved.planina import planina


if __name__ == "__main__":
	all_passing = True
	for n, answer in [(1, 9), (2, 25), (5, 1089)]:
		out = planina(n)
		if out != answer:
			print(f"wrong answer for input {n}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
