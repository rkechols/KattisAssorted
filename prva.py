from typing import List


BLOCK = "#"


def prva(all_scores: List[str]) -> str:
	best_word = None
	best_len = None
	# rows
	for row in all_scores:
		options = row.split(BLOCK)
		for option in options:
			this_len = len(option)
			if this_len < 2:
				continue
			if best_len is None or this_len < best_len:
				best_len = this_len
				best_word = option
	# columns
	for col_num in range(len(all_scores[0])):  # all are the same length, so the first will do
		col = "".join([row[col_num] for row in all_scores])
		options = col.split(BLOCK)
		for option in options:
			this_len = len(option)
			if this_len < 2:
				continue
			if best_len is None or this_len < best_len:
				best_len = this_len
				best_word = option
	return best_word


if __name__ == "__main__":
	line = input().split()
	r = int(line[0])
	c = int(line[1])
	values = list()
	for _ in range(r):
		line = input()
		assert len(line) == c
		values.append(line)
	answer = prva(values)
	print(answer)
