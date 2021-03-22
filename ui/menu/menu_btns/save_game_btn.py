import jsonpickle
from pathlib import Path

from game.game import Game
from ui.gui_state.gui_state_constants import MENU_STATE
from ui.menu.menu_btns.menu_btn import MenuBtn


def save_game(game: Game):
    game_json = jsonpickle.encode(game)
    Path('./assets/game.json').write_text(game_json)
    return MENU_STATE, None


save_game_btn = MenuBtn('Save game', save_game)
