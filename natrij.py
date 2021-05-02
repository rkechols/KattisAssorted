SEC_PER_MIN = 60
MIN_PER_H = 60
H_PER_DAY = 24
DELIMITER = ":"


def timestamp_to_sec(t: str) -> int:
	chunks = t.split(DELIMITER)
	hours = int(chunks[0])
	minutes = int(chunks[1])
	seconds = int(chunks[2])
	return seconds + (SEC_PER_MIN * minutes) + (SEC_PER_MIN * MIN_PER_H * hours)


def sec_to_timestamp(t: int) -> str:
	hours = t // (SEC_PER_MIN * MIN_PER_H)
	hours %= H_PER_DAY
	t_min = t % (SEC_PER_MIN * MIN_PER_H)
	minutes = t_min // SEC_PER_MIN
	seconds = t_min % SEC_PER_MIN
	hours_str = str(hours)
	hours_str = ("0" * (2 - len(hours_str))) + hours_str
	minutes_str = str(minutes)
	minutes_str = ("0" * (2 - len(minutes_str))) + minutes_str
	seconds_str = str(seconds)
	seconds_str = ("0" * (2 - len(seconds_str))) + seconds_str
	return DELIMITER.join([hours_str, minutes_str, seconds_str])


def natrij(time_now: str, time_boom: str) -> str:
	time_now_sec = timestamp_to_sec(time_now)
	time_boom_sec = timestamp_to_sec(time_boom)
	if time_boom_sec < time_now_sec:
		time_boom_sec += (SEC_PER_MIN * MIN_PER_H * H_PER_DAY)
	diff = time_boom_sec - time_now_sec
	return sec_to_timestamp(diff)


if __name__ == "__main__":
	t1 = input()
	t2 = input()
	answer = natrij(t1, t2)
	print(answer)
