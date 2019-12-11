# Advent of Code 2019: Day 9, Part 2
# https://adventofcode.com/2019/day/9

from processor import Processor
from utils import readIntCode

code = readIntCode("./res/challenge9.txt")
proc = Processor(code)
proc.setInput([2])
proc.run()
print(f"Output: {proc.getOutput()}")
