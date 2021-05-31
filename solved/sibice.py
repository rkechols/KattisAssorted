from typing import List


YES = "DA"
NO = "NE"


def sibice(width: int, height: int, sizes: List[int]) -> List[str]:
	biggest = ((width ** 2) + (height ** 2)) ** 0.5
	to_return = list()
	for s in sizes:
		if s <= biggest:
			to_return.append(YES)
		else:
			to_return.append(NO)
	return to_return


if __name__ == "__main__":
	first_line = input().split(" ")
	n = int(first_line[0])
	w = int(first_line[1])
	h = int(first_line[2])
	values = list()
	for _ in range(n):
		values.append(int(input()))
	answer = sibice(w, h, values)
	for v in answer:
		print(v)
