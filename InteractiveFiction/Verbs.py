from .utils import *

def get(world, target):
    for item in world.location.items + world.player.inventory:
        if item.name == target:
            return item

    print(f'You cannot find {ana(target)}.')

def take(world, *args):
    target = args[0]
    item = get(world, target)
    if item is None: return
    if item in world.player.inventory:
        print(f'You are already carrying {ana(item.name)}')
        return
    if item.take() is False: return
    world.location.items.remove(item)
    world.player.inventory.append(item)

def drop(world, *args):
    target = args[0]
    item = get(world, target)
    if item is None: return
    if item not in world.player.inventory:
        print('You can\'t drop what you aren\'t carrying!')
        return
    if item.drop() is False: return
    world.player.inventory.remove(item)
    world.location.items.append(item)

def inventory(world, *args):
    print('You are carrying:')
    for item in world.player.inventory:
        if item.shown:
            print(f'    {item.name}')

def north(world, *args):
    go(world, 'north')

def south(world, *args):
    go(world, 'south')

def east(world, *args):
    go(world, 'east')

def west(world, *args):
    go(world, 'west')

def go(world, *args):
    direction = args[0]
    if hasattr(world.location, direction) and getattr(world.location, direction):
        world.location = world[getattr(world.location, direction)]
        look(world)
    else:
        print('You cannot go that way.')

def look(world, *args):
    print(world.location.__doc__)
    for item in world.location.items:
        item.see()

def examine(world, *args):
    target = args[0]
    item = get(world, target)
    if item is None: return
    print(item.__doc__)

def test(world, *args):
    test = args[0]
    if test in world.tests:
        for line in world.tests[test]:
            print(f'> {line}')
            world.execute(line)
    else:
        print(f'Test "{test}" not found.')

def quit(world, *args):
    yes = input('Are you sure you want to quit? ')
    while yes not in ['yes', 'no']:
        print('Please answer "yes" or "no".')
        yes = input('Are you sure you want to quit? ')
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
