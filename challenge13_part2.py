from processor import Processor
import utils
import os
import time
import curses


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
        self.segmentDisp: int = 0
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.nodelay(True)
        self.running = False

    def update(self) -> bool:

        while not self.processor.requiresInput:
            if self.processor.hasFinished:
                self.running = False
                break
            self.processor.step()

        for p in range(0, len(self.processor.getOutput()), 3):
            (x, y, i) = self.processor.getOutput()[p:p+3]
            if (x, y) == (-1, 0):
                self.segmentDisp = i
            else:
                self.screen[(x, y)] = i

        self.processor.getOutput().clear()
        return False

    def draw(self) -> None:
        xMax = max([x for (x, _) in self.screen.keys()])
        yMax = max([y for (_, y) in self.screen.keys()])

        for y in range(yMax + 1):
            for x in range(xMax + 1):
                tid = self.screen.get((x, y), 0)
                tile = self.tiles.get(tid)
                self.stdscr.addstr(y, x, tile)
        self.stdscr.refresh()

    def clear(self) -> None:
        self.stdscr.clear()

    def getInput(self) -> int:
        items = self.screen.items()
        ball = next(p for p, z in items if z == 4)
        paddle = next(p for p, z in items if z == 3)

        if ball and paddle:
            return utils.sign(utils.subtract(ball, paddle)[0])
        else:
            return 0
        # direction = 0
        # c = self.stdscr.getch()

        # if c == curses.KEY_LEFT:
        #     direction -= 1
        # if c == curses.KEY_RIGHT:
        #     direction += 1
        # if c == curses.KEY_ABORT:
        #     self.running = False
        # return direction

    def gameLoop(self, quarters: int) -> None:
        self.processor.memory[0] = quarters
        self.running = True

        while not self.update() and self.running:
            inp = self.getInput()
            self.processor.setInput([self.getInput()])
            self.clear()
            self.draw()

        curses.nocbreak()   # Turn off cbreak mode
        curses.echo()       # Turn echo back on
        curses.curs_set(1)  # Turn cursor back on
        # If initialized like `my_screen = curses.initscr()`
        self.stdscr.keypad(0)  # Turn off keypad keys
        curses.endwin()


game = Game(utils.readIntCode("./res/challenge13.txt"))

game.gameLoop(2)
blocks = len([i for i in game.screen.values() if i == 2])
print(f"Final score: {game.segmentDisp}")
