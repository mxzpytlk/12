from game.field.field import *


class Game:
    def __init__(self, field_size=5) -> None:
        self.score = 0
        self.__field__ = Field(field_size)
        self.selected_cell = None
        self.game_over = False

    @property
    def field(self):
        return self.__field__.field

    @property
    def field_size(self):
        return self.__field__.size

    def cell_value(self, col, row):
        return self.field[col][row]

    def select_cell(self, row, col):
        if self.is_cell_selected(row, col):
            self.selected_cell = None
        elif self.selected_cell is not None:
            adding_score: int = self.__field__.move(*self.selected_cell, row, col) + 1
            self.score += adding_score
            self.selected_cell = None
            self.game_over = adding_score == 12
        elif self.cell_value(row, col) is not None:
            self.selected_cell = (row, col)

    def unselect_cell(self):
        self.selected_cell = None

    def is_cell_selected(self, row, col):
        return self.selected_cell is not None and self.selected_cell[0] == row and self.selected_cell[1] == col

    def restart(self, field_size=5):
        self.score = 0
        self.__field__ = Field(field_size)
        self.selected_cell = None
        self.game_over = False
