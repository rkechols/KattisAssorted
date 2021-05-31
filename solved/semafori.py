from typing import List, Tuple


def semafori(length: int, lights: List[Tuple[int, int, int]]) -> int:
	current_position = 0
	time_spent = 0
	for location, red, green in lights:
		# drive up to this light
		time_spent += (location - current_position)
		current_position = location
		# where are we in its cycle?
		period = red + green
		remainder = time_spent % period
		# how long until it turns green?
		time_to_green = red - remainder
		if time_to_green > 0:  # we need to wait
			time_spent += time_to_green
	# don't forget from the last light to the end of the road
	time_spent += (length - current_position)
	return time_spent


if __name__ == "__main__":
	N, L = [int(v) for v in input().split()]
	lights_list = list()
	for _ in range(N):
		D, R, G = [int(v) for v in input().split()]
		lights_list.append((D, R, G))
	answer = semafori(L, lights_list)
	print(answer)
