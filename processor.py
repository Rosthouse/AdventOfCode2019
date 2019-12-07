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
        self.input: [int] = []

    def setInput(self, inp) -> None:
        self.input = inp

    def getOutput(self) -> [int]:
        return self.out

    def finished(self) -> bool:
        return self.hasFinished

    def step(self, debug: bool = False):
        instruction = list(
            map(lambda x: int(x), str(self.code[self.function_pointer])))

        while len(instruction) < 5:
            instruction.insert(0, 0)

        op = int(str(instruction[-2]) + str(instruction[-1]))
        opcode = self.code[self.function_pointer:self.function_pointer +
                           self.params.get(op)]

        if debug:
            print("FP: " + str(self.function_pointer) +
                  ", Instruction: " + str(opcode))

        if op == 1:  # add
            val1 = self.modes.get(instruction[2])(opcode[1])
            val2 = self.modes.get(instruction[1])(opcode[2])
            self.code[opcode[3]] = val1 + val2
        elif op == 2:  # multiply
            val1 = self.modes.get(instruction[2])(opcode[1])
            val2 = self.modes.get(instruction[1])(opcode[2])
            self.code[opcode[3]] = val1 * val2
        elif op == 3:  # input
            self.code[opcode[1]] = self.input.pop(0)
        elif op == 4:  # output
            self.out.append(self.code[opcode[1]])
            # print("Out: " + str(self.code[opcode[1]]))
        elif op == 5:  # jump-if-true
            val1 = self.modes.get(instruction[2])(opcode[1])
            val2 = self.modes.get(instruction[1])(opcode[2])
            if(val1 != 0):
                self.function_pointer = val2
                return
        elif op == 6:  # jump-if-false
            val1 = self.modes.get(instruction[2])(opcode[1])
            val2 = self.modes.get(instruction[1])(opcode[2])
            if(val1 == 0):
                self.function_pointer = val2
                return
        elif op == 7:  # less than
            val1 = self.modes.get(instruction[2])(opcode[1])
            val2 = self.modes.get(instruction[1])(opcode[2])
            if(val1 < val2):
                self.code[opcode[3]] = 1
            else:
                self.code[opcode[3]] = 0
        elif op == 8:  # equals
            val1 = self.modes.get(instruction[2])(opcode[1])
            val2 = self.modes.get(instruction[1])(opcode[2])
            if(val1 == val2):
                self.code[opcode[3]] = 1
            else:
                self.code[opcode[3]] = 0
        elif op == 99:
            self.hasFinished = True
            print("Halted")
            return

        self.function_pointer += self.params.get(op)

    def run(self, debug=False):
        while not self.hasFinished:
            self.step(debug)
