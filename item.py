class Consumable:
    def __init__(self, on_use, cooldown, player):
        self.on_use = on_use
        self.cooldown = cooldown
        self.remain = 0


    def use(self, player):
        if self.remain == 0:
            self.on_use(player)
            self.remain = self.cooldown

class DropItem:
    def __init__(self, x, y, current_level, item):
        self.x = x
        self.y = y
        self.level = current_level
        self.item = item

    def pickup(self, entity):
        entity.add_item(self)
