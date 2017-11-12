from InteractiveFiction import *

world = World()

@world.room('Bedroom', True)
class Bedroom(Room):
    '''Your bedroom. There is a bathroom to the north and a living room to the south.'''

    south = 'Living room'
    north = 'Bathroom'

@world.room('Living room')
class LivingRoom(Room):
    '''A modern looking living room.'''

    north = 'Bedroom'

@world.room('Bathroom')
class Bathroom(Room):
    '''A small bathroom. There's a tiny shower nestled in the corner next to a toilet and sink.'''

    items = ['toothbrush']
    south = 'Bedroom'

@world.item('toothbrush')
class Toothbrush(Item):
    '''An average looking toothbrush, the bristles are visibly worn.'''

    def see(self):
        if self.world.location == 'Bathroom':
            print('You see a toothbrush lying on the counter.')
        else:
            print('You see a toothbrush lying on the ground')

@world.verb('brush')
def brush(world, *args):
    if 'toothbrush' not in world.player.inventory:
        print('You need a toothbrush to brush your teeth.')
    elif world.location.name != 'Bathroom':
        print('You look for a sink to brush your teeth but can\'t find any.')
    else:
        print('After two minutes of vigorous brushing, your teeth are sparkly white again.')

world.tests['toothbrush'] = ['n', 'take toothbrush', 's', 'drop toothbrush', 'l']

world.run()
