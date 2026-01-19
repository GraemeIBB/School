import random
import time


class sliderbox:
    def __init__(self, size: int, spaces: int):
        self.size = size
        self.spaces = spaces
        self.state = []
        self.endState = []
        counter = 1

        for y in range(size):
            self.state.append([])
            for x in range(size):
                position = y * size + x
                if position < spaces:
                    self.state[y].append(-1)
                else:
                    self.state[y].append(counter)
            counter += 1

        self.endState = self.state

    def getState(self) -> list[list]:
        return self.state

    def getEndState(self) -> list[list]:
        return self.endState

    def showState(self):
        barrier = ""
        for item in self.state[0]:
            barrier += "---"
        print(barrier)
        for row in self.state:
            print(row)
        print(barrier)

    def _updateState(self, newState):
        self.state = newState

    def _availableMoves(self) -> list[tuple]:
        moves: list[tuple] = []
        # look at table, if direction is available, append to moves

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        for y in range(self.size):
            for x in range(self.size):
                if self.state[y][x] == -1:
                    for dy, dx in directions:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < self.size and 0 <= nx < self.size:
                            if self.state[ny][nx] != -1:
                                moves.append((ny, nx, y, x))

        return moves

    def slide(self, dir: tuple):  # tile_y, tile_x, space_y, space_x
        if dir in self._availableMoves():
            self.state[dir[2]][dir[3]] = self.state[dir[0]][dir[1]]
            self.state[dir[0]][dir[1]] = -1
        else:
            raise Exception("Attempted to make an illegal move")

    def slideBasic(self, dir: str):  # "up", "down", "left", "right"
        dir = dir.strip().lower()
        queue = []
        if dir == "up":
            for move in self._availableMoves():
                if (move[0] - 1) == move[2]:
                    queue.append(move)
        elif dir == "down":
            for move in self._availableMoves():
                if (move[0] + 1) == move[2]:
                    queue.append(move)
        elif dir == "left":
            for move in self._availableMoves():
                if (move[1] - 1) == move[3]:
                    queue.append(move)
        elif dir == "right":
            for move in self._availableMoves():
                if (move[1] + 1) == move[3]:
                    queue.append(move)
        else:
            raise Exception("Unknown direction")

        for move in queue:
            self.slide(move)

    def validSlides(self):
        validDirs = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
        }
        for move in self._availableMoves():
            if (move[0] - 1) == move[2]:
                validDirs["up"] = True
            elif (move[0] + 1) == move[2]:
                validDirs["down"] = True
            elif (move[1] - 1) == move[3]:
                validDirs["left"] = True
            elif (move[1] + 1) == move[3]:
                validDirs["right"] = True
        return validDirs

    def mix(self):
        random.seed(int(time.time() * 100))
        # place in list, mix list, re throw in table
        mixer = []
        for y in range(self.size):
            for x in range(self.size):
                mixer.append(self.state[y][x])
        random.shuffle(mixer)
        count = 0
        for y in range(self.size):
            for x in range(self.size):
                self.state[y][x] = mixer[count]
                count += 1


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("size")
    parser.add_argument("spaces")
    args = parser.parse_args()

    x = sliderbox(int(args.size), int(args.spaces))
    x.mix()
    while True:
        x.showState()
        dir = input("Enter Direction: ")
        x.slideBasic(dir)
