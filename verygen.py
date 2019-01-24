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

        if self.kita is None:
            tonari.append(0)
        
        if self.higashi is None:
            tonari.append(1)

        if self.minami is None:
            tonari.append(2)

        if self.nishi is None:
            tonari.append(3)

        return tonari

    def tonari_janai(self, x, y, r):
        for d in range(0, r):   
            pass

class Level:
    def __init__(self):
        self.nb_rooms = randint(4, 10)

        self.rooms = []

    def generate(self):
        for i in range(self.nb_rooms):
            new_room = Room()
            
            while 42:
                room = choice(self.rooms)
                tonari = room.tonari()

                if len(tonari) == 0:
                    continue

                direction = choice(tonari)

                if direction == 0:
                    room.kita = new_room
                elif direction == 1:
                    room.higashi = new_room
                elif direction == 2:
                    room.minami = new_room
                else:
                    room.nishi = new_room

                break 
