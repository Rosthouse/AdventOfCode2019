import math


def readIntCode(path: str) -> [int]:
    return list(map(lambda x: int(x), open(path).read().split(",")))


def length(vec: (int, int)) -> float:
    return math.sqrt(math.pow(vec[0], 2) + math.pow(vec[1], 2))


def sign(x):
    if x > 0:
        return 1.
    elif x < 0:
        return -1.
    elif x == 0:
        return 0.
    else:
        return x


def add(a, b):
    arr = []
    for x in range(0, len(a), 1):
        arr.append(a[x] + b[x])
    return tuple(arr)


def subtract(a, b):
    arr = []
    for x in range(0, len(a), 1):
        arr.append(a[x] - b[x])
    return tuple(arr)


def normalize(vec: (int, int)) -> (int, int):
    magn = length(vec)
    return (vec[0] / magn, vec[1] / magn)


def absVec(a: ()) -> ():
    return tuple([abs(x) for x in a])
