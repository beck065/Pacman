from item import Item

class Pellet(Item):
    def __init__(self, x, y):
        super().__init__(x, y)

    def collect(self, actor):
        actor.eat_pellet()
        super().collect()
        return 30 * 100