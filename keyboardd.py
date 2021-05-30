import sys
from typing import List, Tuple


INFINITY = float("inf")
MATCH = -3
DUPLICATE = 5
SUB = INFINITY

# constants
# LEFT = "L"
UP = "U"
DIAGONAL = "D"
NULL_CHAR = "-"


def make_scores_array(width, height) -> List[List]:
	scores = list()
	for _ in range(height):
		scores.append([None] * width)
	return scores


def token_alignment_full(string1, string2) -> Tuple[float, str]:
	width = len(string1) + 1
	height = len(string2) + 1
	assert height > width, "the longer string should be the second parameter"
	# make the blank scoring table
	scores = make_scores_array(width, height)

	# set values in the first row
	scores[0][0] = (0, None)
	# for col in range(1, len(scores[0])):
	# 	# copy from the left
	# 	scores[0][col] = (scores[0][col - 1][0] + DUPLICATE, LEFT)

	# calculate remaining scores
	for row in range(1, len(scores)):
		for col in range(len(scores[row])):
			if col < width - (height - row):
				continue  # skip the lower left triangle
			if col > row:
				continue  # skip the upper right triangle
			if col == 0:  # first column
				# copy from above
				scores[row][col] = (scores[row - 1][col][0] + DUPLICATE, UP)
			else:
				# get the three possible scores
				# from_left = scores[row][col - 1][0] + DUPLICATE
				from_above_tup = scores[row - 1][col]
				if from_above_tup is None:
					from_above = INFINITY
				else:
					from_above = from_above_tup[0] + DUPLICATE
				if string1[col - 1] == string2[row - 1]:
					from_diagonal = scores[row - 1][col - 1][0] + MATCH
				else:
					from_diagonal = scores[row - 1][col - 1][0] + SUB
				# pick from the three options
				# if from_diagonal <= from_left and from_diagonal <= from_above:
				if from_diagonal <= from_above:
					# copy from the diagonal
					scores[row][col] = (from_diagonal, DIAGONAL)
				# elif from_left <= from_above:
				# 	# copy from the left
				# 	scores[row][col] = (from_left, LEFT)
				else:
					# copy from above
					scores[row][col] = (from_above, UP)

	# trace the path back
	string1_alignment = list()
	# string2_alignment = list()
	current_row = -1
	current_col = -1
	while True:
		parent_direction = scores[current_row][current_col][1]
		if parent_direction is None:
			break
		# get the alignment
		# if parent_direction == LEFT or parent_direction == DIAGONAL:
		if parent_direction == DIAGONAL:
			string1_alignment.insert(0, string1[current_col])
			current_col -= 1
		else:
			string1_alignment.insert(0, NULL_CHAR)
		# if parent_direction == UP or parent_direction == DIAGONAL:
		# string2_alignment.insert(0, string2[current_row])
		current_row -= 1
		# else:
		# 	string2_alignment.insert(0, NULL_CHAR)

	# return the final score and alignments
	return scores[-1][-1][0], "".join(string1_alignment)  # , "".join(string2_alignment)


def keyboardd(true_text: str, sticky_text: str) -> str:
	# score, edited_true_text, t2 = token_alignment_full(true_text, sticky_text)
	score, edited_true_text = token_alignment_full(true_text, sticky_text)
	print(f"score: {score}", file=sys.stderr)
	sticky_chars = set()
	for c1, c2 in zip(edited_true_text, sticky_text):
		if c1 == NULL_CHAR:
			sticky_chars.add(c2)
	return "".join(sticky_chars)


if __name__ == "__main__":
	true = input()
	sticky = input()
	answer = keyboardd(true, sticky)
	print(answer)
