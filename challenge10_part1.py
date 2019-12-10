
# import numpy as np
import math


def parseAsteroids(text: str) -> [(int, int)]:
    asteroids = []
    rows = [list(x) for x in text.splitlines(False)]
    for y in range(0, len(rows), 1):
        for x in range(0, len(rows[0]), 1):
            if rows[y][x] == "#":
                asteroids.append((x, y))

    return asteroids


def length(vec: (int, int)) -> float:
    return math.sqrt(math.pow(vec[0], 2) + math.pow(vec[1], 2))


def normalize(vec: (int, int)) -> (int, int):
    magn = length(vec)
    return (vec[0] / magn, vec[1] / magn)


def findClosest(center: (int, int), neighbors: [(int, int)]):
    closest = {}
    for neighbor in neighbors:
        direction = (neighbor[0] - center[0], neighbor[1] - center[1])
        magn = length(direction)
        angle =math.atan2(direction[0], direction[1]) * 180/math.pi
        if angle in closest:
            if magn < closest[angle][1]:
                closest[angle] = (neighbor, magn)
            else:
                continue
        else:
            closest[angle] = (neighbor, magn)
    return closest


def findBestVantagePoint(asteroids: [(int, int)]):
    bestVantagePoint = ((0, 0), 0)
    for asteroid in asteroids:
        distances = findClosest(
            asteroid, [x for x in asteroids if x != asteroid])
        # We add one for the center asteroid itself
        if len(distances) >= bestVantagePoint[1]:
            bestVantagePoint = (asteroid, len(distances))

    return bestVantagePoint


first = parseAsteroids(""".#..#
.....
#####
....#
...##""")

expected = [(1, 0), (4, 0), (0, 2), (1, 2), (2, 2),
            (3, 2), (4, 2), (4, 3), (3, 4), (4, 4)]
# assert(expected == first)

second = parseAsteroids("""......#.#.
# ..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
# ..#....#.
.##.#..###
# ...#..#.
.#....####""")
third = parseAsteroids("""#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.""")

fourth = parseAsteroids(""".#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..""")

fifth = parseAsteroids(""".#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""")

test = parseAsteroids(open("./res/challenge10.txt").read())

print(f"Expected ((3,4), 8): {findBestVantagePoint(first)}")
print(f"Expected ((5,8), 33): {findBestVantagePoint(second)}")
print(f"Expected ((1,2), 35): {findBestVantagePoint(third)}")
print(f"Expected ((6,3), 41): {findBestVantagePoint(fourth)}")
print(f"Expected ((11,13), 210): {findBestVantagePoint(fifth)}")


print(f"Actual:  {findBestVantagePoint(test)}")
