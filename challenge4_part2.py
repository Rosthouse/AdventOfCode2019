

def verify_pw(pw: int) -> bool:
    # pwString =
    # a = [x for x in pwString]
    elements: [int] = list(map(lambda digit: int(digit), str(pw)))

    double: bool = False
    ascending: bool = True
    overarch_flag = True

    count = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }
    for i in range(0, len(elements)-1, 1):
        c = elements[i]
        r = elements[i+1]

        if c > r:
            ascending = False

        if c == r:
            count[c] = count[c] + 1

    if 1 in count.values():
        double = True

    return ascending and double


def count_valid_pws(start: int, end: int) -> int:
    counter: int = 0
    for i in range(start, end, 1):
        if verify_pw(i):
            counter += 1
    return counter


print("111111: [false|" + str(verify_pw(111111)) + "]")
print("223450: [false|" + str(verify_pw(223450)) + "]")
print("123789: [false|" + str(verify_pw(123789)) + "]")
print("112233: [true|" + str(verify_pw(112233)) + "]")
print("123444: [false|" + str(verify_pw(123444)) + "]")
print("111122: [true|" + str(verify_pw(111122)) + "]")
print("112222: [true|" + str(verify_pw(112222)) + "]")
print("122234: [false|" + str(verify_pw(122234)) + "]")

print("Valid pws: " + str(count_valid_pws(240920, 789857)))
