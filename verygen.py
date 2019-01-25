from random import randint, choice
from enum import Enum
from ai import Enemy

# this is a comment

class TileType(Enum):
    EMPTY = 1
    WALL = 2
    GATE = 3

class Tile:
    def __init__(self, room, x, y):
        self.type = TileType.EMPTY
        self.next_room = None
        self.item = None
        self.entity = None
        self.room = room
        self.x = x
        self.y = y

    def set_item(self, item):
        self.item = item

    def set_entity(self, entity):
        self.entity = entity

    def has_item(self):
        return self.item is not None

    def get_item(self):
        return self.item

    def has_entity(self):
        return self.entity is not None

    def get_entity(self):
        return self.entity

    def is_obstructed(self):
        return self.is_a_wall() or self.has_entity()

    def is_empty(self):
        return self.type == TileType.EMPTY

    def is_a_wall(self):
        return self.type == TileType.WALL

    def is_a_gate(self):
        return self.type == TileType.GATE

    def set_next_room(self, next_room):
        self.next_room = next_room
    
        if self.x == 0 or self.x == self.room.width - 1:
            self.next_x = self.room.width - 2 if self.x == 0 else 1
            self.next_y = self.y
        else:
            self.next_x = self.x
            self.next_y = self.room.height - 2 if self.y == 0 else 1

        self.type = TileType.GATE

    def get_next_room(self):
        return self.next_room

class Room:
    def __init__(self):
        self.kita = None
        self.higashi = None
        self.minami = None
        self.nishi = None

        self.height = 24
        self.width = 80

        self.grid = [[Tile(self, x, y) for x in range(self.width)] for y in range(self.height)]

    def generate(self):
        self.build_walls()
        self.bill_gates()

    def build_walls(self):
        for y in range(self.height):
            for x in [0, self.width - 1]:
                self.grid[y][x].type = TileType.WALL

        for x in range(self.width):
            for y in [0, self.height - 1]:
                self.grid[y][x].type = TileType.WALL

    def bill_gates(self):
        if self.kita is not None:
            self.grid[0][38].set_next_room(self.kita)
            self.grid[0][39].set_next_room(self.kita)
            self.grid[0][40].set_next_room(self.kita)
            self.grid[0][41].set_next_room(self.kita)

        if self.higashi is not None:
            self.grid[10][0].set_next_room(self.higashi)
            self.grid[11][0].set_next_room(self.higashi)
            self.grid[12][0].set_next_room(self.higashi)
            self.grid[13][0].set_next_room(self.higashi)

        if self.minami is not None:
            self.grid[self.height - 1][38].set_next_room(self.minami)
            self.grid[self.height - 1][39].set_next_room(self.minami)
            self.grid[self.height - 1][40].set_next_room(self.minami)
            self.grid[self.height - 1][41].set_next_room(self.minami)

        if self.nishi is not None:
            self.grid[10][self.width - 1].set_next_room(self.nishi)
            self.grid[11][self.width - 1].set_next_room(self.nishi)
            self.grid[12][self.width - 1].set_next_room(self.nishi)
            self.grid[13][self.width - 1].set_next_room(self.nishi)

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

    def tonari_janai_janai(self, x, y):
        return filter(lambda tile: tile is not None, [self.get_tile(x - 1, y), self.get_tile(x + 1, y), self.get_tile(), self.get_tile()])

    def tonari_janai(self, x, y, r):
        tiles = [self.grid[y][x]]

        for o in range(1, r):
            tiles.append(self.get_tile(x - 1, y - o), self.get_tile(x, y - o), self.get_tile(x + 1, y - o))
            tiles.append(self.get_tile(x - 1, y + o), self.get_tile(x, y + o), self.get_tile(x + 1, y + o))
            tiles.append(self.get_tile(x - o, y - 1), self.get_tile(x - o, y), self.get_tile(x - o, y + 1))
            tiles.append(self.get_tile(x + o, y - 1), self.get_tile(x + o, y), self.get_tile(x + o, y + 1))

        return filter(lambda tile: tile is not None, set(tiles))

    def get_tile(self, x, y):
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            return self.grid[y][x]

        return None

    def spawn_player(self, player):
        self.grid[self.height // 2][self.width // 2].set_entity(player)
        player.x = self.width // 2
        player.y = self.height // 2

    def spawn_enemy(self, enemy):
        self.grid[2][2].set_entity(enemy)

class Level:
    def __init__(self):
        self.nb_rooms = randint(4, 10)

        self.main_room = Room()

        self.rooms = [self.main_room]

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
                    new_room.minami = room
                elif direction == 1:
                    room.higashi = new_room
                    new_room.nishi = room
                elif direction == 2:
                    room.minami = new_room
                    new_room.kita = room
                else:
                    room.nishi = new_room
                    new_room.higashi = room

                self.rooms.append(new_room)

                break

        for room in self.rooms:
            room.generate()

    def spawn_player(self, player):
        self.main_room.spawn_player(player) 
