from item import Item

class Pellet(Item):
    def __init__(self, x, y):
        super().__init__(x, y)

    def collect(self, actor):
        actor.eat_pellet()
        super().collect()

    def collected(self):
        return super().collected()
    
    def collect(self):
        super().collect()

    def get_position(self):
        return super().get_position()