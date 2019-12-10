
import numpy as np


def parseAsteroids(text: str) -> [(int, int)]:
    asteroids = []
    rows = [list(x) for x in text.splitlines(False)]
    for y in range(0, len(rows), 1):
        for x in range(0, len(rows[0]), 1):
            if rows[y][x] == "#":
                asteroids.append((x, y))

    return asteroids


def findClosest(center: (int, int), neighbors: [(int, int)]):
    centerArr = np.array(center)
    closest = {}
    print(f"Testing {center}")
    for neighbor in neighbors:
        neighborArr = np.array(neighbor)
        direction = np.subtract(neighborArr, centerArr)
        magn = np.linalg.norm(direction)
        angle = np.arctan2(neighborArr[1], neighborArr[0])
        if angle in closest:
            if magn <= closest[angle][1]:
                print(f"{neighbor} hides {closest[angle][0]}")
                closest[angle] = (neighbor, magn)
            else:
                print(f"Invisible: {neighbor}")
        else:
            print(f"Inserting {neighbor} at {angle}")
            closest[angle] = (neighbor, magn)

        # closest[angle] = min(closest.get(angle, np.inf), dist)
    return closest


def findBestVantagePoint(asteroids: [(int, int)]):
    bestVantagePoint = ((0, 0), 0)
    for asteroid in asteroids:
        distances = findClosest(
            asteroid, [x for x in asteroids if x != asteroid])
        # We add one for the center asteroid itself
        if len(distances) > bestVantagePoint[1]:
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
print(f"First: {findBestVantagePoint(first)}")
# print(f"Second: {findBestVantagePoint(second)}")
# print(f"Third: {findBestVantagePoint(third)}")
