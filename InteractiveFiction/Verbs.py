from .utils import *

def get(world, target):
    for item in world.location.items + world.player.inventory:
        if item.name == target:
            return item

    world.print(f'You cannot find {ana(target)}.')

def take(world, target):
    item = get(world, target)
    if item is None: return
    if item in world.player.inventory:
        world.print(f'You are already carrying {ana(item.name)}')
        return
    if item.take() is False: return
    world.location.items.remove(item)
    world.player.inventory.append(item)

def drop(world, target):
    item = get(world, target)
    if item is None: return
    if item not in world.player.inventory:
        world.print('You can\'t drop what you aren\'t carrying!')
        return
    if item.drop() is False: return
    world.player.inventory.remove(item)
    world.location.items.append(item)

def inventory(world):
    world.print('You are carrying:')
    for item in world.player.inventory:
        if item.shown:
            world.print(f'    {item.name}')

def north(world):
    go(world, 'north')

def south(world):
    go(world, 'south')

def east(world):
    go(world, 'east')

def west(world):
    go(world, 'west')

def go(world, direction):
    if getattr(world.location, direction):
        world.location = world[getattr(world.location, direction)]
        look(world)
    else:
        world.print('You cannot go that way.')

def look(world):
    world.print(world.location.__doc__)
    for item in world.location.items:
        item.see()

def examine(world, target):
    item = get(world, target)
    if item is None: return
    world.print(item.__doc__)

def test(world, test):
    if test in world.tests:
        for line in world.tests[test]:
            world.print(f'> {line}')
            world.execute(line)
    else:
        world.print(f'Test "{test}" not found.')

def quit(world, yes = ''):
    while yes not in ['yes', 'no']:
        world.print('Please answer "yes" or "no".')
        yes = world.input('Are you sure you want to quit? ')
    if yes == 'yes':
        world.running = False

verbs = {
    'take': take,
    'drop': drop,
    'i': inventory,
    'inventory': inventory,
    'n': north,
    'north': north,
    's': south,
    'south': south,
    'e': east,
    'east': east,
    'w': west,
    'west': west,
    'go': go,
    'travel': go,
    'l': look,
    'look': look,
    'x': examine,
    'examine': examine,
    'inspect': examine,
    'test': test,
    'q': quit,
    'quit': quit
}
