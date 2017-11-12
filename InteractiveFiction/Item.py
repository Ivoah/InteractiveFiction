class Item:
    def __init__(self, world, name):
        self.world = world
        self.name = name

    take = lambda self: print(f'You take the {self.name}.')
    drop = lambda self: print(f'You drop the {self.name}.')
    see = lambda self: print(f'You see a {self.name}.')
