from config import *
import numpy as np
from random import randint, choice


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

        def drunk_troll(self, x: int, y: int, board: list):
            number_of_trees_to_leave = int(np.count_nonzero(board == WALL)*0.4)
            board[x, y] = self.grass
            board[x, y+1] = self.grass
            board[x+1, y] = self.grass
            board[x+1, y+1] = self.grass
            posible_direction = {
                'w': [x-1, y], 's': [x+1, y], 'a': [x, y-1], 'd': [x, y+1]}
            while np.count_nonzero(board == WALL) > number_of_trees_to_leave:
                steps_to_make = self.steps
                while steps_to_make > 0:
                    next_x = 0
                    next_y = 0
                    while next_x < 1 or next_x > len(board)-2 or next_y < 1 or next_y > len(board[0])-2:
                        direction = choice(list(posible_direction.items()))
                        next_x, next_y = direction[1]
                    for _ in range(3):
                        board[x, y] = self.grass
                        x, y = next_x, next_y
                        posible_direction = {
                            'w': [x-1, y], 's': [x+1, y], 'a': [x, y-1], 'd': [x, y+1]}
                        next_x, next_y = posible_direction[direction[0]]
                        while next_x < 1 or next_x > len(board)-2 or next_y < 1 or next_y > len(board[0])-2:
                            direction = choice(list(posible_direction.items()))
                            next_x, next_y = direction[1]
                        steps_to_make -= 1
                x = randint(1, len(board)-2)
                y = randint(1, len(board[0])-2)
                while board[x, y] == self.tree:
                    x = randint(1, len(board)-2)
                    y = randint(1, len(board[0])-2)
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