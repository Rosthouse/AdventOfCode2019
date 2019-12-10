
# import numpy as np
import math
import utils


def parseAsteroids(text: str) -> [(int, int)]:
    asteroids = []
    rows = [list(x) for x in text.splitlines(False)]
    for y in range(0, len(rows), 1):
        for x in range(0, len(rows[0]), 1):
            if rows[y][x] == "#" or "X":
                asteroids.append((x, y))

    return asteroids


def groupAsteroidsByAngle(center: (int, int), neighbors: [(int, int)]):
    closest = {}
    for neighbor in neighbors:
        direction = (neighbor[0] - center[0], neighbor[1] - center[1])
        magn = utils.length(direction)
        # start upwards: correct by 90 degrees
        # -90 % 360, sort descending
        angle = math.atan2(direction[0], direction[1]) * 180/math.pi
        if not angle in closest:
            closest[angle] = []

        indexToInsert = 0
        for x in range(0, len(closest[angle]), 1):
            if closest[angle][x][1] <= magn:
                indexToInsert = x

        closest[angle].insert(indexToInsert, (neighbor, magn))

    return closest


def vaporize(asteroids: [(int, int)], center: (int, int)) -> [(int, int)]:
    group = groupAsteroidsByAngle(
        center, [x for x in asteroids if x != center])

    counter = 0
    while counter < 200:
        roundCounter = 0
        while roundCounter < len(group):
            key = list(group.keys())[roundCounter]
            group[key].pop()
            roundCounter += 1
            counter += 1
        
        for x in group
            if len(group[key]) == 0:
                group.pop(key)
    print(group)


first = parseAsteroids(""".#....#####...#..
##...##.#####..##
# ...#...#.#####.
..#.....X...###..
..#.#.....#....##""")

vaporize(first, (3, 8))
