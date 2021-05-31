from typing import Set, Tuple


ADRIAN = "Adrian"
BRUNO = "Bruno"
GORAN = "Goran"

ADRIAN_SEQ = ["A", "B", "C"]
BRUNO_SEQ = ["B", "A", "B", "C"]
GORAN_SEQ = ["C", "C", "A", "A", "B", "B"]

N_ADRIAN = len(ADRIAN_SEQ)
N_BRUNO = len(BRUNO_SEQ)
N_GORAN = len(GORAN_SEQ)


def ptice(answers: str) -> Tuple[int, Set[str]]:
	a_score = 0
	b_score = 0
	g_score = 0
	for i, answer in enumerate(answers):
		if ADRIAN_SEQ[i % N_ADRIAN] == answer:
			a_score += 1
		if BRUNO_SEQ[i % N_BRUNO] == answer:
			b_score += 1
		if GORAN_SEQ[i % N_GORAN] == answer:
			g_score += 1
	winning_score = max(a_score, b_score, g_score)
	winners_set = set()
	if a_score == winning_score:
		winners_set.add(ADRIAN)
	if b_score == winning_score:
		winners_set.add(BRUNO)
	if g_score == winning_score:
		winners_set.add(GORAN)
	return winning_score, winners_set


if __name__ == "__main__":
	N = int(input())
	answer_line = input()
	assert len(answer_line) == N
	score, winners = ptice(answer_line)
	print(score)
	for winner in sorted(winners):
		print(winner)
