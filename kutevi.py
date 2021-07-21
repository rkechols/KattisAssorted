from typing import List


def kutevi(known_angles: List[int], required_angles: List[int]) -> List[bool]:
	required_angles_alt = [360 - angle for angle in required_angles]
	to_return = list()
	for i in range(len(required_angles)):
		if required_angles[i] in known_angles or required_angles_alt[i] in known_angles:
			to_return.append(True)
		else:
			to_return.append(False)
	return to_return


if __name__ == "__main__":
	N, K = tuple(map(int, input().split()))
	known = list(map(int, input().split()))
	required = list(map(int, input().split()))
	answers = kutevi(known, required)
	for answer in answers:
		if answer:
			print("YES")
		else:
			print("NO")
