from typing import Union


UNKNOWN = "eh"


def letter_to_index(letter: str) -> int:
	return ord(letter) - ord("a")


class TrieNode:
	def __init__(self, value: str = None):
		self.value = value
		self.children = list()
		for _ in range(letter_to_index("z")):
			self.children.append(None)

	def set(self, location: str, value: str):
		index = letter_to_index(location[0])
		if len(location) == 1:  # base case
			if self.children[index] is None:
				self.children[index] = TrieNode(value)
			else:
				self.children[index].value = value
		else:
			if self.children[index] is None:
				self.children[index] = TrieNode()
			self.children[index].set(location[1:], value)

	def get(self, location: str) -> Union[str, None]:
		index = letter_to_index(location[0])
		if self.children[index] is None:
			return None  # dead end
		if len(location) == 1:  # base case
			return self.children[index].value
		return self.children[index].get(location[1:])


if __name__ == "__main__":
	dictionary = TrieNode()
	while True:
		line = input()
		if line == "":
			break
		familiar, foreign = line.split()
		dictionary.set(foreign, familiar)
	try:
		while True:
			foreign = input()
			if foreign == "":
				break
			familiar = dictionary.get(foreign)
			if familiar is None:
				print(UNKNOWN)
			else:
				print(familiar)
	except EOFError:
		pass  # just don't crash
