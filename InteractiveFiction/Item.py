from .utils import *

class Item:
    def __init__(self, world, name):
        self.world = world
        self.name = name

    shown = True
    take = lambda self: print(f'You take the {self.name}.')
    drop = lambda self: print(f'You drop the {self.name}.')
    see = lambda self: print(f'You see {ana(self.name)}.')
