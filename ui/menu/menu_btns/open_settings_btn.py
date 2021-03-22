from ui.gui_state.gui_state_constants import SETTINGS_STATE
from ui.menu.menu_btns.menu_btn import MenuBtn


def open_settings(game):
    return SETTINGS_STATE, None


open_settings_btn = MenuBtn('Settings', open_settings)
