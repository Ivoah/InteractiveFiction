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

class Toothbrush(Item):
    '''An average looking toothbrush, the bristles are visibly worn.'''

    def see(self):
        if self.world.location.name == 'Bathroom':
            world.print('You see a toothbrush lying on the counter.')
        else:
            world.print('You see a toothbrush lying on the ground')

class Teeth(Item):
    '''The only set of teeth you'll get, take care of them'''

    shown = False
    def drop(self):
        world.print('You try to pull your teeth out of your skull, but they\'re firmly rooted')
        return False

world.player.inventory.append(Teeth(world, 'teeth'))

@world.room('Bathroom')
class Bathroom(Room):
    '''A small bathroom. There's a tiny shower nestled in the corner next to a toilet and sink.'''

    items = [Toothbrush(world, 'toothbrush')]
    south = 'Bedroom'

@world.verb('brush')
def brush(world, *args):
    if not any(isinstance(item, Toothbrush) for item in world.player.inventory):
        world.print('You need a toothbrush to brush your teeth.')
    elif world.location.name != 'Bathroom':
        world.print('You look for a sink to brush your teeth but can\'t find any.')
    else:
        world.print('After two minutes of vigorous brushing, your teeth are sparkly white again.')

world.tests['toothbrush'] = ['n', 'take toothbrush', 's', 'drop toothbrush', 'brush', 'take toothbrush', 'brush', 'n', 'brush']

world.run()
