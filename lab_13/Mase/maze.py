# Implements the Maze ADT using a 2-D array.
from arrays import Array2D
from lliststack import Stack


class Maze:
    # Define constants to represent contents of the maze cells.
    MAZE_WALL = " *"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    # Creates a maze object with all cells marked as open.
    def __init__(self, num_rows, num_cols):
        self.mazeCells = Array2D(num_rows, num_cols)
        self.startCell = None
        self.exitCell = None
        self.exit = None

    # Returns the number of rows in the maze.
    def num_rows(self):
        return self.mazeCells.num_rows()

    # Returns the number of columns in the maze.
    def num_cols(self):
        return self.mazeCells.num_cols()

    # Fills the indicated cell with a "wall" marker.
    def set_wall(self, row, col):
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self.mazeCells[row, col] = self.MAZE_WALL

    # Sets the starting cell position.
    def set_start(self, row, col):
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self.startCell = CellPosition(row, col)

    # Sets the exit cell position.
    def set_exit(self, row, col):
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self.exitCell = CellPosition(row, col)

    def find_path(self):
        stack = Stack()
        current = self.startCell
        current.path.append(current)
        current.parent = current

        if current == self.exitCell:
            return True
        home_cords_nei = self.check_neighbors(current.row, current.col)
        for cell in home_cords_nei:
            if cell == self.exitCell:
                return True
            cell.path.append(current)
            stack.push(cell)
        self.mark_tried(current.row, current.col)

        while not stack.isEmpty():
            parent = current
            current = stack.peek()
            current.parent = parent
            current.path += parent.path
            current.path.append(current)

            self.mark_tried(current.row, current.col)
            if self.exit_found(current.row, current.col):
                self.exit = current
                return True
            stack.pop()
            for cell in self.check_neighbors(current.row, current.col):
                stack.push(cell)
        return False

    def print_way(self):
        for cord in self.exit.path:
            self.mazeCells[cord.row, cord.col] = self.PATH_TOKEN
        return self


    def __str__(self):
        string = ""
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                if self.mazeCells[i, j] is not None:
                    string += self.mazeCells[i, j].replace(" ", "")
                else:
                    string += " "
            string += "\n"
        return string

    def check_neighbors(self, row, col):
        lst = []
        for cor in [(1, 0), (0, 1), (-1, 0), (0, -1), ]:
            if self.valid_move(row + cor[0], col + cor[1]):
                lst.append(CellPosition(row + cor[0], col + cor[1]))
        return lst

    # Resets the maze by removing all "path" and "tried" tokens.
    def reset(self):
        for r in range(self.num_rows()):
            for c in range(self.num_cols()):
                if self.mazeCells[r, c] == self.TRIED_TOKEN or self.mazeCells[r, c] == self.PATH_TOKEN:
                    self.mazeCells[r, c] = None
        return str(self)

    # Prints a text-based representation of the maze.
    def draw(self):
        print(self)
        return str(self)

    # Returns True if the given cell position is a valid move.
    def valid_move(self, row, col):
        return 0 <= row < self.num_rows() \
               and 0 <= col < self.num_cols() \
               and self.mazeCells[row, col] is None

    # Helper method to determine if the exit was found.
    def exit_found(self, row, col):
        return row == self.exitCell.row and col == self.exitCell.col

    # Drops a "tried" token at the given cell.
    def mark_tried(self, row, col):
        self.mazeCells[row, col] = self.TRIED_TOKEN

    # Drops a "path" token at the given cell.
    def mark_path(self, row, col):
        self.mazeCells[row, col] = self.PATH_TOKEN


# Private storage class for holding a cell position.
class CellPosition:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.path = []
        self.parent = None
