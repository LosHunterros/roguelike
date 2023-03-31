from random import randint

from config import *
import util
import view.ui as ui
import model.levels.level_generator as levels
import controller.player_controller as Player
import controller.enemies_controller as Enemies
import model.data_manager as data

MONSTER_LIST = "model\monster_list.csv"


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
    player = Player.Player(PLAYER_ICON, start_position_x, start_position_y, PLAYER_HP,PLAYER_EXPERIENCE,PLAYER_MAX_EXPERIENCE,PLAYER_MAX_HP,PLAYER_ATTACK)
    enemy_lvl_1=Enemies.Enemy_lvl_1(ENEMY_LVL_1_ICON, ENEMY_LVL_1_HP,ENEMY_LVL_1_EXPERIENCE,ENEMY_LVL_1_ATTACK)
    board = levels.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board = levels.create_forest(board, 10, player.position_x, player.position_y)
    data.clear_file(MONSTER_LIST)
    for i in range(10):
        enemy = enemy_lvl_1
        board, x, y = put_enemies_on_board(board, enemy_lvl_1.icon)
        single_enemy = {
            "HP": enemy_lvl_1.HP,
            "ATAK": enemy_lvl_1.attack,
            "EXP": enemy_lvl_1.EX,
            "position": [x, y],
        }
        data.write_in_file(MONSTER_LIST, single_enemy)
    util.clear_screen()
    is_running = True
    while is_running:
        board = put_on_board(board, player.position_x, player.position_y, player.icon)
        ui.display_board(board)
        key = util.key_pressed()
        if key == "q":
            is_running = False
        else:
            util.clear_screen()
            player.movement(board, key)
            board = put_on_board(
                board, player.position_x, player.position_y, player.icon
            )
            ui.display_board(board)
        util.clear_screen()
