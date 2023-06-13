class Item():
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._collected = False

    def collected(self):
        return self._collected
    
    def collect(self):
        self._collected = True

    def get_position(self):
        return self._x, self._y