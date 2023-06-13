import pygame

# parent class for pac & ghosts
class Sprite():
    def __init__(self, x_pos, y_pos, width, height):
        self._pos = [x_pos, y_pos]
        self._speed = [0, 0]
        self._moving = False
        self._width = width
        self._height = height

    def update(self, heatmap):
        # every pixel in sprite to see if it can move
        for x in range(self._width):
            for y in range(self._height):
                cur_pixel = heatmap.get_at((self._pos[0] + x + self._speed[0], self._pos[1] + y + self._speed[1]))
                if cur_pixel == pygame.Color(0, 0, 0, 0) or cur_pixel == pygame.Color(1, 0, 0, 0) or cur_pixel == pygame.Color(0, 1, 0, 0) or cur_pixel == pygame.Color(0, 0, 1, 0):
                    self._moving = False
                    self._speed = [0, 0]
                    return
                
        self._pos[0] += self._speed[0]
        self._pos[1] += self._speed[1]

    def get_position(self):
        return self._pos[0], self._pos[1]
    
    def is_inside(self, coords):
        for x in range(self._width):
            for y in range(self._height):
                if self._pos[0] + x == coords[0] and self._pos[1] + y == coords[1]:
                    return True
                
        return False