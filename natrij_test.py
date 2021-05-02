from natrij import natrij


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		(("20:00:00", "20:00:00"), "24:00:00"),  # hidden test case?
		(("20:00:00", "04:00:00"), "08:00:00"),
		(("12:34:56", "14:36:22"), "02:01:26")
	]:
		out = natrij(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
