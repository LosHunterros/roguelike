from random import randint
import sys

from config import *
import util
import view.ui as ui
import model.levels.level_generator as levels
import model.levels.level_2 as level_2
import model.levels.level_3 as level_3
import controller.player_controller as Player
import controller.enemies_controller as Enemies
import model.data_manager as data
import time

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
        if board[position_x][position_y] != PATH:
            position_x = None
            position_y = None

    return position_x, position_y


def put_on_board(board, position_x, position_y, icon):
    board[position_x][position_y] = icon
    return board


def put_icon_on_board(board, icon):
    start_icon_position_x, start_icon_position_y = get_random_path(board)
    board = put_on_board(
        board, start_icon_position_x, start_icon_position_y, icon
    )
    return board, start_icon_position_x, start_icon_position_y
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
    board = board.tolist()
    data.clear_file(MONSTER_LIST)
    data.clear_file(ITEM_POSITION)
    for enemy in [enemy_lvl_1, enemy_lvl_2]:
        for _ in range(10):
            board, x, y = put_icon_on_board(board, enemy.icon)
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
            board, x, y = put_icon_on_board(board, item["icon"])
            single_item = {
                "heal_HP": item["heal_HP"],
                "max_HP": item["max_HP"],
                "ATAK": item["ATAK"],
                "EX": item["EX"],
                "position": [x, y],
            }
            data.write_in_file(ITEM_POSITION, single_item)
    
    board, x, y = put_icon_on_board(board, NEXT_LEVEL)
    is_running = True
    while is_running:
        board = put_on_board(board, player.position_x, player.position_y, player.icon)
        ui.display_board(board, player)
        key = util.key_pressed()
        if key == "q":
            is_running = False
        elif key in ["w", "s", "a", "d"]:
            board = player.movement(board, key)
            if board != False:
                board = put_on_board(board, player.position_x, player.position_y, player.icon)
                ui.display_board(board, player)

        if board == False: is_running = False

        if player.current_hp <= 0:
            is_running = False
            ui.display_gameover()
            sys.exit()



    player.position_x = 2
    player.position_y = 2
    enemy_lvl_1 = Enemies.Enemy_lvl_1(
        ENEMY_LVL_1_ICON, ENEMY_LVL_1_HP, ENEMY_LVL_1_EXPERIENCE, ENEMY_LVL_1_ATTACK
    )
    enemy_lvl_2 = Enemies.Enemy_lvl_2(
        ENEMY_LVL_2_ICON, ENEMY_LVL_2_HP, ENEMY_LVL_2_EXPERIENCE, ENEMY_LVL_2_ATTACK
    )
    board = level_2.BOARD_LVL_2
    data.clear_file(MONSTER_LIST)
    data.clear_file(ITEM_POSITION)
    for enemy in [enemy_lvl_1, enemy_lvl_2]:
        for _ in range(10):
            board, x, y = put_icon_on_board(board, enemy.icon)
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
            board, x, y = put_icon_on_board(board, item["icon"])
            single_item = {
                "heal_HP": item["heal_HP"],
                "max_HP": item["max_HP"],
                "ATAK": item["ATAK"],
                "EX": item["EX"],
                "position": [x, y],
            }
            data.write_in_file(ITEM_POSITION, single_item)
    
    board = put_on_board(board, 29, 52, NEXT_LEVEL)
    is_running = True
    while is_running:
        board = put_on_board(board, player.position_x, player.position_y, player.icon)
        ui.display_board(board, player)
        key = util.key_pressed()
        if key == "q":
            is_running = False
        elif key in ["w", "s", "a", "d"]:
            board = player.movement(board, key)
            if board != False:
                board = put_on_board(board, player.position_x, player.position_y, player.icon)
                ui.display_board(board, player)

        if board == False: is_running = False

        if player.current_hp <= 0:
            is_running = False
            ui.display_gameover()
            sys.exit()



    player.position_x = 22
    player.position_y = 29
    enemy_lvl_2 = Enemies.Enemy_lvl_2(
        ENEMY_LVL_2_ICON, ENEMY_LVL_2_HP, ENEMY_LVL_2_EXPERIENCE, ENEMY_LVL_2_ATTACK
    )
    boss = Enemies.Boss(
        BOSS_ICON, BOSS_HP, BOSS_EXPERIENCE, BOSS_ATTACK
    )
    board = level_3.BOARD_LVL_3
    data.clear_file(MONSTER_LIST)
    data.clear_file(ITEM_POSITION)
    board = put_on_board(board, 10, 29, enemy_lvl_2.icon)
    single_enemy = {
        "HP": enemy_lvl_2.HP,
        "ATAK": enemy_lvl_2.attack,
        "EXP": enemy_lvl_2.experience,
        "position": [10, 29],
    }
    data.write_in_file(MONSTER_LIST, single_enemy)
    board = put_on_board(board, 10, 28, enemy_lvl_2.icon)
    single_enemy = {
        "HP": enemy_lvl_2.HP,
        "ATAK": enemy_lvl_2.attack,
        "EXP": enemy_lvl_2.experience,
        "position": [10, 28],
    }
    data.write_in_file(MONSTER_LIST, single_enemy)
    board = put_on_board(board, 10, 30, enemy_lvl_2.icon)
    single_enemy = {
        "HP": enemy_lvl_2.HP,
        "ATAK": enemy_lvl_2.attack,
        "EXP": enemy_lvl_2.experience,
        "position": [10, 30],
    }
    data.write_in_file(MONSTER_LIST, single_enemy)
    board = put_on_board(board, 9, 29, boss.icon)
    single_enemy = {
        "HP": boss.HP,
        "ATAK": boss.attack,
        "EXP": boss.experience,
        "position": [9, 29],
    }
    data.write_in_file(MONSTER_LIST, single_enemy)

    is_running = True
    while is_running:
        board = put_on_board(board, player.position_x, player.position_y, player.icon)
        ui.display_board(board, player)
        key = util.key_pressed()
        if key == "q":
            is_running = False
        elif key in ["w", "s", "a", "d"]:
            board = player.movement(board, key)
            if board != False:
                board = put_on_board(board, player.position_x, player.position_y, player.icon)
                ui.display_board(board, player)

        if board == False: is_running = False

        if player.current_hp <= 0:
            is_running = False
            ui.display_gameover()
            sys.exit()