from typing import List, Tuple


def prod(a: List[int]) -> int:
	if len(a) <= 0:
		raise ValueError("cannot take the product of a list with length less than 1!")
	to_return = a[0]
	for v in a[1:]:
		to_return *= v
	return to_return


def perket(ingredients: List[Tuple[int, int]]) -> int:
	smallest = None
	i_count = len(ingredients)
	for combo_dec in range(1, 2 ** i_count):
		combo_bin = format(combo_dec, "b")
		combo_bin = ("0" * (i_count - len(combo_bin))) + combo_bin  # pad the front with 0
		sours = list()
		bitters = list()
		for i, bit in enumerate(combo_bin):
			if bit == "1":
				this_s, this_b = ingredients[i]
				sours.append(this_s)
				bitters.append(this_b)
		s_score = prod(sours)
		b_score = sum(bitters)
		net_score = abs(s_score - b_score)
		if smallest is None or net_score < smallest:
			smallest = net_score
	return smallest


if __name__ == "__main__":
	n = int(input())
	values = list()
	for _ in range(n):
		line = input().split()
		s = int(line[0])
		b = int(line[1])
		values.append((s, b))
	answer = perket(values)
	print(answer)
