from config import *
import model.data_manager as data

MONSTER_LIST = "model\monster_list.csv"
ITEM_POSITION = "model\item_position.csv"


class Player:
    def __init__(self, posiotion_x: int, posiotion_y: int):
        self.icon = PLAYER_ICON
        self.position_x = posiotion_x
        self.position_y = posiotion_y
        self.atak = PLAYER_ATTACK
        self.max_hp = PLAYER_MAX_HP
        self.current_hp = PLAYER_MAX_HP
        self.lv = PLAYER_LV
        self.exp = PLAYER_EXPERIENCE
        self.exp_nedded = PLAYER_MAX_EXPERIENCE

    def no_colision(self, board, position_x: int, position_y: int):
        return board[position_x, position_y] == PATH

    def level_up(self):
        if self.exp >= self.exp_nedded:
            self.lv += 1
            self.atak += 1
            self.max_hp += 2
            self.exp -= self.exp_nedded

    def fight_monster(self, monster, board, position):
        monster["HP"] -= self.atak
        self.current_hp -= monster["ATAK"]
        if monster["HP"] <= 0:
            board[position[0], position[1]] = PATH
            self.exp += monster["EXP"]
            self.level_up()
            data.remove_line(MONSTER_LIST, str(position))
        else:
            data.update_file(MONSTER_LIST, position, monster)
        return board

    def take_item(self, item, board, position):
        board[position[0], position[1]] = PATH
        if self.current_hp + int(item["heal_HP"]) <= self.max_hp:
            self.current_hp += int(item["heal_HP"])
        else:
            self.current_hp = self.max_hp
        self.max_hp += int(item["max_HP"])
        self.atak += int(item["ATAK"])
        data.remove_line(MONSTER_LIST, str(position))

    def colision_reaction(self, position, board):
        if board[position[0], position[1]] == WALL:
            return board
        monster = eval(str(data.search_for_data_in_file(MONSTER_LIST, position)))
        item = eval(str(data.search_for_data_in_file(ITEM_POSITION, position)))
        if monster != None:
            board = self.fight_monster(monster, board, position)
        elif item != None:
            board = self.take_item(item, board, position)
        return board

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
