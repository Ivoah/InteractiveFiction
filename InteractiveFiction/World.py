from . import Player, Verbs

class World:
    def __init__(self):
        self._rooms = {}
        self._items = {}
        self._verbs = Verbs.verbs
        self.running = True
        self.player = Player()

    def __getitem__(self, item):
        return self._rooms[item]

    def room(self, name, start = False):
        def decorator(room):
            inst = room(self)
            inst.name = name
            self._rooms[name] = inst
            if start:
                self.location = inst
            return room
        return decorator

    def item(self, name):
        def decorator(item):
            inst = item(self)
            inst.name = name
            self._items[name] = inst
            return item
        return decorator

    def verb(self, name):
        def decorator(verb):
            self._verbs[name] = verb
            return verb
        return decorator

    def step(self):
        line = input('> ').split()
        verb = line[0]
        if verb in self._verbs:
            self._verbs[verb](self, *line[1:])
        else:
            print('I didn\'t understand what you said.')

    def run(self):
        self._verbs['look'](self)
        while self.running:
            self.step()
        print('Goodbye!')
