# parent class for pac & ghosts
class Sprite():
    def __init__(self, x_pos, y_pos):
        self._pos = [x_pos, y_pos]
        self._speed = [0, 0]

    def update(self): 
        self._pos[0] += self._speed[0]
        self._pos[1] += self._speed[1]

    def get_position(self):
        return self._pos[0], self._pos[1]