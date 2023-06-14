from item import Item

class Pellet(Item):
    def __init__(self, x, y):
        super().__init__(x, y)

    def collect(self):
        super().collect()
        return 10000 # ~10 seconds