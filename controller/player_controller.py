from config import *
import model.data_manager as data

MONSTER_LIST = "model\monster_list.csv"
ITEM_LIST = ""


class Player:
    def __init__(
        self,
        icon: str,
        posiotion_x: int,
        posiotion_y: int,
        atak: int,
        hp: int,
    ):
        self.icon = icon
        self.position_x = posiotion_x
        self.position_y = posiotion_y
        self.atak = atak
        self.max_hp = hp
        self.current_hp = hp
        self.lv = 1
        self.exp = 0

    def no_colision(self, board, position_x: int, position_y: int):
        return board[position_x, position_y] == PATH

    def fight_monster(self, monster, board, position):
        monster["HP"] -= self.atak
        if monster["HP"] <= 0:
            board[position[0], position[1]] = PATH
            self.exp += monster["EXP"]
            data.remove_line(MONSTER_LIST, str(position))
        else:
            self.current_hp -= monster["ATAK"]
            data.update_file(MONSTER_LIST, position, monster)
            self.level_up()
        return board

    def take_item(self):
        pass

    def colision_reaction(self, position, board):
        if board[position[0], position[1]] == WALL:
            return board
        monster = eval(data.search_for_data_in_file(MONSTER_LIST, position))
        # item = eval(data.search_for_data_in_file(ITEM_LIST, position))
        if monster != None:
            board = self.fight_monster(monster, board, position)
        # elif item != None:
        #     board = self.take_item()
        return board

    def level_up(self):
        if self.exp >= 100:
            self.lv += 1
            self.atak += 1
            self.max_hp += 2

    def movement(self, board, key: str):
        board[self.position_x, self.position_y] = PATH
        match key:
            case "w":
                if self.no_colision(board, self.position_x - 1, self.position_y):
                    self.position_x -= 1
                else:
                    board = self.colision_reaction(
                        [self.position_x - 1, self.position_y], board
                    )
            case "s":
                if self.no_colision(board, self.position_x + 1, self.position_y):
                    self.position_x += 1
                else:
                    board = self.colision_reaction(
                        [self.position_x + 1, self.position_y], board
                    )
            case "a":
                if self.no_colision(board, self.position_x, self.position_y - 1):
                    self.position_y -= 1
                else:
                    board = self.colision_reaction(
                        [self.position_x, self.position_y - 1], board
                    )
            case "d":
                if self.no_colision(board, self.position_x, self.position_y + 1):
                    self.position_y += 1
                else:
                    board = self.colision_reaction(
                        [self.position_x, self.position_y + 1], board
                    )
