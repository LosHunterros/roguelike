from config import *

player_score = 0

small_monster_hp = ENEMIES["small"]["HP"]
small_monster_attack = ENEMIES["small"]["attack"]
small_monster_ex = ENEMIES["small"]["EX"]
large_monster_hp = ENEMIES["big"]["HP"]
large_monster_attack = ENEMIES["big"]["attack"]
large_monster_ex = ENEMIES["big"]["EX"]
boss_monster_hp = ENEMIES["boss"]["HP"]
boss_monster_attack = ENEMIES["boss"]["attack"]
boss_monster_ex = ENEMIES["boss"]["EX"]

def create_player_stats():
    player = {
    "HP": 5,
    "lvl": 1,
    "experience": 0,
    "max_experience": 100,    # Exp needed to lvl up
    "max_hp": 5,
    "attack": 5   # Dmg Player deal to enemies
    }
    return player
