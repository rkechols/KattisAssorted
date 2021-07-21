SANIC_R = 1.0


def sanic(r: float) -> float:
	rotations_if_flat = r / SANIC_R
	return rotations_if_flat - 1


if __name__ == "__main__":
	loop_radius = float(input())
	answer = sanic(loop_radius)
	print(answer)
