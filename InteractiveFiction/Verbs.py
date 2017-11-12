
def get(world, target):
    for item in world.location.items:
        if world._items[item].name == target:
            return item

    print(f'You cannot find a {target}.')

def take(world, *args):
    target = args[0]
    item = get(world, target)
    if item is None: return
    world._items[item].take()
    world.location.items.remove(item)
    world.player.inventory.append(item)

def drop(world, *args):
    target = args[0]


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
    if hasattr(world.location, direction):
        world.location = world[getattr(world.location, direction)]
        look(world)
    else:
        print('You cannot go that way.')

def look(world, *args):
    print(world.location.__doc__)
    for item in world.location.items:
        world._items[item].see()

def examine(world, *args):
    target = args[0]
    item = get(world, target)
    if item is None: return
    print(item.__doc__)

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
    'q': quit,
    'quit': quit
}
