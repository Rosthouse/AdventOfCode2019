import math


##
def man_dist(p1: (int,  int), p2: (int, int)) -> int:
    return abs(abs(p1[0]) - abs(p2[0])) + abs(abs(p1[1]) - abs(p2[1]))


def lay_cable(wire: [str]) -> [(int, int)]:
    pos = (0, 0)
    switcher = {
        "R": lambda pos: (pos[0]+1, pos[1]),
        "L": lambda pos: (pos[0]-1, pos[1]),
        "U": lambda pos: (pos[0],   pos[1]+1),
        "D": lambda pos: (pos[0],   pos[1]-1)
    }
    cable = []
    for i in range(0, len(wire), 1):
        command = wire[i]
        op = command[0]
        count = int(command[1:])
        func = switcher.get(op)
        for j in range(0, count, 1):
            pos = func(pos)
            cable.append(pos)

    return cable


def find_intersections(w1: (int, int), w2: (int, int)) -> [(int, int)]:
    return set(w1) - (set(w1) - set(w2))


def calculate_min_intersection(w1: str, w2: str):
    wire1 = w1.split(",")
    wire2 = w2.split(",")

    cable1 = lay_cable(wire1)
    cable2 = lay_cable(wire2)

    intersections = find_intersections(cable1, cable2)
    print(intersections)
    min_pos = min(intersections, key=lambda p: man_dist((0, 0), p))
    print(min_pos)
    min_dist=man_dist((0, 0), min_pos)
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
