from config import *
import util

def display_board(board):
    interface = [""] * BOARD_HEIGHT
    for i, row in enumerate(interface):
        interface[i] = "                                                ⬜"

    interface[0] =              "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"
    interface[BOARD_HEIGHT-1] = "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"
    interface[3] = util.string_fill("Roguelike Game", 48).upper() + "⬜"
    interface[5] = util.string_fill("Level: x", 48).upper() + "⬜"
    interface[7] = util.string_fill("Player statistics:", 48).upper() + "⬜"
    interface[8] = util.string_fill("Level: x", 48) + "⬜"
    interface[9] = util.string_fill("Experience: x", 48) + "⬜"
    interface[10] = util.string_fill("Healing Points: x/x", 48) + "⬜"
    interface[11] = util.string_fill("Attack: x", 48) + "⬜"
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
    print(f"\n{title.upper()}\n")
    for i, option in enumerate(list_options):
        if i != 0:
            print(f"({i}) {option}")

    print(f"\n(0) {list_options[0]}")