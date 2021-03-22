import random as rand
from typing import List

from game.field.field_exceptions import *


class Field:
    def __init__(self, size):
        self.size = size
        self.__field__: List[List[int]] = [[None] * self.size for _ in range(self.size)]
        self.__create_random_value__(3)

    def cell_value(self, col, row):
        return self.__field__[col][row]

    def set_cell_value(self, col, row, value):
        self.__field__[col][row] = value

    @property
    def field(self):
        def row_in_tuple(row):
            return tuple(row)

        return tuple(map(row_in_tuple, self.__field__))

    def move(self, prev_col, prev_row, next_col, next_row):
        prev_cell_value = self.cell_value(prev_col, prev_row)
        if prev_cell_value is None:
            raise CellIsEmptyException
        if not self.__way_exists__(prev_col, prev_row, next_col, next_row):
            raise WayNotExistsException

        next_cell_value = self.cell_value(next_col, next_row)
        if next_cell_value is not None and next_cell_value != prev_cell_value:
            raise CellNotEmptyException

        if next_cell_value is None:
            self.set_cell_value(next_col, next_row, prev_cell_value)
            self.set_cell_value(prev_col, prev_row, None)
            self.__create_random_value__(2)
            return 0
        else:
            self.set_cell_value(next_col, next_row, next_cell_value + 1)
            self.set_cell_value(prev_col, prev_row, None)
            self.__create_random_value__(1)
            return next_cell_value

    def __create_random_value__(self, count_values):
        fulfilled_cells_counter = 0
        while fulfilled_cells_counter < count_values:
            cell = rand.randint(0, self.size ** 2 - 1)
            if self.cell_value(cell // self.size, cell % self.size) is None:
                probability = rand.random()
                value = (1 if probability < .65 else
                         (2 if probability < .85 else 3))
                self.set_cell_value(cell // self.size, cell % self.size, value)
                fulfilled_cells_counter += 1

    def __way_exists__(self, prev_col, prev_row, next_col, next_row, visited=None):
        if visited is None:
            visited = set()
        if prev_col not in range(0, self.size) or prev_row not in range(0, self.size) \
                or Cell(prev_col, prev_row) in visited:
            return False

        if prev_col == next_col and prev_row == next_row:
            return True

        if self.cell_value(prev_col, prev_row) is not None and len(visited) > 0:
            return False

        visited.add(Cell(prev_col, prev_row))
        return self.__way_exists__(prev_col - 1, prev_row, next_col, next_row, visited) \
            or self.__way_exists__(prev_col, prev_row - 1, next_col, next_row, visited) \
            or self.__way_exists__(prev_col + 1, prev_row, next_col, next_row, visited) \
            or self.__way_exists__(prev_col, prev_row + 1, next_col, next_row, visited)


class Cell:

    def __init__(self, col, row):
        self.row = row
        self.col = col

    def __eq__(self, o: object) -> bool:
        return self.col == o.col and self.row == o.row

    def __hash__(self) -> int:
        return hash(f'${self.col} ${self.row}')
