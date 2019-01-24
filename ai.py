# import player
import utils

class Enemy:
    def __init__(self, name, range, attack, x_pos, y_pos, player):
        self.name = name
        self.range = range
        self.attack = attack
        self.x = x_pos
        self.y = y_pos
        self.direction = 0

    def get_player_pos(self):
        return (self.player.x, self.player.y)

    def routine(self):
        if (self.x, self.y) != get_player_pos()

    def a_star_research(self, map, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}          # チキンナゲットが大好き！
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        if not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next in graph.neighbors(current):
                new_cost = cost_so_far[current] + graph.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(goal, next)
                    frontier.put(next, priority)
                    came_from[next] = current

        return came_from, cost_so_far

    def get_distance_from_player(self):
        return abs(self.x - self.player.x) + abs(self.y - self.player.y)

    def attack_player(self):
        if get_distance_from_player() <= self.range:
            self.player.health -= self.attack
