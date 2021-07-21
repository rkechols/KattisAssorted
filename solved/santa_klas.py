from typing import Union
from math import pi, sin


RAD_PER_DEG = 2 * pi / 360


def santa_klas(altitude: int, angle: int) -> Union[int, None]:
	if 0 <= angle <= 180:
		return None
	if angle == 270:
		return altitude
	if 180 < angle < 270:
		angle -= 180
	else:
		angle = 360 - angle
	angle *= RAD_PER_DEG
	# angle is now the angle of depression in radians
	# distance * sin(angle) = altitude
	distance = altitude / sin(angle)
	return int(distance)


if __name__ == "__main__":
	H, V = tuple(map(int, input().split()))
	answer = santa_klas(H, V)
	if answer is None:
		print("safe")
	else:
		print(answer)
