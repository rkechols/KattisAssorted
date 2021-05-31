from semafori import semafori


if __name__ == "__main__":
	all_passing = True
	for in_values, answer in [
		((10, [(3, 5, 5), (5, 2, 2)]), 12),
		((30, [(7, 13, 5), (14, 4, 4), (15, 3, 10), (25, 1, 1)]), 36)
	]:
		out = semafori(*in_values)
		if out != answer:
			print(f"wrong answer for input {in_values}: got {out} but expected {answer}")
			all_passing = False
	if all_passing:
		print("all tests passed!")
