from item import Item

class Dot(Item):
    def __init__(self, x, y):
        super().__init__(x, y)

    def collect(self):
        super().collect()