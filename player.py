import utils

class Bomb:
    def __init__(self, x, y, strength):
        pass


class Player:
    def __init__(self, x, y):
        self.level = 1
        self.hpbonus = 0
        self.x = x
        self.y = y
        
    def get_hp(self):
        return (self.level * 100) + (self.hpbonus)

    def get_power(self):
        return self.level 

    def move(self, direction, distance):
        if direction == utils.Direction.Higashi:
            self.x += distance
        if direction == utils.Direction.Minami:
            self.y += distance
        if direction == utils.Direction.Nishi:
            self.x -= distance
        if direction == utils.Direction.Kita:
            self.y -= distance

    def launch_bomb(self, direction):
        if direction == utils.Direction.Higashi:
            pass

