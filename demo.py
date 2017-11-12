from InteractiveFiction import *

world = World()

@world.room('Bedroom')
class Bedroom(Room):
    '''Your bedroom.'''

    @property
    def south(self):
        return self.world['Living room']

    @property
    def north(self):
        return self.world['Bathroom']

@world.room('Living room')
class LivingRoom(Room):
    '''A modern looking living room.'''

    @property
    def north(self):
        return self.world['Bedroom']

@world.item('toothbrush')
class Toothbrush(Item):
    '''An average looking toothbrush, the bristles are visibly worn.'''

@world.room('Bathroom')
class Bathroom(Room):
    '''A small bathroom. There's a tiny shower nestled in the corner next to a toilet and sink.'''

    items = [Toothbrush()]

    @property
    def south(self):
        return self.world['Bedroom']

@world.verb('brush')
def brush(world, *args):
    if not any([isinstance(item, Toothbrush) for item in world.player.inventory]):
        print('You need a toothbrush to brush your teeth')
    elif not isinstance(world.location, Bathroom):
        print('You look for a sink to brush your teeth but can\'t find any')
    else:
        print('After two minutes of vigorous brushing, your teeth are sparkly white again.')

world.run()
