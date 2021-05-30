from fox_say import fox_say


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
			(("toot woof wa ow ow ow pa blub blub pa toot pa blub pa pa ow pow toot",
			["dog goes woof", "fish goes blub", "elephant goes toot", "seal goes ow"]
			), "wa pa pa pa pa pa pow")
	]:
		out = fox_say(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}:")
			print(f"actual:\n{out}")
			print(f"expected:\n{answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
