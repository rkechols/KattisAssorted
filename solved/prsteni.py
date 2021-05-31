from typing import List
from fractions import Fraction


def prsteni(rings: List[int]) -> List[Fraction]:
	current_speed = Fraction(1, 1)
	to_return = list()
	for i in range(len(rings) - 1):
		this_size = rings[i]
		next_size = rings[i + 1]
		ratio = Fraction(this_size, next_size)
		current_speed = current_speed * ratio
		to_return.append(current_speed)
	return to_return


if __name__ == "__main__":
	N = int(input())
	ring_radii = [int(v) for v in input().split()]
	assert len(ring_radii) == N
	answer = prsteni(ring_radii)
	for frac in answer:
		print(f"{frac.numerator}/{frac.denominator}")
