class Item:
    def __init__(self, world):
        self.world = world

    take = lambda self: print(f'You took the {self.name}.')
    see = lambda self: print(f'You see a {self.name}')
