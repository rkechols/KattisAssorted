from typing import List


ANSWERS = {0: "none", 1: "one", 2: "both"}


def vauvau(d1_agg: int, d1_calm: int, d2_agg: int, d2_calm: int, heroes: List[int]) -> List[int]:
	d1_period = d1_agg + d1_calm
	d2_period = d2_agg + d2_calm
	to_return = list()
	for hero_time in heroes:
		count = 0
		d1_remainder = hero_time % d1_period
		if 0 < d1_remainder <= d1_agg:
			count += 1
		d2_remainder = hero_time % d2_period
		if 0 < d2_remainder <= d2_agg:
			count += 1
		to_return.append(count)
	return to_return


if __name__ == "__main__":
	A, B, C, D = [int(v) for v in input().split()]
	hero_times = [int(v) for v in input().split()]
	answer_ints = vauvau(A, B, C, D, hero_times)
	for answer_int in answer_ints:
		assert answer_int in ANSWERS
		print(ANSWERS[answer_int])
