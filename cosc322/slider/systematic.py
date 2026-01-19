from types import prepare_class
from sliderbox import sliderbox


class Astar:
    def __init__(self, size: int, spaces: int) -> None:
        self.game = sliderbox(size, spaces)
        self.nodeList: list[Node] = []

    def checkChildren(self):
        # get current state
        for optionsself.game
        self.nodeList
        x = self.game.getState()
        # generate states


class Node:
    def __init__(self, state, parent=None) -> None:
        self.state = state
        self.g_cost = 0
        self.h_cost = 0
        self.f_cost = 0
        self.parent = parent

    def setGCost(self, cost):
        self.g_cost = cost

    def setHCost(self, cost):
        self.h_cost = cost

    def setFCost(self, cost):
        self.f_cost = cost
