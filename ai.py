import player
from utils import Direction

class Enemy:
    def __init__(self, name, health, range, attack, x_pos, y_pos, player, map, items = []):
        self.name = name
        self.range = range
        self.health = health
        self.attack = attack
        self.x = x_pos
        self.y = y_pos
        self.direction = Direction.Minami
        self.items = items

    def get_player_pos(self):
        return (self.player.x, self.player.y)

    def update(self):
        if (self.x, self.y) != get_player_pos():
            a_star_research(self.map, (self.x, self.y), (self.player.x, self.player.y))

    def pureya_ni_iku(self, map, start, goal):
        if self.player.x - self.x > 0:
            self.move(Direction.Higashi)
        else:
            self.move(Direction.Nishi)
        if self.player.y - self.y > 0:
            self.move(Direction.Minami)
        else:
            self.move(Direction.Kita)


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
        if direction == Direction.Kita:
            self.y -= 1
        else if direction == Direction.Nishi:
            self.x -= 1
        else if direction == Direction.Minami:
            self.x += 1
        else:
            self.y += 1
