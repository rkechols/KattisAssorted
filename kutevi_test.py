from kutevi import kutevi


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		(([30, 70], [40]), [True]),
		(([100], [60]), [True]),
		(([10, 20, 30], [5, 70]), [False, True])
	]:
		out = kutevi(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
