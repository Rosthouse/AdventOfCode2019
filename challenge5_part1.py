# Advent of Code 2019: Day 2, Part 2
# https://adventofcode.com/2019/day/2


def run(code):

    params = {
        1: 4,
        2: 4,
        3: 2,
        4: 2
    }

    modes = {
        0: lambda x: code[x],
        1: lambda x: x,
    }

    function_pointer = 0

    while function_pointer < len(code):

        opcode = code[function_pointer:function_pointer+4]
        instruction = list(map(lambda x: int(x), str(opcode[0])))
        # TODO: Handle 99
        while len(instruction) < 2:
            instruction.insert(0, 0)

        op = int(str(instruction[-2]) + str(instruction[-1]))

        if(op == 99):
            break

        if op == 1:
            val1 = modes.get(instruction[1])(opcode[1])
            val2 = modes.get(instruction[0])(opcode[2])
            code[opcode[3]] = val1 + val2
        elif op == 2:
            val1 = modes.get(instruction[1])(opcode[1])
            val2 = modes.get(instruction[0])(opcode[2])
            code[opcode[3]] = val1 * val2
        elif op == 3:
            val1 = modes.get(0)(opcode[0])
            code[opcode[0]] = int(input("Input:"))
        elif op == 4:
            print(opcode[1])

        function_pointer += params.get(op)

    return code

# print(run([1002, 4, 3, 4, 33]))
# print(run([1101, 100, -1, 4, 0]))
# print(run([3,0,4,0,99]))

code = list(map(lambda x: int(x), open("./res/challenge5.txt").readline().split(",")))
result = run(code)
print("Test: " + str(result))
