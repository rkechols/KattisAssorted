from typing import List


GOES = "goes "
GOES_LEN = len(GOES)
TRIGGER = "what does the fox say?"


def fox_say(ambient_sound: str, known_sounds: List[str]) -> str:
	known_set = set()
	for sound_description in known_sounds:
		goes_index = sound_description.find(GOES)
		sound = sound_description[(goes_index + GOES_LEN):]
		known_set.add(sound)
	to_return = list()
	for sound in ambient_sound.split():
		if sound not in known_set:
			to_return.append(sound)
	return " ".join(to_return)


if __name__ == "__main__":
	N = int(input())
	for _ in range(N):
		ambient = input()
		known = list()
		while True:
			line = input()
			if line == TRIGGER:
				break
			known.append(line)
		answer = fox_say(ambient, known)
		print(answer)
