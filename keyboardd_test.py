from keyboardd import keyboardd


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		(("this is very annoying", "thiss iss veery annoying"), "se"),
		(("so sticky", "ssoo  ssttiicckkyy"), "its yock")
	]:
		out = keyboardd(*in_values)
		out_set = {c for c in out}
		answer_set = {c for c in answer}
		if out_set != answer_set:
			print(f"wrong answer for input {in_values}:")
			print(f"actual:\n{out_set}")
			print(f"expected:\n{answer_set}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
