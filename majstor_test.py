from majstor import majstor


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		(("SSPPR", ["SSPPR"]), (5, 10)),
		(("SSPPR", ["PPRRS", "RRSSP"]), (10, 15)),
		(("SPRS", ["RPRP", "SRRR", "SSPR", "PSPS"]), (12, 21))
	]:
		out = majstor(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}:")
			print(f"actual:\n{out}")
			print(f"expected:\n{answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
