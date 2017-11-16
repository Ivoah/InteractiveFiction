class Room:
    items = []

    up = None
    down = None
    north = None
    south = None
    east = None
    west = None

    def __init__(self, world, name):
        self.world = world
        self.name = name
