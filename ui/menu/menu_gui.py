from typing import Union

import pygame as pg

from game.game import Game
from ui.gui_state.gui_state_constants import *
from ui.menu.menu_btns.continue_btn import continue_btn
from ui.menu.menu_btns.load_btn import load_game_btn
from ui.menu.menu_btns.new_game_btn import new_game_btn
from ui.menu.menu_btns.open_settings_btn import open_settings_btn
from ui.menu.menu_btns.rules_btn import rules_btn
from ui.menu.menu_btns.save_game_btn import save_game_btn
from ui.ui_constants import *

btns = [new_game_btn, continue_btn, save_game_btn, load_game_btn, rules_btn, open_settings_btn]


def draw_menu(game: Game, screen: Union):
    for i in range(len(btns)):
        pg.draw.rect(screen, MENU_BTN_COLOR,
                     (MENU_ACTION_HORIZONTAL_INDENT,
                      MENU_ACTION_VERTICAL_INDENT + (MENU_ACTION_BTN_HEIGHT + INDENT_BETWEEN_ACTION_BTN) * i,
                      MENU_ACTION_BTN_WIDTH, MENU_ACTION_BTN_HEIGHT))
        text_printer = pg.font.Font(None, ACTION_FONT)
        text = text_printer.render(btns[i].name, True, WHITE)
        screen.blit(text, (MENU_ACTION_HORIZONTAL_INDENT + 30,
                           MENU_ACTION_VERTICAL_INDENT + (MENU_ACTION_BTN_HEIGHT + INDENT_BETWEEN_ACTION_BTN) * i + 13))


def handle_menu_click(game: Game, event: pg.event):
    x, y = event.pos

    for i in range(len(btns)):
        y_start = MENU_ACTION_VERTICAL_INDENT + (MENU_ACTION_BTN_HEIGHT + INDENT_BETWEEN_ACTION_BTN) * i
        if x in range(MENU_ACTION_HORIZONTAL_INDENT, MENU_ACTION_HORIZONTAL_INDENT + MENU_ACTION_BTN_WIDTH) and \
                y in range(y_start,
                           y_start + MENU_ACTION_BTN_HEIGHT):
            return btns[i].handle_click(game)

    return MENU_STATE, None
