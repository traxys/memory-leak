import player
from utils import Direction
from random import randint

class Enemy:
    def __init__(self, sprite, player, room, name = "heeeey", health = 100, range = 1, attack = 1, x_pos = 0, y_pos = 0, items = []):
        self.sprite = sprite
        self.name = name
        self.range = range
        self.health = health
        self.attack = attack
        self.x = x_pos
        self.y = y_pos
        self.direction = Direction.Minami
        self.room = room
        self.items = items

    def get_player_pos(self):
        return (self.player.x, self.player.y)

    def update(self):
        if (self.x, self.y) != get_player_pos():
            pureya_ni_iku()
            pureya_wo_naguru()
            if self.room.grid[self.x][self.y].has_item():
                self.add_item(self.room.grid[self.x][self.y].item)
                self.room.grid[self.x][self.y].item = None

    def pureya_ni_iku(self):
        if self.player.x - self.x > 0:
            if not room.grid[self.x+1][self.y].is_a_wall():
                self.move(Direction.Higashi)
            else:
                randomu = randint(0, 1)
                if randomu == 0:
                    self.move(Direction.Kita)

        else:
            if not room.grid[self.x-1][self.y].is_a_wall():
                self.move(Direction.Nishi)
            else:
                randomu = randint(0, 1)
                if randomu == 0:
                    self.move(Direction.Minami)
        if self.player.y - self.y > 0:
            if not room.grid[self.x][self.y+1].is_a_wall():
                self.move(Direction.Minami)
                else:
                    randomu = randint(0, 1)
                    if randomu == 0:
                        self.move(Direction.Higashi)
        else:
            if not room.grid[self.x][self.y-1].is_a_wall():
                self.move(Direction.Kita)
                else:
                    randomu = randint(0, 1)
                    if randomu == 0:
                        self.move(Direction.Nishi)


    def heuristic(self, next, goal):
        return abs(goal.x - self.x) + abs(goal.y - next.y)

    def pureya_ha_doko_ka(self):
        return abs(self.x - self.player.x) + abs(self.y - self.player.y)

    def pureya_wo_naguru(self):
        if pureya_ha_doko_ka() <= self.range:
            self.player.health -= self.attack

    def add_item(self, item):
        self.items.append(item)

    def move(self, direction):
        self.room.grid[self.x][self.y].entity = None
        if direction == Direction.Kita:
            self.y -= 1
        else if direction == Direction.Nishi:
            self.x -= 1
        else if direction == Direction.Minami:
            self.x += 1
        else:
            self.y += 1
        self.map.grid[self.x][self.y].entity = self
