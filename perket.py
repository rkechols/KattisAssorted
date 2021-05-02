from typing import List, Tuple


def prod(a: List[int]) -> int:
	if len(a) <= 0:
		raise ValueError("cannot take the product of a list with length less than 1!")
	to_return = a[0]
	for v in a[1:]:
		to_return *= v
	return to_return


def perket(ingredients: List[Tuple[int, int]]) -> int:
	i_count = len(ingredients)
	best = None
	for start_index in range(i_count):
		running_s, running_b = ingredients[start_index]
		running_net = abs(running_s - running_b)
		for i in range(start_index + 1, i_count):
			this_s, this_b = ingredients[i]
			new_s = running_s * this_s
			new_b = running_b + this_b
			new_net = abs(new_s - new_b)
			if new_net < running_net:
				running_net = new_net
		if best is None or running_net < best:
			best = running_net
	return best


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
