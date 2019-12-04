# Advent of Code 2019: Day 4, Part 1
# https://adventofcode.com/2019/day/4

def verify_pw(pw: int) -> bool:
    elements: [int] = list(map(lambda digit: int(digit), str(pw)))

    double: bool = False
    ascending: bool = True
    for i in range(0, len(elements)-1, 1):
        if elements[i] == elements[i+1]:
            double = True
        if elements[i] > elements[i+1]:
            ascending = False

    return double and ascending

def count_valid_pws(start: int, end: int) -> int:
    counter: int = 0
    for i in range(start, end, 1):
        if verify_pw(i):
            counter += 1
    return counter


print("111111: [true|" + str(verify_pw(111111)) + "]")
print("111111: [false|" + str(verify_pw(223450)) + "]")
print("111111: [false|" + str(verify_pw(123789)) + "]")

print("Valid pws: " + str(count_valid_pws(240920, 789857)))