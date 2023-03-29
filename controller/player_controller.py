from config import *

class Player:
    def __init__(self, icon: str, posiotion_x: int, posiotion_y: int):
        self.icon = icon
        self.position_x = posiotion_x
        self.position_y = posiotion_y

    def no_colision(self, board, position_x: int, position_y: int):
        return board[position_x, position_y] != WALL

    def movement(self, board, key: str):
        board[self.position_x, self.position_y] = PATH
        match key:
            case 'w':
                if self.no_colision(board, self.position_x - 1, self.position_y):
                    self.position_x -= 1
            case 's':
                if self.no_colision(board, self.position_x + 1, self.position_y):
                    self.position_x += 1
            case 'a':
                if self.no_colision(board, self.position_x, self.position_y - 1):
                    self.position_y -= 1
            case 'd':
                if self.no_colision(board, self.position_x, self.position_y + 1):
                    self.position_y += 1