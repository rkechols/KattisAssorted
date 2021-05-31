from typing import List, Tuple


def pet(all_scores: List[List[int]]) -> Tuple[int, int]:
	best_index = None
	best_score = None
	for index, scores in enumerate(all_scores, start=1):
		this_score = sum(scores)
		if best_score is None or this_score > best_score:
			best_score = this_score
			best_index = index
	return best_index, best_score


if __name__ == "__main__":
	values = list()
	for i_ in range(5):
		line = input().split()
		values.append([int(v) for v in line])
	row, value = pet(values)
	print(f"{row} {value}")
