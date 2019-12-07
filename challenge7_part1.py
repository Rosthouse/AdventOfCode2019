
# Advent of Code 2019: Day 5, Part 2
# https://adventofcode.com/2019/day/5


from processor import Processor
import itertools


def run_settings(settings: [int], code: [int]) -> int:
    out = 0
    current = 0
    processors: [Processor] = [Processor(code.copy()) for x in range(5)]
    while current < 5:
        processors[current].setInput([settings[current], out])
        while len(processors[current].out) == 0:
            processors[current].step()
        out = processors[current].getOutput().pop()
        # print("Amp " + str(current) + ": " + str(out))
        current += 1
    return out


def find_max_thrust(code: [int]) -> int:
    thrust = (-1, -1)
    for i in itertools.permutations([0, 1, 2, 3, 4], 5):
        # settings = list(map(lambda x: int(x), str(i).zfill(5)))
        currentThrust = run_settings(i, code)
        if currentThrust > thrust[0]:
            thrust = (currentThrust, i)
            print("Found bigger:  " + str(thrust))
    return thrust


# print("Expected 43210: " +
#       str(find_max_thrust([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0])))
# print("Expected 43210: " + str(find_max_thrust([3, 23, 3, 24, 1002, 24, 10,
#                                                 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0])))
# print("Expected 43210: " + str(find_max_thrust([3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2,
    # 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0])))

# run_settings([4, 3, 2, 1, 0], [3, 15, 3, 16, 1002, 16,
#                                10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0])
# run_settings([0, 1, 2, 3, 4], [3, 23, 3, 24, 1002, 24, 10, 24, 1002,
#                                23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0])
# run_settings([1, 0, 4, 3, 2], [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33,
#                                1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0])


code = list(map(lambda x: int(x), open(
    "./res/challenge7.txt").read().split(",")))
print("Max: " + str(find_max_thrust(code)))

# run_settings([0, 3, 3, 3, 3], [Processor(code.copy()) for x in range(5)])
