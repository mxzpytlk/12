from ui.gui_state.gui_state_constants import GAME_STATE
from ui.menu.menu_btns.menu_btn import MenuBtn


def continue_game(game):
    return GAME_STATE, None


continue_btn = MenuBtn('Continue', continue_game)
