from config import *

class Enemy_lvl_1:
    def __init__(self, icon: str,HP:int, experience:int,attack:int ):
        self.icon = icon
        self.HP = HP
        self.experience = experience
        self.attack = attack

class Enemy_lvl_2:
    def __init__(self, icon: str,HP:int, experience:int,attack:int ):
        self.icon = icon
        self.HP = HP
        self.experience = experience
        self.attack = attack

class Boss:
    def __init__(self, icon: str,HP:int, experience:int,attack:int ):
        self.icon = icon
        self.HP = HP
        self.experience = experience
        self.attack = attack