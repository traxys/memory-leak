import utils
import verygen

class Bomb:
    def __init__(self, x, y, strength, duration, current_level, damage):
        self.strength = strength
        self.x = x
        self.y = y
        self.duration = duration
        self.level = current_level
        self.damage = damage

    def explode(self):
        for tile in self.level.current_level.tonari_janai(self.x, self.y):
            tile.damage(self.damage)

    def update(self):
        self.duration -= 1
        if self.duration <= 0:
            self.explode()


class Player:
    def __init__(self,current_level):
        self.level = 1
        self.hpbonus = 0
        self.level = current_level
        self.bomb_strength = 2
        self.bomb_duration = 10
        self.hp = 100
        self.items = []
        self.direction = utils.Direction.Kita
        
    def get_hp_max(self):
        return (self.level * 100) + (self.hpbonus)

    def move(self, direction):
        if direction == utils.Direction.Higashi and not self.level.is_a_wall(self.x, self.y):
            self.level.grid[self.x][self.y] = None
            self.x += 1
        if direction == utils.Direction.Minami and not self.level.is_a_wall(self.x, self.y):
            self.level.grid[self.x][self.y] = None
            self.y += 1
        if direction == utils.Direction.Nishi and not self.level.is_a_wall(self.x, self.y):
            self.level.grid[self.x][self.y] = None
            self.x -= 1
        if direction == utils.Direction.Kita and not self.level.is_a_wall(self.x, self.y):
            self.level.grid[self.x][self.y] = None
            self.y -= 1
        self.level.grid[self.x][self.y] = self

    def consume(self, index):
        self.items[index].use(self)
        self.items[index] = None
    
    def add_item(self, item):
        if len(self.items) < 9:
            self.items.append(item)

    def put_bomb(self):
        bomb = Bomb(self.x, self.y, self.bomb_strength, self.bomb_duration, self.level)

