from typing import List


def natjecanje(broken_teams: List[int], reserve_teams: List[int]) -> int:
	unfixable_count = 0
	broken = set(broken_teams)
	reserve = set(reserve_teams)
	# figure out which teams use their own reserve
	fixed = set()
	for team_num in broken:
		if team_num in reserve:
			reserve.remove(team_num)
			fixed.add(team_num)
	broken.difference_update(fixed)
	# figure out which teams aren't next to a team with a reserve
	unfixable = set()
	for team_num in broken:
		if len({team_num - 1, team_num + 1}.difference(reserve)) == 2:
			# neither adjacent team has a reserve
			unfixable.add(team_num)
	unfixable_count += len(unfixable)
	broken.difference_update(unfixable)
	# figure out which teams have useless reserves
	useless = set()
	for team_num in reserve:
		if len({team_num - 1, team_num + 1}.difference(broken)) == 2:
			# neither adjacent team has a broken
			useless.add(team_num)
	reserve.difference_update(useless)
	# figure out what contiguous chunks are left and if they have:
	# - one more reserve than broken
	# - even reserve and broken
	# - one more broken than reserve
	# the number of chunks that are the last is the number of lost teams
	pairs = [(team_num, False) for team_num in broken] + [(team_num, True) for team_num in reserve]
	pairs.sort(key=lambda x: x[0])
	chunk_balance = 0
	for i, (team_num, is_ok) in enumerate(pairs):
		if is_ok:
			chunk_balance += 1
		else:
			chunk_balance -= 1
		# if the next team is unreachable, the same type, or we're at the end of the list,
		# that's the end of this chunk
		if i + 1 < len(pairs):
			next_team_num, next_is_ok = pairs[i + 1]
			if next_team_num > team_num + 1 or is_ok == next_is_ok:
				end_of_chunk = True
			else:
				end_of_chunk = False
		else:
			end_of_chunk = True
		if end_of_chunk:  # assess the chunk and reset for the new chunk
			assert chunk_balance in [-1, 0, 1]
			if chunk_balance == -1:
				unfixable_count += 1
			chunk_balance = 0
	return unfixable_count


if __name__ == "__main__":
	N, S, R = (int(v) for v in input().split())
	broken_all = [int(v) for v in input().split()]
	assert len(broken_all) == S
	reserved_all = [int(v) for v in input().split()]
	assert len(reserved_all) == R
	answer = natjecanje(broken_all, reserved_all)
	print(answer)
