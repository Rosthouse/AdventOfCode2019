# Advent of Code 2019: Day 11, Part 1
# https://adventofcode.com/2019/day/11

from utils import readIntCode, add
from robot import Robot

code = readIntCode("./res/challenge11.txt")
robot = Robot(code)


panels = {}
position = (0, 0)

while not robot.isFinished():

    color = robot.calculatePanelColor(
        panels[position] if position in panels else 0)
    if color == -1:
        break

    panels[position] = color
    position = add(position, robot.dir)

print(f"Visited panels: {len(panels)}")
