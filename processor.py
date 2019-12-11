# Processor for the IntCode, used in several challenges


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
            9: 2,
            99: 1
        }

        self.readModes = {
            # Position mode
            0: lambda x: self.get_address(x),
            # Immediate mode
            1: lambda x: x,
            # Relative mode
            2: lambda x: self.get_address(self.relative_address + x)
        }

        self.writeModes = {
            # position mode
            0: lambda pos, val: self.set_address(pos, val),
            # relative mode
            2: lambda pos, val: self.set_address(self.relative_address + pos, val)
        }
        self.function_pointer = 0
        self.relative_address = 0
        self.memory: [int] = code
        self.out: [int] = []
        self.hasFinished: bool = False
        self.input: [int] = []

    def setInput(self, inp: [int]) -> None:
        self.input = inp

    def getOutput(self) -> [int]:
        return self.out

    def finished(self) -> bool:
        return self.hasFinished

    def step(self, debug: bool = False):
        instruction = list(
            map(lambda x: int(x), str(self.memory[self.function_pointer])))

        while len(instruction) < 5:
            instruction.insert(0, 0)

        op = int(str(instruction[-2]) + str(instruction[-1]))
        opcode = self.memory[self.function_pointer:self.function_pointer +
                             self.params.get(op)]

        if debug:
            print(
                f"OP: {opcode}, FP: {self.function_pointer}, RP: {self.relative_address}")

        if op == 1:  # add
            val1 = self.get_value(instruction[2], opcode[1])
            val2 = self.get_value(instruction[1], opcode[2])
            self.set_value(instruction[0], opcode[3],  val1 + val2)
        elif op == 2:  # multiply
            val1 = self.get_value(instruction[2], opcode[1])
            val2 = self.get_value(instruction[1], opcode[2])
            self.set_value(instruction[0], opcode[3], val1 * val2)
        elif op == 3:  # input
            self.set_value(instruction[2], opcode[1], self.input.pop(0))
        elif op == 4:  # output
            self.out.append(self.get_value(instruction[2], opcode[1]))
        elif op == 5:  # jump-if-true
            val1 = self.get_value(instruction[2], opcode[1])
            val2 = self.get_value(instruction[1], opcode[2])
            if(val1 != 0):
                self.function_pointer = val2
                return
        elif op == 6:  # jump-if-false
            val1 = self.get_value(instruction[2], opcode[1])
            val2 = self.get_value(instruction[1], opcode[2])
            if(val1 == 0):
                self.function_pointer = val2
                return
        elif op == 7:  # less than
            val1 = self.get_value(instruction[2], opcode[1])
            val2 = self.get_value(instruction[1], opcode[2])
            if(val1 < val2):
                self.set_value(instruction[0], opcode[3], 1)
            else:
                self.set_value(instruction[0], opcode[3], 0)
        elif op == 8:  # equals
            val1 = self.get_value(instruction[2], opcode[1])
            val2 = self.get_value(instruction[1], opcode[2])
            if(val1 == val2):
                self.set_value(instruction[0], opcode[3], 1)
            else:
                self.set_value(instruction[0], opcode[3], 0)
        elif op == 9:  # adjust relative position
            self.relative_address += self.get_value(instruction[2],  opcode[1])
        elif op == 99:
            self.hasFinished = True
            print("Halted")
            return

        self.function_pointer += self.params.get(op)

    def get_value(self, mode: int, position: int) -> int:
        return self.readModes.get(mode)(position)

    def set_value(self, mode: int, position: int, value: int) -> None:
        self.writeModes.get(mode)(position, value)

    def get_address(self, address: int) -> int:
        self.fit_memory_size(address)
        return self.memory[address]

    def set_address(self, address: int, value: int) -> None:
        self.fit_memory_size(address)
        self.memory[address] = value

    def fit_memory_size(self, address: int):
        while address >= len(self.memory):
            self.memory.extend([0 for x in range(0, len(self.memory))])

    def run(self, debug=False):
        while not self.hasFinished:
            self.step(debug)
