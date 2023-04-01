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
    interface[14] = util.string_fill(f"{ENEMY_LVL_1_ICON} Healing Points: {ENEMY_LVL_1_HP}", 47) + "⬜"
    interface[15] = util.string_fill(f"{ENEMY_LVL_2_ICON} Healing Points: {ENEMY_LVL_2_HP}", 47) + "⬜"
    interface[16] = util.string_fill(f"{BOSS_ICON} Healing Points: {BOSS_HP}", 47) + "⬜"
    interface[18] = util.string_fill("Items:", 48).upper() + "⬜"
    interface[19] = util.string_fill(f"{ITEM_WATERMELON_ICON} Heal: {ITEM_WATERMELON_ADD_HP}", 47) + "⬜"
    interface[20] = util.string_fill(f"{ITEM_APPLE_ICON} Heal: {ITEM_APPLE_ADD_HP}", 47) + "⬜"
    interface[21] = util.string_fill(f"{ITEM_BANANA_ICON} Heal: {ITEM_BANANA_ADD_HP}", 47) + "⬜"
    interface[22] = util.string_fill(f"{ITEM_KNIFE_ICON} Attack: {ITEM_KNIFE_ATTACK}", 47) + "⬜"
    interface[23] = util.string_fill(f"{ITEM_MEDICINE_ICON} Max Healing Points: {MEDICINE_MAX_HP}", 47) + "⬜"
    interface[25] = util.string_fill(f"{NEXT_LEVEL}: Next level", 47) + "⬜"

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
    menu[8] = "⬜⬛⬛⬛⬛⬛⬛⬛⬜⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛  ⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜          Level: 1                    ⬜"
    menu[9] = "⬜⬛⬜⬜⬛⬜⬛⬛⬜⬛⬜⬜⬛⬛⬛⬛⬜⬜⬛  ⬜⬛                                                                                  ⬛⬜     Experience: 0/100                ⬜"
    menu[10] = "⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛  ⬜⬛" + util.string_fill(title.upper(), 82)                                        + "⬛⬜    Healing Points: 5/5               ⬜"
    menu[11] = "⬜⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬛  ⬜⬛                                                                                  ⬛⬜         Attack: 1                    ⬜"
    menu[12] = "⬜⬛⬛⬛⬛⬜⬛⬛⬜⬛⬛⬛⬛⬜⬛⬜⬛⬜⬛  ⬜⬛" + util.string_fill("(1) Play", 82)                                           + "⬛⬜                                      ⬜"
    menu[13] = "⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛  ⬜⬛" + util.string_fill("(2) Option 2", 82)                                       + "⬛⬜                                      ⬜"
    menu[14] = "⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛🐁⬛  ⬜⬛" + util.string_fill("(3) Option 3", 82)                                       + "⬛⬜                                      ⬜"
    menu[15] = "⬜⬜⬜⬛⬛⬜⬛⬛⬜⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛  ⬜⬛                                                                                  ⬛⬜                                      ⬜"
    menu[16] = "⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛  ⬜⬛" + util.string_fill("(0) Exit", 82)                                           + "⬛⬜                                      ⬜"
    menu[17] = "⬜⬜⬜⬜⬛⬜⬛⬛⬜⬛⬜⬛⬛⬜⬛⬜⬛⬛⬛  ⬜⬛                                                                                  ⬛⬜                                      ⬜"
    menu[18] = "⬜⬜⬜⬜⬛⬜⬛⬛⬜⬛⬜⬛⬛⬜⬛⬜⬛⬛⬛  ⬜⬛                                                                                  ⬛⬜                                      ⬜"
    menu[19] = "⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛  ⬜⬛                                                                                  ⬛⬜                                      ⬜"
    menu[20] = "⬜⬜⬜⬛⬛⬛🐁⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛  ⬜⬛                                                                                  ⬛⬜                                      ⬜"
    menu[21] = "⬜⬜⬜⬛⬜⬜⬛⬛⬜⬛⬜⬛⬛⬜⬛⬛⬜⬛⬛  ⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜                                      ⬜"
    menu[22] = "⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛  ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜                                      ⬜"
    menu[23] = "⬜⬛⬛⬛⬜⬛⬛⬛⬜⬛⬜⬛⬛⬜⬛⬛⬜⬛⬛                                                                                                                                  ⬜"
    menu[24] = "⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜                                                ⬜"
    menu[25] = "⬜⬛⬜⬜⬛🐁⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🧙⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜⬛⬜⬛⬛⬛⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜                                                ⬜"
    menu[26] = "⬜⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬜⬛⬜⬛⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜⬛⬜⬛⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜                                                ⬜"
    menu[27] = "⬜⬛⬜⬜⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛⬜⬛⬛⬜⬛⬛⬛⬛⬛🐁⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬜⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜                                                ⬜"
    menu[28] = "⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜                                                ⬜"
    menu[29] = "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"

    util.clear_screen()
    for line in menu:
            print(line)