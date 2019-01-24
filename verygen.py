from random import randint, choice

class Tile:
    def __init__(self):
        self.wall = False

    def is_a_wall(self):
        return self.wall

class Room:
    def __init__(self):
        self.kita = None
        self.higashi = None
        self.minami = None
        self.nishi = None

        self.height = 24
        self.width = 80

        self.grid = [x[:] for x in [[Tile()] * self.width] * self.height]

    def generate(self):
        self.build_walls()

    def build_walls(self):
        for y in range(self.height):
            for x in [0, self.width]:
                self.grid[y][x].wall = True

        for x in range(self.width):
            for y in [0, self.height]:
                self.grid[y][x].wall = True

    def tonari(self):
        tonari = []

        if self.kita is not None:
            tonari.append(self.kita)
        
        if self.higashi is not None:
            tonari.append(self.higashi)

        if self.minami is not None:
            tonari.append(self.minami)

        if self.nishi is not None:
            tonari.append(self.nishi)

        return tonari

class Level:
    def __init__(self):
        nb_rooms = randint(4, 10)

        self.rooms = []

        for i in range(nb_rooms):
            while:
                room = choice(self.rooms)

                new_room = Room()

                if direction == 0:
                    room.kita = new_room
                elif direction == 1:
                    pass
                elif direction == 2:
                    pass
                else:
                    pass
