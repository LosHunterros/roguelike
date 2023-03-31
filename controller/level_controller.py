from random import randint

from config import *
import util
import view.ui as ui
import model.levels.level_generator as levels
import controller.player_controller as Player
import controller.enemies_controller as Enemies
import model.data_manager as data
import ast

MONSTER_LIST = "model\monster_list.csv"
ITEM_POSITION = "model\item_position.csv"
ITEM_DICTIONARY = "model\item_list.txt"


def get_random_coordinates():
    return randint(1, BOARD_HEIGHT - 2), randint(1, BOARD_WIDTH - 2)


def get_random_path(board):
    position_x = None
    position_y = None
    while position_x == None or position_y == None:
        position_x, position_y = get_random_coordinates()
        if board[position_x, position_y] == WALL:
            position_x = None
            position_y = None

    return position_x, position_y


def put_on_board(board, position_x, position_y, icon):
    board[position_x, position_y] = icon
    return board


def put_enemies_on_board(board, enemy_icon):
    start_enemy_position_x, start_enemy_position_y = get_random_path(board)
    board = put_on_board(
        board, start_enemy_position_x, start_enemy_position_y, enemy_icon
    )
    return board, start_enemy_position_x, start_enemy_position_y
    # '''
    # Modifies the game board by placing the player icon at its coordinates.

    # Args:
    # list: The game board
    # dictionary: The player information containing the icon and coordinates

    # Returns:
    # Nothing
    # '''
    # pass


def level():

    start_position_x, start_position_y = get_random_coordinates()
    player = Player.Player(start_position_x, start_position_y)
    enemy_lvl_1 = Enemies.Enemy_lvl_1(
        ENEMY_LVL_1_ICON, ENEMY_LVL_1_HP, ENEMY_LVL_1_EXPERIENCE, ENEMY_LVL_1_ATTACK
    )
    enemy_lvl_2 = Enemies.Enemy_lvl_2(
        ENEMY_LVL_2_ICON, ENEMY_LVL_2_HP, ENEMY_LVL_2_EXPERIENCE, ENEMY_LVL_2_ATTACK
    )
    board = levels.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board = levels.create_forest(board, 10, player.position_x, player.position_y)
    data.clear_file(MONSTER_LIST)
    data.clear_file(ITEM_POSITION)
    for enemy in [enemy_lvl_1, enemy_lvl_2]:
        for _ in range(10):
            board, x, y = put_enemies_on_board(board, enemy.icon)
            single_enemy = {
                "HP": enemy.HP,
                "ATAK": enemy.attack,
                "EXP": enemy.experience,
                "position": [x, y],
            }
            data.write_in_file(MONSTER_LIST, single_enemy)
    items = data.read_file_to_list(ITEM_DICTIONARY)
    for item in items:
        item = eval(item)
        for _ in range(10):
            board, x, y = put_enemies_on_board(board, item["icon"])
            single_item = {
                "heal_HP": item["heal_HP"],
                "max_HP": item["max_HP"],
                "ATAK": item["ATAK"],
                "EX": item["EX"],
                "position": [x, y],
            }
            data.write_in_file(ITEM_POSITION, single_item)
    util.clear_screen()
    is_running = True
    while is_running:
        board = put_on_board(board, player.position_x, player.position_y, player.icon)
        ui.display_board(board, player)
        key = util.key_pressed()
        if key == "q":
            is_running = False
        else:
            util.clear_screen()
            player.movement(board, key)
            board = put_on_board(
                board, player.position_x, player.position_y, player.icon
            )
            ui.display_board(board, player)
        util.clear_screen()
