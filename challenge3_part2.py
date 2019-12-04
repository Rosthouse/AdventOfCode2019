# Advent of Code 2019: Day 3, Part 2
# https://adventofcode.com/2019/day/3
class Cell:

    def __init__(self, x: int, y: int, steps: int):
        self.x = x
        self.y = y
        self.steps = steps

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.steps) + ")"


def man_dist(p1: Cell, p2: Cell) -> int:
    return abs(abs(p1.x) - abs(p2.x)) + abs(abs(p1.y) - abs(p2.y))


def lay_cable(wire: [str]) -> [Cell]:
    pos = (0, 0)
    switcher = {
        "R": lambda pos: (pos[0]+1, pos[1]),
        "L": lambda pos: (pos[0]-1, pos[1]),
        "U": lambda pos: (pos[0],   pos[1]+1),
        "D": lambda pos: (pos[0],   pos[1]-1)
    }
    cable: [Cell] = []
    step_counter = 1
    for i in range(0, len(wire), 1):
        command = wire[i]
        op = command[0]
        count = int(command[1:])
        func = switcher.get(op)
        for j in range(0, count, 1):
            pos = func(pos)
            cable.append(Cell(pos[0], pos[1], step_counter))
            step_counter += 1

    return cable


def find_intersections(w1: [Cell], w2: [Cell]) -> [Cell]:
    return set(w1).intersection(set(w2))


def steps_for_intersections(intersections: [Cell], c1: [Cell], c2: [Cell]) -> [int]:
    steps: [int] = []
    for int_cell in intersections:
        cell1 = next(x for x in c1 if x == int_cell)
        cell2 = next(x for x in c2 if x == int_cell)
        steps.append(cell1.steps + cell2.steps)
    return steps


def calculate_min_intersection(w1: str, w2: str):
    wire1 = w1.split(",")
    wire2 = w2.split(",")

    cable1 = lay_cable(wire1)
    cable2 = lay_cable(wire2)

    intersections = find_intersections(cable1, cable2)

    steps = steps_for_intersections(intersections, cable1, cable2)

    zero = Cell(0, 0, 0)

    min_pos: Cell = min(intersections, key=lambda p: man_dist(zero, p))
    min_dist = man_dist(zero, min_pos)
    min_steps: int = min(steps)
    print("Minimum steps: " + str(min_steps))
    return min_dist


print("Expected 6, actual: " +
      str(calculate_min_intersection("R8,U5,L5,D3", "U7,R6,D4,L4")))
print("Expected 159, actual: " + str(calculate_min_intersection(
    "R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83")))
print("Expected 135, actual: " + str(calculate_min_intersection(
    "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")))

f = open("./res/challenge3.txt")
wire1 = f.readline()
wire2 = f.readline()

print("Min intersections: " + str(calculate_min_intersection(wire1, wire2)))
