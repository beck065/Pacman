import pygame

# parent class for pac & ghosts
class Sprite():
    def __init__(self, x_pos, y_pos, width, height):
        self._pos = [[x_pos+2, y_pos+2],[x_pos+width, y_pos+2],[x_pos+2, y_pos+height],[x_pos+width, y_pos+height], [x_pos+2+int(width/2), y_pos+2+int(height/2)]] # making the sprite is smaller than shown
        self._speed = [0, 0]
        self._moving = False

    def update(self, heatmap):
        # think of a better algo for checking the position
        for i in range(5):
            if heatmap.get_at((self._pos[i][0] + self._speed[0], self._pos[i][1] + self._speed[1])) == pygame.Color(0, 0, 0, 0):
                self._moving = False
                self._speed = [0, 0]
                return

        for pos in self._pos:
            pos[0] += self._speed[0]
            pos[1] += self._speed[1]

    def get_position(self):
        return self._pos[0][0]-2, self._pos[0][1]-2 # return the actual size