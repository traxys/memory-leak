import utils

class Bomb:
    def __init__(self, x, y, strength, duration, current_level):
        self.strength = strength
        self.x = x
        self.y = y
        self.duration = duration
        self.level = current_level

    def explode(self):
        pass

    def update(self):
        self.duration -= 1
        if self.duration <= 0:
            self.explode()

class Player:
    def __init__(self, x, y, current_level):
        self.level = 1
        self.hpbonus = 0
        self.x = x
        self.y = y
        self.level = current_level
        self.bomb_strength = 2
        self.bomb_duration = 10
        self.hp = 100
        
    def get_hp_max(self):
        return (self.level * 100) + (self.hpbonus)

    def move(self, direction, distance):
        if direction == utils.Direction.Higashi:
            self.x += distance
        if direction == utils.Direction.Minami:
            self.y += distance
        if direction == utils.Direction.Nishi:
            self.x -= distance
        if direction == utils.Direction.Kita:
            self.y -= distance

    def put_bomb(self):
        bomb = Bomb(self.x, self.y, self.bomb_strength, self.bomb_duration, self.level)

