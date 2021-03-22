from enum import Enum
from typing import Union

from game.game import Game
from ui.game_gui import draw_field, handle_game_click
from ui.menu.menu_gui import draw_menu, handle_menu_click
from ui.rules_gui import draw_rules, handle_rules_click
from ui.gui_state.gui_state_constants import *

import pygame as pg

from ui.settings_gui import draw_settings, handle_settings_click


class GUI_State(Enum):
    MENU = (MENU_STATE, draw_menu, handle_menu_click)
    GAME = (GAME_STATE, draw_field, handle_game_click)
    RULES = (RULES_STATE, draw_rules, handle_rules_click)
    SETTINGS = (SETTINGS_STATE, draw_settings, handle_settings_click)

    def __init__(self, state, draw_func, click_handler):
        self.__click_handler__ = click_handler
        self.__draw_func__ = draw_func
        self.__type__ = state

    def draw(self, game: Game, screen: Union):
        self.__draw_func__(game, screen)

    def handle_click(self, game: Game, event: pg.event):
        return self.__click_handler__(game, event)

    @staticmethod
    def get_state(state_id):
        for state in GUI_State:
            if state.__type__ == state_id:
                return state
        return GUI_State.MENU
