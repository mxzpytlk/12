from game.game import Game
from ui.gui_state.gui_state_constants import RULES_STATE
from ui.menu.menu_btns.menu_btn import MenuBtn


def open_rules(game: Game):
    return RULES_STATE, None


rules_btn = MenuBtn('Rules', open_rules)
