from game.game import Game
from ui.gui_state.gui_state_constants import GAME_STATE
from ui.menu.menu_btns.menu_btn import MenuBtn


def restart_game(game: Game):
    return GAME_STATE, Game(game.field_size)


new_game_btn = MenuBtn('New game', restart_game)
