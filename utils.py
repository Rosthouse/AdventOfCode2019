import math


def read_intcode(path: str) -> [int]:
    return list(map(lambda x: int(x), open(path).read().split(",")))


def length(vec: (int, int)) -> float:
    return math.sqrt(math.pow(vec[0], 2) + math.pow(vec[1], 2))


def normalize(vec: (int, int)) -> (int, int):
    magn = length(vec)
    return (vec[0] / magn, vec[1] / magn)
