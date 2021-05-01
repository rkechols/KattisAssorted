def planina(iterations: int) -> int:
	segments_count = 2 ** iterations
	edge_point_count = segments_count + 1
	return edge_point_count ** 2


if __name__ == "__main__":
	n = int(input())
	answer = planina(n)
	print(answer)
