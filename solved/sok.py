from typing import List
from fractions import Fraction


def sok(purchased: List[int], need: List[int]) -> List[float]:
	assert len(purchased) == len(need)
	ratios = [Fraction(p, n) for p, n in zip(purchased, need)]
	limiting_ingredient_ratio = ratios[0]
	for this_ratio in ratios[1:]:
		if this_ratio < limiting_ingredient_ratio:
			limiting_ingredient_ratio = this_ratio
	used_amounts = [n * limiting_ingredient_ratio for n in need]
	remaining_amounts = [float(p - u) for p, u in zip(purchased, used_amounts)]
	return remaining_amounts


if __name__ == "__main__":
	purchased_ints = [int(v) for v in input().split()]
	need_ints = [int(v) for v in input().split()]
	answer = sok(purchased_ints, need_ints)
	print(" ".join(["{:.6f}".format(v) for v in answer]))
