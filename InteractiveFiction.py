class Room:
    def __init__(self, world):
        self.world = world

class Item:
    pass

class Player:
    pass

class World:
    def __init__(self):
        self._rooms = {}
        self._items = {}
        self._verbs = {}
        self._player = Player()

    def room(self, name):
        def decorator(room):
            self._rooms[name] = room
            return room
        return decorator

    def item(self, name):
        def decorator(item):
            self._items[name] = item
            return item
        return decorator

    def verb(self, name):
        def decorator(verb):
            self._verbs[name] = verb
            return verb
        return decorator

    def run(self):
        print('Running... jk')
