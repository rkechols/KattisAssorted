from okvir import okvir


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		((2, 2, 2, 2, ["honi", "oker", "nera", "irak"]), ["#.#.#.#.", ".#.#.#.#", "#.honi#.", ".#oker.#", "#.nera#.", ".#irak.#", "#.#.#.#.", ".#.#.#.#"]),
		((1, 0, 3, 1, ["rima", "mama"]), ["#.#.#.#", "rima.#.", "mama#.#", ".#.#.#."])
	]:
		out = okvir(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}:")
			print(f"actual:\n{out}")
			print(f"expected:\n{answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
