from typing import Union

import pygame as pg

from game.game import Game
from ui.gui_state.gui_state_constants import MENU_STATE, SETTINGS_STATE
from ui.gui_uttils import is_click_in_circle
from ui.ui_constants import *

field_sizes = tuple(range(5, 9))
indent_between_sizes = (WIDTH - 2 * MENU_ACTION_HORIZONTAL_INDENT) // len(field_sizes)


def draw_settings(game: Game, screen: Union):
    text_printer = pg.font.Font(None, ACTION_FONT)
    field_size_text = text_printer.render('FIELD SIZE', True, WHITE)
    screen.blit(field_size_text, (MENU_ACTION_HORIZONTAL_INDENT, MENU_ACTION_VERTICAL_INDENT))

    for i in range(len(field_sizes)):
        size = text_printer.render(str(field_sizes[i]), True, WHITE)
        screen.blit(size,
                    (MENU_ACTION_HORIZONTAL_INDENT + indent_between_sizes * i,
                     MENU_ACTION_VERTICAL_INDENT * 1.1 + ACTION_FONT))
        pg.draw.circle(screen, WHITE,
                       (MENU_ACTION_HORIZONTAL_INDENT + RADIO_BTN_R + indent_between_sizes * i,
                        MENU_ACTION_VERTICAL_INDENT * 1.1 + ACTION_FONT * 2.1), RADIO_BTN_R,
                       0 if game.field_size == field_sizes[i] else 1)

    arrow_left_image = pg.image.load('./assets/images/arrow_left.png')
    screen.blit(arrow_left_image, ARROW_LEFT_POS)


def is_click_in_return_btn(x, y):
    center_x = ARROW_LEFT_POS[0] + ARROW_LEFT_SIZE / 2
    center_y = ARROW_LEFT_POS[1] + ARROW_LEFT_SIZE / 2
    return (center_x - x) ** 2 + (center_y - y) ** 2 <= (ARROW_LEFT_SIZE / 2) ** 2


def handle_settings_click(game: Game, event: pg.event):
    x, y = event.pos
    arrow_left_center = (ARROW_LEFT_POS[0] + ARROW_LEFT_SIZE / 2, ARROW_LEFT_POS[1] + ARROW_LEFT_SIZE / 2)
    if is_click_in_circle(x, y, arrow_left_center, ARROW_LEFT_SIZE / 2):
        return MENU_STATE, None

    for i in range(len(field_sizes)):
        if is_click_in_circle(x, y, (MENU_ACTION_HORIZONTAL_INDENT + RADIO_BTN_R + indent_between_sizes * i,
                                     MENU_ACTION_VERTICAL_INDENT * 1.1 + ACTION_FONT * 2.1), RADIO_BTN_R):
            return SETTINGS_STATE, Game(field_size=field_sizes[i])

    return SETTINGS_STATE, None
