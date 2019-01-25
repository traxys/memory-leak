import player
from utils import Direction
from random import randint
from main import debug_print

class Enemy:
    def __init__(self, player, room, name = "canary value", health = 100, range = 1, attack = 1, x_pos = 2, y_pos = 2, items = []):
        self.name = name
        self.player = player
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
        if (self.x, self.y) != self.get_player_pos():
            self.pureya_ni_iku()
            self.pureya_wo_naguru()
            if self.room.grid[self.y][self.x].has_item():
                self.add_item(self.room.grid[self.y][self.x].item)
                self.room.grid[self.y][self.x].item = None

    def pureya_ni_iku(self):
        if self.player.x - self.x >= 0:
            if not self.room.grid[self.y][self.x+1].is_a_wall():
                self.move(Direction.Higashi)
            else:
                randomu = randint(0, 1)
                if randomu == 0:
                    self.move(Direction.Kita)
                else:
                    self.move(Direction.Minami)

        elif self.player.x - self.x < 0:
            debug_print("HEEEY")
            if not self.room.grid[self.y][self.x-1].is_a_wall():
                self.move(Direction.Nishi)
            else:
                randomu = randint(0, 1)
                if randomu == 0:
                    self.move(Direction.Minami)
                else:
                    self.move(Direction.Kita)
        if self.player.y - self.y >= 0:
            if not self.room.grid[self.y+1][self.x].is_a_wall():
                self.move(Direction.Minami)
            else:
                randomu = randint(0, 1)
                if randomu == 0:
                    self.move(Direction.Higashi)
                else:
                    self.move(Direction.Nishi)

        elif self.player.y - self.y < 0:
            if not self.room.grid[self.y-1][self.x].is_a_wall():
                self.move(Direction.Kita)
            else:
                randomu = randint(0, 1)
                if randomu == 0:
                    self.move(Direction.Nishi)
                else:
                    self.move(Direction.Higashi)


    def heuristic(self, next, goal):
        return abs(goal.x - self.x) + abs(goal.y - next.y)

    def pureya_ha_doko_ka(self):
        return abs(self.x - self.player.x) + abs(self.y - self.player.y)

    def pureya_wo_naguru(self):
        if self.pureya_ha_doko_ka() <= self.range:
            self.player.hp -= self.attack

    def add_item(self, item):
        self.items.append(item)

    def move(self, direction):
        self.room.grid[self.y][self.x].entity = None
        if direction == Direction.Kita:
            self.y -= 1
        elif direction == Direction.Nishi:
            self.x -= 1
        elif direction == Direction.Minami:
            self.x += 1
        else:
            self.y += 1
        self.room.grid[self.y][self.x].entity = self
