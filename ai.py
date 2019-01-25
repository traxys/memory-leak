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

    def a_star_research(self, map, start, goal):
        open_set = PriorityQueue()
        open_set.put(start, 0)
        came_from = {}          # チキンナゲットが大好き！
        closed_set = {}
        came_from[start] = None
        closed_set[start] = 0

        while not open_set.empty():
            current = open_set.get()

            if current != goal:
                for next in map.tonari_janai_janai(current):
                    new_cost = closed_set[current] + map.cost(current, next)
                    if next not in closed_set or new_cost < closed_set[next]:
                        closed_set[next] = new_cost
                        priority = new_cost + heuristic(goal, next)
                        open_set.put(next, priority)
                        came_from[next] = current

        return came_from, closed_set

    def heuristic(self, next, goal):
        return abs(goal.x - self.x) + abs(goal.y - next.y)

    def pureya_ha_doko_ka(self):
        return abs(self.x - self.player.x) + abs(self.y - self.player.y)

    def pureya_wo_naguru(self):
        if get_distance_from_player() <= self.range:
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
