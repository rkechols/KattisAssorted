from typing import List, Tuple


R = "R"
P = "P"
S = "S"
OPTIONS = [R, P, S]


def points(this: str, other: str) -> int:
	if this == R:
		if other == S:
			return 2
		elif other == R:
			return 1
		else:  # other == P
			return 0
	elif this == S:
		if other == P:
			return 2
		elif other == S:
			return 1
		else:  # other == R
			return 0
	else:  # this == P
		if other == R:
			return 2
		elif other == P:
			return 1
		else:  # other == S
			return 0


def majstor(player: str, opponents: List[str]) -> Tuple[int, int]:
	score_real_total = 0
	score_potential_total = 0
	for i in range(len(player)):
		real_pick = player[i]
		opponent_picks = [opp[i] for opp in opponents]
		scores = dict()
		for pick in OPTIONS:
			this_score = 0
			for opponent_pick in opponent_picks:
				this_score += points(pick, opponent_pick)
			scores[pick] = this_score
		score_real = scores[real_pick]
		score_potential = max(scores.values())
		score_real_total += score_real
		score_potential_total += score_potential
	return score_real_total, score_potential_total


if __name__ == "__main__":
	n_rounds = int(input())
	sven = input()
	N = int(input())
	friends = list()
	for _ in range(N):
		friends.append(input())
	actual_score, best_score = majstor(sven, friends)
	print(actual_score)
	print(best_score)
