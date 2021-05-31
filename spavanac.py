from typing import Tuple


HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60


def spavanac(hours: int, minutes: int, minutes_shift: int = -45) -> Tuple[int, int]:
	minutes += minutes_shift
	if minutes_shift < 0:
		while minutes < 0:
			minutes += MINUTES_PER_HOUR
			hours -= 1
	elif minutes_shift > 0:
		while minutes > MINUTES_PER_HOUR:
			minutes -= MINUTES_PER_HOUR
			hours += 1
	else:
		return hours, minutes
	hours %= HOURS_PER_DAY
	return hours, minutes


if __name__ == "__main__":
	H, M = (int(v) for v in input().split())
	H_out, M_out = spavanac(H, M)
	print(f"{H_out} {M_out}")
