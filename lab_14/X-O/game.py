import sys
import os
from random import choice
from copy import deepcopy
sys.path.append(os.path.join(os.path.dirname(__file__), '../',  'Trees_easy-master', 'Trees_easy-master'))
from linked_binary_tree import LinkedBinaryTree


class Board:
    _O_POINT = "O"
    _X_POINT = "X"
    _TIE = "TIE"

    def __init__(self):
        self.field = [[None for _ in range(3)] for _ in range(3)]
        self.last_turn = [None, None, None]  # [row, col, 'O' or 'X']

    def __str__(self):
        stryng = ""
        for row in range(3):
            for col in range(3):
                if self.field[row][col] is not None:
                    stryng += self.field[row][col]
                else:
                    stryng += " "
            stryng += '\n'
        return stryng

    def empty_coords(self):
        empty_cells = set()
        for row in range(3):
            for col in range(3):
                if self.field[row][col] is None:
                    empty_cells.add((row, col))
        return empty_cells

    def points_coords(self):
        """
        find out the coordinates of points
        :return: tuple(list)
        """
        x_coords = set()
        o_coords = set()
        for row in range(3):
            for col in range(3):
                if self.field[row][col] == self._O_POINT:
                    o_coords.add((row, col))
                elif self.field[row][col] == self._X_POINT:
                    x_coords.add((row, col))
        return x_coords, o_coords

    def someone_wins(self):
        """
        analyse field to find out the winner or return None otherwise
        :return: str or None
        """
        x_coords = self.points_coords()[0]
        o_coords = self.points_coords()[1]

        if len(x_coords) + len(o_coords) == 9:
            return self._TIE

        if self.analyse(x_coords):
            return self._X_POINT
        if self.analyse(o_coords):
            return self._O_POINT
        return None

    @staticmethod
    def analyse(li):
        winning_positions = ([(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                             [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                             [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)])
        for position in winning_positions:
            if set(position).issubset(set(li)):
                return True
        return False

    def turn(self, mark, coords):
        """
        make a turn
        :param mark: "X" or "O"
        :param coords: tuple(int)
        :return:
        """
        self.field[coords[0]][coords[1]] = mark.upper()

board = Board()


def build_tree(b):
    if b.someone_wins() == "TIE" or b.someone_wins() == "O" or b.someone_wins() == "X":
        return

    tree = LinkedBinaryTree(b)
    free_cells = b.empty_coords()
    random_cell1 = choice(list(free_cells))
    choice1 = deepcopy(b)
    choice1.turn("O", random_cell1)
    tree.left_child = LinkedBinaryTree(choice1)
    build_tree(choice1)

    free_cells.discard(random_cell1)
    if free_cells != set():  # we have to check if set isn't empty
        random_cell2 = choice(list(free_cells))
        choice2 = deepcopy(b)
        choice2.turn("O", random_cell2)
        tree.right_child = LinkedBinaryTree(choice2)
        build_tree(choice2)

while True:
    print("type x and y coordinates with space *1 2* or *0 0*: ")
    x, y = [int(_) for _ in input().split()]
    board.turn("X", (x, y))
    print(board, "\n--------------------")

    build_tree(board)

    if board.someone_wins() == "TIE":
        print("it is a tie")
        break

    elif board.someone_wins() == "O":
        print("you lost")
        break
    elif board.someone_wins() == "X":
        print("you win")
        break

    free_cells = board.empty_coords()
    random_cell = choice(list(free_cells))

    board.turn("O", random_cell)
    print(board)

    if board.someone_wins() == "TIE":
        print("it is a tie")
        break

    elif board.someone_wins() == "O":
        print("you lost")
        break
    elif board.someone_wins() == "X":
        print("you win")
        break
