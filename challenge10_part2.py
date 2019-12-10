import math
import utils


def vec_angle(vec: (int, int)) -> float:
    ang = 90.0 if vec[1] == 0 else (
        math.atan(vec[0]/vec[1]) * 180 / math.pi) % 360
    return ang


def parseAsteroids(text: str) -> [(int, int)]:
    asteroids = []
    rows = [list(x) for x in text.splitlines(False)]
    for y in range(0, len(rows), 1):
        for x in range(0, len(rows[0]), 1):
            if not rows[y][x] == ".":
                asteroids.append((x, y))

    return asteroids


def vaporize(asteroids, angles, vaporStop=0) -> (int, int):

    currentAngleIndex = angles.index(90.0)

    vaporizeCounter = 0
    while True:
        currentAngle = angles[currentAngleIndex]
        nextAsteroids = [x for x in asteroids if x[2] == currentAngle]
        if len(nextAsteroids) > 0:
            nextAsteroids.sort(key=utils.length)
            vaporized = nextAsteroids.pop(0)

            vaporizeCounter += 1
            if vaporizeCounter >= vaporStop:
                return vaporized
            asteroids.remove(vaporized)
        currentAngleIndex = (currentAngleIndex + 1) % len(angles)


asteroids = parseAsteroids(""".#....###24...#..
##...##.13#67..9#
##...#...5.8####.
..#.....X...###..
..#.#.....#....##""")

center = (8, 3)

angles = []
asteroids = list(map(lambda x: (x[0] , x[1], vec_angle((x[0]-center[0], x[1] - center[1]))), asteroids))
asteroids = [x for x in asteroids if not (x[0], x[1]) == (0, 0)]
angles = list(dict.fromkeys(map(lambda x: x[2], asteroids)))
asteroids.sort(key=lambda x: x[2], reverse=True)
angles.sort(reverse=True)

print(
    f"Expected (8,1) vaporized: { utils.add(vaporize(asteroids, angles, 1), center)}")
