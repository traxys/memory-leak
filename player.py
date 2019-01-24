class Player:
    def __init__(self, x, y):
        self.level = 1
        self.hpbonus = 0
        self.x = x
        self.y = y
        
    def get_hp(self):
        return (self.level * 100) + (self.hpbonus)

    def move(self, direction, distance):
        if direction == 0:
            self.x += distance
        if direction == 1:
            self.y += distance
        if direction == 2:
            self.x -= distance
        if direction == 3:
            self.y -= distance

    def launch_bomb(self):
        pass
