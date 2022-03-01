from xml.etree import ElementInclude
from sqlalchemy import true

from tables import Cols
from Cell import Cell


class Map:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._cells = [[Cell() for x in range(cols)] for y in range(rows)]

    # rows getter
    def get_rows(self){
        return self._rows
    }

    # cols getter
    def get_cols(self){
        return self._cols
    }

    def get_cell(self, row, col):
        if (row < 0 or row >= self._rows or col < 0 or col >= self._cols):  # condition
            print("\033[1;31;46mNext move is out of boundary!\033[0;0m")
            return None
        else:
            # return a cell
            return self._cells[row][col]
            # END

    # TODO: !!!need to determine whether return a bool or return a cell
    def build_cell(self, row, col, cell):
        #
        if (row < 0 or row >= self._rows or col < 0 or col >= self._cols):  # condition
            print(
                "\033[1;31;46mThe position (%d, %d) is out of boundary!\033[0;0m" % (row, col))
            return false
        else:
            self._cells[row][col] = cell
            return True
            # END

    def get_neighbours(self, row, col):
        return_cells = []

        for i in range(max(0, row-1), min(row+1, self._rows-1)+1):
            for j in range(max(0, col-1), min(col+1, self.cols-1)+1):
                return_cells.append(self._cells[i][j])

        return return_cells

    def display(self):
        for i in range(0, self.cols):
            print("%d     ", i)
        print("%n")
        for i in range(0, self.rows):
            print("%d ", i)
            for j in range(0, self.cols):
                self._cells[i][j].display()
            print("%n%n")
