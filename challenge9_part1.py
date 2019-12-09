from processor import Processor
from utils import read_intcode
# add relative mode

# Add opcode 9

# Add huge memory

proc = Processor([109, 1, 204, -1, 1001, 100, 1, 100,
                  1008, 100, 16, 101, 1006, 101, 0, 99])

# proc.run(True)
# print(f"Output: {proc.getOutput()}")

# proc = Processor([1102, 34915192, 34915192, 7, 4, 7, 99, 0])
# proc.run(True)
# print(f"Output: {proc.getOutput()}")

# proc = Processor([104, 1125899906842624, 99])
# proc.run(True)
# print(f"Output: {proc.getOutput()}")

proc = Processor([9, 10, 203, 1, 4, 11, 99])
proc.setInput([25])
proc.run(True)
print(f"Output: {proc.getOutput()}, Memory: {proc.memory}")

code = read_intcode("./res/challenge9.txt")
proc = Processor(code)
proc.setInput([1])
while not proc.hasFinished:
    proc.step(True)
print(f"Output: {proc.getOutput()}")
