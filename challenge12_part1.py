import utils
import math


def getStartPositions(path: str) -> [(int, int, int)]:
    lines = path.splitlines()
    planets = []
    for line in lines:
        positions = line.replace("<", "").replace(
            ">", "").replace(" ", "").split(",")
        position = tuple([int(x.split("=")[-1]) for x in positions])
        # position = (int(positions[0][:1]), int(
        #     positions[1][:1]), int(positions[2][:1]))
        planets.append(position)
    return planets


def calculateEnergy(positions: [(int, int, int)], velocities: [(int, int, int)]) -> None:
        # Then, it might help to calculate the total energy in the system. The total energy for
        # a single moon is its potential energy multiplied by its kinetic energy. A moon's potential
        #  energy is the sum of the absolute values of its x, y, and z position coordinates.
        # A moon's kinetic energy is the sum of the absolute values of its velocity coordinates.
        # Below, each line shows the calculations for a moon's potential energy (pot), kinetic energy (kin), and total energy:
    potTot = 0
    kinTot = 0
    totEn = 0
    for pos, vel in zip(positions, velocities):
        pot = sum(utils.absVec(pos))
        kin = sum(utils.absVec(vel))
        potTot += pot
        kinTot += kin
        en = pot * kin
        totEn += en
        print(f"{pos}/{vel}: pot = {pot}, kin = {kin}, total = {en}")

    print(
        f"Total pot energy: {potTot}; Total kin energy: {kinTot}; Total energy: {totEn}")


def simulate(positions: [(int, int, int)], iterations) -> None:
    velocities = [(0, 0, 0) for x in range(0, len(positions), 1)]
    for i in range(0, iterations, 1):
        print(f"Iteration {i}")
        # To apply gravity, consider every pair of moons. On each axis (x, y, and z),
        # the velocity of each moon changes by exactly +1 or -1 to pull the moons together.
        # For example, if Ganymede has an x position of 3, and Callisto has a x position of 5,
        # then Ganymede's x velocity changes by +1 (because 5 > 3) and Callisto's x velocity
        # changes by -1 (because 3 < 5). However, if the positions on a given axis are the
        # same, the velocity on that axis does not change for that pair of moons.
        for center in range(0, len(positions), 1):
            for neighbor in range(0, len(positions), 1):
                diff = utils.subtract(positions[neighbor], positions[center])
                signed = tuple([utils.sign(x) for x in diff])
                velocities[center] = utils.add(velocities[center], signed)

        for p in range(0, len(positions), 1):
            positions[p] = utils.add(positions[p], velocities[p])

        message = [f"Position: {positions[x]}, velocity: {velocities[x]}" for x in range(
            0, len(positions), 1)]

        for m in message:
            print(m)
    calculateEnergy(positions, velocities)


startPositions = getStartPositions("""<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""")
print(f"Start: {startPositions}")
simulate(startPositions, 10)

startPositions = getStartPositions("""<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>""")
simulate(startPositions, 100)

startPositions = getStartPositions(open("./res/challenge12.txt").read())
simulate(startPositions, 1000)
