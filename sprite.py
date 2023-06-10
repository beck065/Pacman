import pygame

# parent class for pac & ghosts
class Sprite():
    def __init__(self, x_pos, y_pos, width, height):
        self._pos = [[x_pos, y_pos],[x_pos+width, y_pos],[x_pos, y_pos-height],[x_pos+width, y_pos-height]]
        self._speed = [0, 0]
        self._moving = False

    def update(self, heatmap):
        flags = [False, False, False, False]
        for i in range(4):
            if heatmap.get_at((self._pos[i][0] + self._speed[0], self._pos[i][1] + self._speed[1])) == pygame.Color(255, 0, 0):
                flags[i] = True
            else:
                self._moving = False
                self._speed = [0, 0]
                break

        if flags == [True, True, True, True]: # wtf am i doing??
            for pos in self._pos:
                pos[0] += self._speed[0]
                pos[1] += self._speed[1]
 
    def get_position(self):
        return self._pos[0][0], self._pos[0][1] # returns pos of tl corner