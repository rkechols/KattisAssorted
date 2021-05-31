from typing import List, Tuple


CORRECT = "T"
# INCORRECT = "N"
# PASS = "P"
NUM_PLAYERS = 8
TIME_LIMIT_SECONDS = (3 * 60) + 30


def volim(starting_player_label: int, questions: List[Tuple[int, str]]) -> int:
	current_player_index = starting_player_label - 1
	current_time = 0
	for q_time, answer_type in questions:
		current_time += q_time
		if current_time > TIME_LIMIT_SECONDS:  # does it explode during this question?
			return current_player_index + 1
		if answer_type == CORRECT:  # at the end of this question, do they pass it?
			current_player_index += 1
			current_player_index %= NUM_PLAYERS
	return -1  # they answered all the questions?


if __name__ == "__main__":
	K = int(input())
	N = int(input())
	question_list = list()
	for _ in range(N):
		line_split = input().split()
		question_list.append((int(line_split[0]), line_split[1]))
	answer = volim(K, question_list)
	print(answer)
