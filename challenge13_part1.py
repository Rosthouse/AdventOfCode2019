# Advent of Code 2019: Day 13, Part 1
# https://adventofcode.com/2019/day/13

from processor import Processor
import utils


class Game:
    def __init__(self, code: [int]):
        self.processor = Processor(code)
        self.tiles = {
            0: ' ',
            1: '#',
            2: '@',
            3: 'P',
            4: 'B'
        }
        self.screen: dict = {}

    def update(self) -> bool:

        while len(self.processor.getOutput()) < 3:
            if self.processor.hasFinished:
                return True
            self.processor.step()

        (x, y, i) = self.processor.getOutput()
        self.screen[(x, y)] = i
        self.processor.getOutput().clear()
        return False

    def draw(self) -> None:
        return

    def gameLoop(self) -> None:
        while not self.update():
            self.draw()


game = Game(utils.readIntCode("./res/challenge13.txt"))

game.gameLoop()
blocks = len([i for i in game.screen.values() if i == 2])
print(f"Found {blocks} blocks")
