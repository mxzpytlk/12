import jsonpickle
from pathlib import Path

from game.game import Game
from ui.gui_state.gui_state_constants import GAME_STATE
from ui.menu.menu_btns.menu_btn import MenuBtn


def load_game(game: Game):
    json_game = Path('./assets/game.json').read_text()
    new_game = jsonpickle.decode(json_game)
    return GAME_STATE, new_game


load_game_btn = MenuBtn('Load game', load_game)
