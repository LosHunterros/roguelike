from config import *
import numpy as np
from random import randint, choice
import controller.level_controller as lc


class Game_Map:
    def __init__(self, width: int, hight: int):
        self.width = width
        self.hight = hight

    def creat_base_map(self):
        board = np.full((self.hight, self.width), WALL)
        return board

    class Forest:
        def __init__(self, tree: str, grass: str, steps: int):
            self.tree = tree
            self.grass = grass
            self.steps = steps

        def replant_trees(self, board, x, y):

            place_for_tree = [
                board[x, y] == PATH,
                board[x - 1, y] == PATH,
                board[x, y - 1] == PATH,
                board[x, y + 1] == PATH,
                board[x + 1, y] == PATH,
                board[x - 2, y] == PATH,
                board[x - 2, y - 1] == PATH,
                board[x - 2, y + 1] == PATH,
                board[x - 1, y - 2] == PATH,
                board[x - 1, y - 1] == PATH,
                board[x - 1, y + 2] == PATH,
                board[x - 1, y + 1] == PATH,
                board[x, y - 2] == PATH,
                board[x, y + 2] == PATH,
                board[x + 1, y - 2] == PATH,
                board[x + 1, y - 1] == PATH,
                board[x + 1, y + 1] == PATH,
                board[x + 1, y + 2] == PATH,
                board[x + 2, y - 1] == PATH,
                board[x + 2, y] == PATH,
                board[x + 2, y + 1] == PATH,
            ]
            for condition in place_for_tree:
                try:
                    condition
                except IndexError:
                    pass
            if len(place_for_tree) == 21 and all(place_for_tree):
                board[x, y] = WALL
                board[x - 1, y] = WALL
                board[x, y - 1] = WALL
                board[x, y + 1] = WALL
                board[x + 1, y] = WALL
                return board, True
            return board, False

        def drunk_troll(self, x: int, y: int, board: list):
            number_of_trees_to_leave = int(np.count_nonzero(board == WALL) * 0.3)
            board[x, y] = self.grass
            y_conditions = [
                [y + 1 > 1, y + 1 < len(board[0]) - 2],
                [y - 1 > 1, y - 1 < len(board[0]) - 2],
            ]
            x_conditions = [
                [x + 1 > 1, x + 1 < len(board) - 2],
                [x - 1 > 1, x - 1 < len(board) - 2],
            ]
            if all(y_conditions[0]):
                board[x, y + 1] = self.grass
                if all(x_conditions[0]):
                    board[x + 1, y + 1] = self.grass
                    if all(x_conditions[1]):
                        board[x - 1, y + 1] = self.grass
            if all(y_conditions[1]):
                board[x, y - 1] = self.grass
                if all(x_conditions[0]):
                    board[x + 1, y - 1] = self.grass
                    if all(x_conditions[1]):
                        board[x - 1, y - 1] = self.grass
            while np.count_nonzero(board == WALL) > number_of_trees_to_leave:
                for _ in range(self.steps):
                    board[x, y] = self.grass
                    available_direction = []
                    posible_direction = {
                        "w": [x - 1, y],
                        "s": [x + 1, y],
                        "a": [x, y - 1],
                        "d": [x, y + 1],
                    }
                    for key in posible_direction.keys():
                        try:
                            board[posible_direction[key]]
                        except:
                            pass
                        conditions = [
                            posible_direction[key][0] > 1,
                            posible_direction[key][0] < len(board) - 2,
                            posible_direction[key][1] > 1,
                            posible_direction[key][1] < len(board[0]) - 2,
                        ]
                        if all(conditions):
                            available_direction.append(posible_direction[key])
                    try:
                        direction = choice(available_direction)
                        x, y = direction
                    except IndexError:
                        x = randint(1, len(board) - 2)
                        y = randint(1, len(board[0]) - 2)
                    available_direction.clear()
            i = 0
            j = 0
            while i < 15 or j < 30:
                x, y = None, None
                while x == None and y == None:
                    x, y = lc.get_random_path(board)
                board, tree_was_planted = self.replant_trees(board, x, y)
                if tree_was_planted:
                    i += 1
                j += 1

            return board

    #
    # DOESN"T WORK YET
    # class Cave:
    #     def __init__(self, wall: str, path: str, x, y):
    #         self.wall = wall
    #         self.path = path
    #         self.center_x = x
    #         self.center_y = y

    #     def dig_cave(self, board):
    #         number_of_particles = int(np.count_nonzero(board == "#")*0.1)
    #         board[self.center_x, self.center_y] = self.path
    #         board[self.center_x, self.center_y+1] = self.path
    #         board[self.center_x + 1, self.center_y] = self.path
    #         board[self.center_x + 1, self.center_y+1] = self.path
    #         for _ in range(number_of_particles):
    #             x, y = self.center_x, self.center_y
    #             while board[x, y] == PATH:
    #                 x, y = randint(1, len(board)-2), randint(1,
    #                                                          len(board[0])-2)
    #             while board[x, y] != PATH:
    #                 while x > 1 or x < len(board)-2 or y > 1 or y < len(board[0])-2:
    #                     previous_x = x
    #                     previous_y = y
    #                     x += choice([-1, 1])
    #                     y += choice([-1, 1])
    #             board[previous_x, previous_y] = self.path
    #         return board


def create_board(width, hight):
    board = Game_Map(width, hight).creat_base_map()
    return board


def create_forest(board, steps, x, y):
    forest = Game_Map.Forest(WALL, PATH, steps).drunk_troll(x, y, board)
    return forest


def create_cave(board, x, y):
    cave = Game_Map.Cave(WALL, PATH, x, y).dig_cave(board)
    return cave
