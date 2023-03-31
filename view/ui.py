from config import *
import util

def display_board(board, player):
    interface = [""] * BOARD_HEIGHT
    for i, row in enumerate(interface):
        interface[i] = "                                                ⬜"

    interface[0] =              "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"
    interface[BOARD_HEIGHT-1] = "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"
    interface[3] = util.string_fill("Roguelike Game", 48).upper() + "⬜"
    interface[5] = util.string_fill("Level: x", 48).upper() + "⬜"
    interface[7] = util.string_fill("Player statistics:", 48).upper() + "⬜"
    interface[8] = util.string_fill(f"Level: {player.lv}", 48) + "⬜"
    interface[9] = util.string_fill(f"Experience: {player.exp}/{player.exp_nedded}", 48) + "⬜"
    interface[10] = util.string_fill(f"Healing Points: {player.current_hp}/{player.max_hp}", 48) + "⬜"
    interface[11] = util.string_fill(f"Attack: {player.atak}", 48) + "⬜"
    interface[13] = util.string_fill("Creatures:", 48).upper() + "⬜"
    interface[14] = util.string_fill("🐁 HP: x", 47) + "⬜"
    interface[15] = util.string_fill("🐁 HP: x", 47) + "⬜"
    interface[16] = util.string_fill("🐁 HP: x", 47) + "⬜"
    interface[17] = util.string_fill("🐁 HP: x", 47) + "⬜"
    interface[19] = util.string_fill("Items:", 48).upper() + "⬜"
    interface[20] = util.string_fill("🍎 HP: +x", 47) + "⬜"
    interface[21] = util.string_fill("🍎 HP: +x", 47) + "⬜"
    interface[22] = util.string_fill("🍎 HP: +x", 47) + "⬜"
    interface[23] = util.string_fill("🍎 HP: +x", 47) + "⬜"

    board_list = board.tolist()
    for i, row in enumerate(board_list):
        print((''.join(row)) +  interface[i])

    # '''
    # Displays complete game board on the screen

    # Returns:
    # Nothing
    # '''
    # pass


def display_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Option 1
    (2) Option 2
    (3) Option 3
    (0) Exit

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    menu = [""] * BOARD_HEIGHT
    menu[0] = "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"
    menu[1] = "⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜                                                ⬜"
    menu[2] = "⬜⬛⬛⬛⬛⬛⬛⬛⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬛⬜⬜⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬛⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜                                                ⬜"
    menu[3] = "⬜⬛⬛⬛⬛⬛⬛⬛⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬛⬜⬜⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬛⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜                 ROGUELIKE GAME                 ⬜"
    menu[4] = "⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬜⬛⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🐁⬛⬛⬛⬜⬜⬜                                                ⬜"
    menu[5] = "⬜⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜⬜⬛⬜⬛⬛⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜⬛⬛⬜⬛⬜⬜⬛⬜⬜⬜                    LEVEL: X                    ⬜"
    menu[6] = "⬜⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜⬜⬛⬜⬜⬛⬜⬜⬛                                                                                                                                  ⬜"
    menu[7] = "⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛  ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜     PLAYER STATISTICS:               ⬜"
    menu[8] = "⬜⬛⬛⬛⬛⬛⬛⬛⬜⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛  ⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜          Level: x                    ⬜"
    menu[9] = "⬜⬛⬜⬜⬛⬜⬛⬛⬜⬛⬜⬜⬛⬛⬛⬛⬜⬜⬛  ⬜⬛                                                                                  ⬛⬜       Experience: x                  ⬜"
    menu[10] = "⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛  ⬜⬛" + util.string_fill(title.upper(), 82)                                        + "⬛⬜    Healing Points: x/x               ⬜"
    menu[11] = "⬜⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬛  ⬜⬛                                                                                  ⬛⬜         Attack: x                    ⬜"
    menu[12] = "⬜⬛⬛⬛⬛⬜⬛⬛⬜⬛⬛⬛⬛⬜⬛⬜⬛⬜⬛  ⬜⬛" + util.string_fill("(1) Play", 82)                                           + "⬛⬜                                      ⬜"
    menu[13] = "⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛  ⬜⬛" + util.string_fill("(2) Option 2", 82)                                       + "⬛⬜         CREATURES:                   ⬜"
    menu[14] = "⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛🐁⬛  ⬜⬛" + util.string_fill("(3) Option 3", 82)                                       + "⬛⬜          🐁 HP: x                    ⬜"
    menu[15] = "⬜⬜⬜⬛⬛⬜⬛⬛⬜⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛  ⬜⬛                                                                                  ⬛⬜          🐁 HP: x                    ⬜"
    menu[16] = "⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛  ⬜⬛" + util.string_fill("(0) Exit", 82)                                           + "⬛⬜          🐁 HP: x                    ⬜"
    menu[17] = "⬜⬜⬜⬜⬛⬜⬛⬛⬜⬛⬜⬛⬛⬜⬛⬜⬛⬛⬛  ⬜⬛                                                                                  ⬛⬜          🐁 HP: x                    ⬜"
    menu[18] = "⬜⬜⬜⬜⬛⬜⬛⬛⬜⬛⬜⬛⬛⬜⬛⬜⬛⬛⬛  ⬜⬛                                                                                  ⬛⬜                                      ⬜"
    menu[19] = "⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛  ⬜⬛                                                                                  ⬛⬜           ITEMS:                     ⬜"
    menu[20] = "⬜⬜⬜⬛⬛⬛🐁⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛  ⬜⬛                                                                                  ⬛⬜         🍎 HP: +x                    ⬜"
    menu[21] = "⬜⬜⬜⬛⬜⬜⬛⬛⬜⬛⬜⬛⬛⬜⬛⬛⬜⬛⬛  ⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜         🍎 HP: +x                    ⬜"
    menu[22] = "⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛  ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜         🍎 HP: +x                    ⬜"
    menu[23] = "⬜⬛⬛⬛⬜⬛⬛⬛⬜⬛⬜⬛⬛⬜⬛⬛⬜⬛⬛                                                                                                     🍎 HP: +x                    ⬜"
    menu[24] = "⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜                                                ⬜"
    menu[25] = "⬜⬛⬜⬜⬛🐁⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🧙⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜⬛⬜⬛⬛⬛⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜                                                ⬜"
    menu[26] = "⬜⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬜⬛⬜⬛⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜⬛⬜⬛⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜                                                ⬜"
    menu[27] = "⬜⬛⬜⬜⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛⬜⬛⬛⬜⬛⬛⬛⬛⬛🐁⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬜⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜                                                ⬜"
    menu[28] = "⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜                                                ⬜"
    menu[29] = "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"

    util.clear_screen()
    for line in menu:
            print(line)