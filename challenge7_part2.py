
# Advent of Code 2019: Day 7, Part 2
# https://adventofcode.com/2019/day/7


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


def run_feedback_settings(settings: [int], code: [int], debug=False) -> int:
    out = 0
    current = 0
    processors: [Processor] = [Processor(code.copy()) for x in range(5)]

    for i in range(0, len(processors), 1):
        processors[i].input.append(settings[i])

    iterationCounter = 0
    while True:
        processors[current].input.append(out)
        while len(processors[current].out) == 0 and not processors[current].hasFinished:
            processors[current].step(debug)

        if processors[current].hasFinished:
            break
        out = processors[current].getOutput().pop()
        # print("Amp " + str(current) + ": " + str(out))
        if current < 4:
            current += 1
        else:
            iterationCounter += 1
            current = 0
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


def find_max_thrust_feedback_loop(code: [int]) -> int:
    thrust = (-1, -1)
    for i in itertools.permutations([5, 6, 7, 8, 9], 5):
        # settings = list(map(lambda x: int(x), str(i).zfill(5)))
        currentThrust = run_feedback_settings(i, code)
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


print("Expected 139629729: " + str(run_feedback_settings([9, 8, 7, 6, 5], [
      3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5])))

print("Expected 18216: " + str(run_feedback_settings([9, 7, 8, 5, 6], [
      3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
      -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
      53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10])))

code = list(map(lambda x: int(x), open(
    "./res/challenge7.txt").read().split(",")))
print("Max thrust: ", find_max_thrust_feedback_loop(code))
# run_settings([0, 3, 3, 3, 3], [Processor(code.copy()) for x in range(5)])
