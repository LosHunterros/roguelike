from random import randint

from config import *
import util
import view.ui as ui
import model.levels.level_generator as levels
import controller.player_controller as Player


def get_random_coordinates():
    return randint(0, BOARD_HEIGHT-1), randint(0, BOARD_WIDTH-1)

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


def put_enemies_on_board(board,enemy_icon):
    start_enemy_position_x, start_enemy_position_y = get_random_path(board)
    board=put_on_board(board,start_enemy_position_x, start_enemy_position_y,enemy_icon)
    return board
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
    player = Player.Player(PLAYER_ICON, start_position_x, start_position_y)
    board = levels.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board = levels.create_forest(board, 10, player.position_x, player.position_y)
    for i in range(10):
        board=put_enemies_on_board(board, str(ENEMIES["small"]["icon"]))

    util.clear_screen()
    is_running = True
    while is_running:
        board = put_on_board(board, player.position_x, player.position_y, player.icon)
        ui.display_board(board)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            util.clear_screen()
            player.movement(board, key)
            board = put_on_board(board, player.position_x, player.position_y, player.icon)
            ui.display_board(board)
        util.clear_screen()
