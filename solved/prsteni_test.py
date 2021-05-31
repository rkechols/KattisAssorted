from solved.prsteni import prsteni
from fractions import Fraction


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		([8, 4, 2], [Fraction(2, 1), Fraction(4, 1)]),
		([12, 3, 8, 4], [Fraction(4, 1), Fraction(3, 2), Fraction(3, 1)]),
		([300, 1, 1, 300], [Fraction(300, 1), Fraction(300, 1), Fraction(1, 1)])
	]:
		out = prsteni(in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}:")
			print(f"actual:\n{out}")
			print(f"expected:\n{answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
