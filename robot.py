

from processor import Processor
from utils import readIntCode, add
import math


class Robot:

    def __init__(self, code: [int]):
        self.processor: Processor = Processor(code)
        self.dir = (0, -1)
        self.paintedPanels: [(int, int)] = []

    def isFinished(self) -> bool:
        return self.processor.hasFinished

    def rotate(self, rotation) -> None:
        # 1 -> cw, 0 -> ccw
        if rotation:
            # cw
            self.dir = (-self.dir[0], -self.dir[1])
        self.dir = (self.dir[1], -self.dir[0])

    def calculatePanelColor(self, panel: int) -> int:
        self.processor.setInput([panel])
        while len(self.processor.getOutput()) < 2:
            self.processor.step()
            if self.processor.hasFinished:
                return -1
        self.rotate(self.processor.getOutput().pop())
        return self.processor.getOutput().pop()


