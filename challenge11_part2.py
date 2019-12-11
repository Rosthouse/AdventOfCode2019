from utils import readIntCode, add
from robot import Robot
from colorama import Back, Style

code = readIntCode("./res/challenge11.txt")
robot = Robot(code)


panels = {}
position = (0, 0)

color = robot.calculatePanelColor(1)
panels[position] = color
position = add(position, robot.dir)

while not robot.isFinished():

    color = robot.calculatePanelColor(
        panels[position] if position in panels else 0)
    if color == -1:
        break

    panels[position] = color
    position = add(position, robot.dir)

print(f"Visited panels: {len(panels)}")


xMin = min([x[0] for x in list(panels.keys())])
yMin = min([x[1] for x in list(panels.keys())])

xMax = max([x[0] for x in list(panels.keys())])
yMax = max([x[1] for x in list(panels.keys())])

panel: [[str]] = []

for y in range(yMin, yMax + 1, 1):
    row = []
    for x in range(xMin, xMax + 1, 1):
        row.append("X")
    panel.append(row)

for p in panels:
    pos = (p[0] - xMin, p[1] - yMin)
    panel[pos[1]][pos[0]] = "#" if panels[p] else "."

print("\n".join(''.join(i for i in x) for x in panel))
