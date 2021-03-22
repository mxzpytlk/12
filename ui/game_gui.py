from typing import Union

import pygame as pg

from game.field.field_exceptions import FieldException
from game.game import Game
from ui.ui_constants import *
from ui.gui_state.gui_state_constants import *


def update_game(game: Game, mouse_x, mouse_y):
    field = game.field
    field_size = len(field)

    field_x = mouse_x - HORIZONTAL_INDENT
    field_width = WIDTH - HORIZONTAL_INDENT * 2
    col = int(field_x / field_width * field_size)

    field_y = mouse_y - VERTICAL_INDENT
    field_height = HEIGHT - VERTICAL_INDENT
    row = int(field_y / field_height * field_size)
    try:
        game.select_cell(row, col)
    except FieldException:
        game.unselect_cell()


def draw_score(game: Game, screen: Union):
    score_printer = pg.font.Font(None, 60)
    score = score_printer.render(f'Score: {game.score}', True, WHITE)
    screen.blit(score, SCORE_POS)


def draw_menu_btn(screen: Union):
    pg.draw.rect(screen, MENU_BTN_COLOR, (MENU_BTN_POS[0], MENU_BTN_POS[1], MENU_BTN_WIDTH, MENU_BTN_HEIGHT))
    printer = pg.font.Font(None, 60)
    text = printer.render('Menu', True, WHITE)
    screen.blit(text, (MENU_BTN_POS[0] + 17, MENU_BTN_POS[1] + 17))


def draw_field(game: Game, screen: Union):
    field = game.field
    field_size = len(field)

    cell_size = (WIDTH - HORIZONTAL_INDENT) // field_size - INDENT_BETWEEN_CELLS
    draw_score(game, screen)
    draw_menu_btn(screen)

    for i in range(field_size):
        y = VERTICAL_INDENT + i * (cell_size + (INDENT_BETWEEN_CELLS if i != 0 else 0))
        for j in range(field_size):
            x = HORIZONTAL_INDENT + j * (cell_size + (INDENT_BETWEEN_CELLS if j != 0 else 0))
            color = (CELL_COLOR if game.cell_value(i, j) is None else CELL_COLORS[game.cell_value(i, j) - 1])
            pg.draw.rect(screen, color, (x, y, cell_size, cell_size))
            if game.is_cell_selected(i, j):
                pg.draw.rect(screen, CELL_BORDER_COLOR, (x, y, cell_size, cell_size), 8)

            if game.cell_value(i, j) is not None:
                cell_value_printer = pg.font.Font(None, 450 // game.field_size)
                value = cell_value_printer.render(str(game.cell_value(i, j)), True, WHITE)
                screen.blit(value, (x + cell_size / 3, y + cell_size / 3))


def handle_game_click(game: Game, event: pg.event):
    x, y = event.pos
    if x in range(HORIZONTAL_INDENT, WIDTH - HORIZONTAL_INDENT) and y in range(VERTICAL_INDENT, HEIGHT):
        update_game(game, x, y)
        if game.game_over:
            game.restart()
            return MENU_STATE, None

    if x in range(MENU_BTN_POS[0], MENU_BTN_POS[0] + MENU_BTN_WIDTH) and \
            y in range(MENU_BTN_POS[1], MENU_BTN_POS[1] + MENU_BTN_HEIGHT):
        game.unselect_cell()
        return MENU_STATE, None

    return GAME_STATE, None
