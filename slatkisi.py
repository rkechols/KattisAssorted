def slatkisi(cost: int, bill_power: int) -> int:
	bill_value = 10 ** bill_power
	bill_count = cost // bill_value
	remainder = cost % bill_value
	portion = remainder / bill_value
	if portion >= 0.5:
		bill_count += 1
	return bill_count * bill_value


if __name__ == "__main__":
	c, k = (int(v) for v in input().split())
	answer = slatkisi(c, k)
	print(answer)
