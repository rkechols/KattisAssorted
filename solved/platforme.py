from copy import copy
from typing import List, Tuple


class Interval:
	def __init__(self, value: int, left: int, right: int):
		if value < 0:
			raise ValueError("value must be non-negative")
		if left > right:
			raise ValueError("must satisfy left <= right")
		self.value = value
		self.left = left
		self.right = right

	def __lt__(self, other):
		assert isinstance(other, Interval)
		return self.value < other.value

	def __repr__(self) -> str:
		return f"Interval({self.value}, left={self.left}, right={self.right})"


class SegmentTree:
	def __init__(self):
		self.data = list()
		self.max = 0

	def add(self, new_interval: Interval):
		if new_interval.value < self.max:
			raise ValueError("values must be added in order lowest to highest")
		i = 0
		while i < len(self.data):
			if self.data[i].left < new_interval.left:
				if new_interval.left <= self.data[i].right <= new_interval.right:
					self.data[i].right = new_interval.left
				elif new_interval.right < self.data[i].right:
					to_split = copy(self.data[i])
					self.data[i].right = new_interval.left
					self.data.insert(i + 1, Interval(to_split.value, new_interval.right, to_split.right))
					i += 1
				# else:  # self.data[i].right < new_interval.left:
				# 	pass  # no overlap
			elif new_interval.left <= self.data[i].left <= new_interval.right:
				if self.data[i].right <= new_interval.right:
					self.data.pop(i)
					i -= 1
				else:  # new_interval.right < self.data[i].right
					self.data[i].left = new_interval.right
			# else:  # new_interval.right < self.data[i].left
			# 	pass  # no overlap
			i += 1
		self.data.append(new_interval)
		self.max = new_interval.value  # intervals only added in order lowest to highest

	def get(self, location: float) -> int:
		for interval in self.data:
			if interval.left <= location <= interval.right:
				return interval.value
		return 0


def platforme(platforms: List[Tuple[int, int, int]]) -> int:
	platforms = [Interval(*platform_tup) for platform_tup in platforms]
	platforms.sort()
	tree = SegmentTree()
	total = 0
	for platform in platforms:
		total += (platform.value - tree.get(platform.left + 0.5))
		total += (platform.value - tree.get(platform.right - 0.5))
		tree.add(platform)
	return total


if __name__ == "__main__":
	platform_count = int(input())
	all_platforms = list()
	for _ in range(platform_count):
		all_platforms.append(tuple(map(int, input().split())))
	answer = platforme(all_platforms)
	print(answer)
