# Advent of Code 2019: Day 2, Part 2
# https://adventofcode.com/2019/day/2


def run(code):

    params = {
        1: 4,
        2: 4,
        3: 2,
        4: 2,
        99: 1
    }

    modes = {
        0: lambda x: code[x],
        1: lambda x: x,
    }

    function_pointer = 0

    while function_pointer < len(code):

        instruction = list(map(lambda x: int(x), str(code[function_pointer])))

        # TODO: Handle 99
        while len(instruction) < 5:
            instruction.insert(0, 0)

        op = int(str(instruction[-2]) + str(instruction[-1]))
        opcode = code[function_pointer:function_pointer +
                      params.get(op)]

        print("Instruction: " + str(opcode))

        if(op == 99):
            break

        if op == 1:
            val1 = modes.get(instruction[2])(opcode[1])
            val2 = modes.get(instruction[1])(opcode[2])
            code[opcode[3]] = val1 + val2
        elif op == 2:
            val1 = modes.get(instruction[2])(opcode[1])
            val2 = modes.get(instruction[1])(opcode[2])
            code[opcode[3]] = val1 * val2
        elif op == 3:
            code[opcode[1]] = int(input("Input:"))
        elif op == 4:
            print("Out: " + str(code[opcode[1]]))

        function_pointer += params.get(op)

    return code


# print(run([1002, 4, 3, 4, 33]))
# print(run([1101, 100, -1, 4, 0]))
# print(run([3, 0, 4, 0, 99]))
# print(run([1101, 37, 61, 3, 99]))
# print("Expected: 135")
# run([101, 34, 0, 3, 4, 3, 99])


code = list(map(lambda x: int(x), open(
    "./res/challenge5.txt").readline().split(",")))
result = run(code)
