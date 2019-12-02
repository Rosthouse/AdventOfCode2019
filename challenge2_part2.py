def run(code):
    switcher = {
        1: lambda x, y: code[x] + code[y],
        2: lambda x, y: code[x] * code[y],
    }

    for i in range(0, len(code), 4):
        opcode = code[i]
        if(opcode == 99):
            break

        mem1 = code[i+1]
        mem2 = code[i+2]
        memS = code[i+3]

        func = switcher.get(opcode)
        code[memS] = func(mem1, mem2)
    return code


def test_code(code):
    for i in range(0, 100, 1):
        for j in range(0, 100, 1):
            codeCpy = code.copy()
            codeCpy[1] = i
            codeCpy[2] = j
            result = run(codeCpy)

            if(result[0] == 19690720):
                print("Result: " + str(i) + str(j) )
                return


print(run([1, 0, 0, 0, 99]))
print(run([2, 3, 0, 3, 99]))
print(run([2, 4, 4, 5, 99, 0]))
print(run([1, 1, 1, 4, 99, 5, 6, 0, 99]))

code = list(map(lambda x: int(x), open(
    "./res/challenge2.txt").readline().split(",")))

test_code(code)
