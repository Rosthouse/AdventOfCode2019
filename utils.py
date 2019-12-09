

def read_intcode(path: str) -> [int]:
    return list(map(lambda x: int(x), open(path).read().split(",")))
