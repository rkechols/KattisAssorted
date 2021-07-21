from typing import List, Tuple
from math import sqrt


class Pipe:
	def __init__(self, parent_id: int, child_id: int, flow: int, power: int):
		self.parent_id = parent_id
		self.child_id = child_id
		self.flow = flow
		self.power = (power == 1)


class Node:
	def __init__(self, node_id: int):
		self.id = node_id
		self.parent_id = None
		self.children = dict()

	def add_child(self, child_id: int, flow: int, power: bool):
		self.children[child_id] = (flow, power)

	def is_leaf(self) -> bool:
		return len(self.children) == 0

	# def __repr__(self) -> str:  # for debugging
	# 	return f"Node(id={self.id}, parent_id={self.parent_id}, children={self.children})"


def needed_fluid(node_id: int, nodes: List[Node], leaves: List[int]) -> float:
	curr_node = nodes[node_id]
	if curr_node.is_leaf():
		return leaves[node_id]
	actual_total_need = None
	for child_id, (flow, power) in curr_node.children.items():
		child_need = needed_fluid(child_id, nodes, leaves)
		if power:
			child_need = sqrt(child_need)
		total_need = child_need / (flow / 100)
		if actual_total_need is None or actual_total_need < total_need:
			actual_total_need = total_need
	return actual_total_need


def mravi(pipes: List[Tuple[int, int, int, int]], leaves: List[int]) -> float:
	n = len(pipes) + 1
	pipes = [Pipe(*tup) for tup in pipes]
	nodes = [Node(i) for i in range(n)]  # id's are shifted down from the input
	for pipe in pipes:
		nodes[pipe.parent_id - 1].add_child(pipe.child_id - 1, pipe.flow, pipe.power)
		nodes[pipe.child_id - 1].parent_id = pipe.parent_id - 1
	required_total = needed_fluid(0, nodes, leaves)
	return required_total


if __name__ == "__main__":
	N = int(input())
	pipe_info = list()
	for _ in range(N - 1):
		pipe_info.append(tuple(map(int, input().split())))
	leaf_info = list(map(int, input().split()))
	answer = mravi(pipe_info, leaf_info)
	print(answer)
