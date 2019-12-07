
# Advent of Code 2019: Day 5, Part 2
# https://adventofcode.com/2019/day/5


class Processor:

    def __init__(self, code: [int]):
        self.params = {
            1: 4,
            2: 4,
            3: 2,
            4: 2,
            5: 3,
            6: 3,
            7: 4,
            8: 4,
            99: 1
        }

        self.modes = {
            0: lambda x: code[x],   # Position mode
            1: lambda x: x,         # Immediate mode
        }
        self.function_pointer = 0
        self.code: [int] = code
        self.out: [int] = []
        self.hasFinished: bool = False

    def setInput(self, inp: [int]) -> None:
        self.input = inp

    def getOutput(self) -> [int]:
        return self.out

    def finished(self) -> bool:
        return self.hasFinished

    def step(self: Processor, debug: bool = False):
        instruction = list(
            map(lambda x: int(x), str(code[self.function_pointer])))

        while len(instruction) < 5:
            instruction.insert(0, 0)

        op = int(str(instruction[-2]) + str(instruction[-1]))
        opcode = code[function_pointer:function_pointer +
                      self.params.get(op)]

        if debug:
            print("FP: " + str(function_pointer) +
                  ", Instruction: " + str(opcode))

        if(op == 99):
            self.hasFinished = True
            return

        if op == 1:  # add
            val1 = self.modes.get(instruction[2])(opcode[1])
            val2 = self.modes.get(instruction[1])(opcode[2])
            code[opcode[3]] = val1 + val2
        elif op == 2:  # multiply
            val1 = self.modes.get(instruction[2])(opcode[1])
            val2 = self.modes.get(instruction[1])(opcode[2])
            code[opcode[3]] = val1 * val2
        elif op == 3:  # input
            code[opcode[1]] = input_callback()
        elif op == 4:  # output
            self.out.append(code[opcode[1]])
            # print("Out: " + str(code[opcode[1]]))
        elif op == 5:  # jump-if-true
            val1 = self.modes.get(instruction[2])(opcode[1])
            val2 = self.modes.get(instruction[1])(opcode[2])
            if(val1 != 0):
                function_pointer = val2
                continue
        elif op == 6:  # jump-if-false
            val1 = self.modes.get(instruction[2])(opcode[1])
            val2 = self.modes.get(instruction[1])(opcode[2])
            if(val1 == 0):
                function_pointer = val2
                continue
        elif op == 7:  # less than
            val1 = self.modes.get(instruction[2])(opcode[1])
            val2 = self.modes.get(instruction[1])(opcode[2])
            if(val1 < val2):
                code[opcode[3]] = 1
            else:
                code[opcode[3]] = 0
        elif op == 8:  # equals
            val1 = self.modes.get(instruction[2])(opcode[1])
            val2 = self.modes.get(instruction[1])(opcode[2])
            if(val1 == val2):
                code[opcode[3]] = 1
            else:
                code[opcode[3]] = 0

        function_pointer += self.params.get(op)

    def run(self, debug=False,):
        while not self.hasFinished:
            self.step(debug)


def run_settings(settings: [int], processors: [Processor]) -> int:
    out = 0
    curr = 0)
    while not processors[4].hasFinished:
        inputList
        [settings[curr], out]
        while len(processors[curr].out) == 0:
            processors[curr].step(False)

    for i in range(0, 5, 1):
        out = run(code.copy(), lambda: inputList.pop(0), True)[0]
        print("Settings: " + str(settings) +
              ", Amp: " + str(i) + ", Out: " + str(out))

    return out


# print("Expected 43210: " + str(run_settings(
#     [4, 3, 2, 1, 0],
#     [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0])))
# print("Expected 54321: " + str(run_settings(
#     [0, 1, 2, 3, 4],
#     [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0])))
# print("Expected 65210: " + str(run_settings(
#     [1, 0, 4, 3, 2],
#     [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0])))

def find_max_thrust(code: [int]) -> int:
    thrust = 0
    for i in range(0, 100000):
        settings = list(map(lambda x: int(x), str(i).zfill(5)))
        processors: [Processor] = [Processor(code.copy()) for x in range(5)]
        currentThrust = run_settings(settings, processors)
        thrust = currentThrust if currentThrust > thrust else thrust
    return thrust


code = list(map(lambda x: int(x), open(
    "./res/challenge7.txt").read().split(",")))

run_settings([0, 0, 0, 0, 5], code)
# print("Max: " + str(find_max_thrust(code)))
