import sys

import pygame as pg

from game.game import Game
from ui.gui_state.gui_state import GUI_State
from ui.ui_constants import *


def click(game: Game, event: pg.event, state: GUI_State):
    new_state_type, new_game = state.handle_click(game, event)
    new_state = state
    if new_state_type is not None:
        new_state = GUI_State.get_state(new_state_type)
    if new_game is None:
        new_game = game
    return new_state, new_game


def start(game: Game):
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT), pg.DOUBLEBUF)
    pg.display.set_caption('12')
    clock = pg.time.Clock()
    state = GUI_State.MENU

    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                state, game = click(game, event, state)

        screen.fill(BACKGROUND_COLOR)
        state.draw(game, screen)

        pg.display.flip()
        clock.tick(FPS)
