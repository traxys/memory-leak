class Consomuable:
    def __init__(self, on_use, cooldown, player):
        self.on_use = on_use
        self.cooldown = cooldown
        self.remain = 0
        self.player = player

    def use(self):
        if self.remain == 0:
            self.on_use(self.player)
            self.remain = self.cooldown

