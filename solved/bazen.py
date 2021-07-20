from typing import Tuple, Union


INFINITY = float("inf")


class Point:
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y

	def __eq__(self, other):
		if not isinstance(other, Point):
			return False
		return self.x == other.x and self.y == other.y

	def __repr__(self):
		return f"Point({self.x}, {self.y})"


def iso_center(p1: Point, p2: Point, p3: Point) -> Point:
	iso_x = (p1.x + p2.x + p3.x) / 3
	iso_y = (p1.y + p2.y + p3.y) / 3
	return Point(iso_x, iso_y)


class Line:
	def __init__(self, m: float, b: float = None, x_intercept: float = None):
		self.m = m
		assert not (b is None and x_intercept is None), "either b or x_intercept must be provided"
		if b is None:
			if m == INFINITY or m == -INFINITY:
				self.b = None
			else:
				self.b = -m * x_intercept
		else:
			self.b = b
		if x_intercept is None:
			if self.m == 0:
				self.x_intercept = None
			else:
				self.x_intercept = -self.b / self.m
		else:
			self.x_intercept = x_intercept

	def f(self, x: float) -> float:
		return self.m * x + self.b

	def __repr__(self):
		return f"Line({self.m}, {self.b}, {self.x_intercept})"

	def is_on_line(self, point: Point) -> bool:
		if self.m == INFINITY or self.m == -INFINITY:
			return point.x == self.x_intercept
		expected_y = self.f(point.x)
		return abs(expected_y - point.y) < 0.0001

	@staticmethod
	def from_points(p1: Point, p2: Point):  # -> Line:
		if p1.x == p2.x:
			return Line(INFINITY, x_intercept=p1.x)
		# line from two points:
		# y = y_1 + ((y_1 - y_2) / (x_1 - x_2) * (x - x_1)
		m = slope(p1, p2)
		b = p2.y - m * p2.x
		return Line(m, b)
	
	@staticmethod
	def from_point_slope(point: Point, m: float):  # -> Line:
		if m == INFINITY or m == -INFINITY:
			return Line(m, x_intercept=point.x)
		# y = m * x + (y_1 - m * x_1)
		b = point.y - (m * point.x)
		return Line(m, b)


def slope(p1: Point, p2: Point) -> float:
	if p1.x == p2.x:
		return INFINITY
	return (p2.y - p1.y) / (p2.x - p1.x)


def intersect(line_1: Line, line_2: Line) -> Union[None, Point]:
	if line_1.m == line_2.m:  # parallel
		return None
	# x1 = x2
	# m1 * x1 + b1 = m2 * x2 + b2
	if line_1.m == INFINITY or line_1.m == -INFINITY:
		x = line_1.x_intercept
		y = line_2.f(x)
	elif line_2.m == INFINITY or line_2.m == -INFINITY:
		x = line_2.x_intercept
		y = line_1.f(x)
	else:
		x = (line_2.b - line_1.b) / (line_1.m - line_2.m)
		y = line_1.f(x)
	return Point(x, y)


def in_bounding_box(corner_1: Point, corner_2: Point, target: Point) -> bool:
	if corner_1.x <= corner_2.x:
		if not (corner_1.x <= target.x <= corner_2.x):
			return False
	else:
		if not (corner_2.x <= target.x <= corner_1.x):
			return False
	# x is fine, now check y
	if corner_1.y <= corner_2.y:
		if not (corner_1.y <= target.y <= corner_2.y):
			return False
	else:
		if not (corner_2.y <= target.y <= corner_1.y):
			return False
	# both are fine
	return True


def midpoint(p1: Point, p2: Point) -> Point:
	return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)


POINT_A = Point(0, 0)
POINT_B = Point(0, 250)
POINT_C = Point(250, 0)

LINE_AB = Line.from_points(POINT_A, POINT_B)
LINE_BC = Line.from_points(POINT_B, POINT_C)
LINE_CA = Line.from_points(POINT_C, POINT_A)

ISO_CENTER = iso_center(POINT_A, POINT_B, POINT_C)


def bazen(x: int, y: int) -> Tuple[float, float]:
	start_point = Point(x, y)
	if LINE_AB.is_on_line(start_point):
		far_corner = POINT_C
		this_midpoint = midpoint(POINT_A, POINT_B)
		base_line = LINE_AB
	elif LINE_BC.is_on_line(start_point):
		far_corner = POINT_A
		this_midpoint = midpoint(POINT_B, POINT_C)
		base_line = LINE_BC
	elif LINE_CA.is_on_line(start_point):
		far_corner = POINT_B
		this_midpoint = midpoint(POINT_C, POINT_A)
		base_line = LINE_CA
	else:
		raise ValueError("given point not on any line?")
	slope_to_parallel = slope(start_point, far_corner)
	dividing_line = Line.from_point_slope(this_midpoint, slope_to_parallel)
	for other_line in [LINE_AB, LINE_BC, LINE_CA]:
		if other_line is base_line:
			continue  # we don't want it to give use the start point back
		end_point = intersect(dividing_line, other_line)
		if end_point is None:  # parallel, no intersection
			continue
		# check if this intersection is on an actual edge of the triangle or outside of it
		if other_line is LINE_AB and not in_bounding_box(POINT_A, POINT_B, end_point):
			continue
		if other_line is LINE_BC and not in_bounding_box(POINT_B, POINT_C, end_point):
			continue
		if other_line is LINE_CA and not in_bounding_box(POINT_C, POINT_A, end_point):
			continue
		# good to go
		return end_point.x, end_point.y
	raise ValueError("Can't find the answer :(")


if __name__ == "__main__":
	x_in, y_in = tuple(map(int, input().split()))
	x_out, y_out = bazen(x_in, y_in)
	print(f"{x_out:.2f} {y_out:.2f}")
