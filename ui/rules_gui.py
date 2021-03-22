from pathlib import Path
from typing import Union

import pygame as pg
import re

from game.game import Game
from ui.gui_state.gui_state_constants import MENU_STATE, RULES_STATE
from ui.gui_uttils import is_click_in_circle
from ui.ui_constants import *


def draw_rules(game: Game, screen: Union):
    text_printer = pg.font.Font(None, RULES_FONT_SIZE)
    rules = re.split('\n', Path('./assets/rules.txt').read_text())
    for i in range(len(rules)):
        text = text_printer.render(rules[i], True, WHITE)
        screen.blit(text, (RULES_POS[0], RULES_POS[1] + RULES_FONT_SIZE * i))
    arrow_left_image = pg.image.load('./assets/images/arrow_left.png')
    screen.blit(arrow_left_image, ARROW_LEFT_POS)


def handle_rules_click(game: Game, event: pg.event):
    x, y = event.pos
    arrow_left_center = (ARROW_LEFT_POS[0] + ARROW_LEFT_SIZE / 2, ARROW_LEFT_POS[1] + ARROW_LEFT_SIZE / 2)
    if is_click_in_circle(x, y, arrow_left_center, ARROW_LEFT_SIZE / 2):
        return MENU_STATE, None
    return RULES_STATE, None
