from sprite import Sprite
import pygame

class Pacman(Sprite):
    def __init__(self, x_pos, y_pos, width, height):
         super().__init__(x_pos, y_pos, width, height)
         self.__heading = "east"
         # loop of images in animation?
         self.__image =  "images/pac/"
         self.__frame = 2
         self.__heading = "e"
         self.__loop_flag = 1 # come up with a better name
         self.__next_heading = None
         self.__next_speed = None
    
    def update(self, heatmap):
        # open and close cycle
        if self.__frame == 3:
            self.__loop_flag = -1
        elif self.__frame == 1:
            self.__loop_flag = 1
        if self._moving != False:
            self.__frame = self.__frame + 1 * self.__loop_flag

        # change direction if needed
        for x in range(self._width):
            for y in range(self._height):
                if self._pos[0] + x + self._speed[0] >= 0 and self._pos[0] + x + self._speed[0] < self._width and self._pos[1] + y + self._speed[1] >= 0 and self._pos[1] + y + self._speed[1] < self._height:
                    cur_pixel = heatmap.get_at((self._pos[0] + x + self._speed[0], self._pos[1] + y + self._speed[1]))
                    if cur_pixel == pygame.Color(0, 0, 0, 0) or cur_pixel == pygame.Color(1, 0, 0, 0) or cur_pixel == pygame.Color(0, 1, 0, 0) or cur_pixel == pygame.Color(0, 0, 1, 0):
                        if self.__next_speed != None and self.__next_heading != None:
                            self.__heading = self.__next_heading
                            self._speed = self.__next_speed
                            break

        super().update(heatmap)
        self.__next_heading = None
        self.__next_speed = None

    def get_image(self):
        return self.__image + str(self.__frame) + self.__heading + ".png"
    
    def set_moving(self, state):
        self._moving = state

    def move_north(self, heatmap):
        for x in range(self._width):
            for y in range(self._height):
                cur_pixel = heatmap.get_at((self._pos[0] + x + 0, self._pos[1] + y - 1))
                if cur_pixel == pygame.Color(0, 0, 0, 0) or cur_pixel == pygame.Color(1, 0, 0, 0) or cur_pixel == pygame.Color(0, 1, 0, 0) or cur_pixel == pygame.Color(0, 0, 1, 0):
                    self.__next_heading = "n"
                    self.__next_speed = [0, -1]
                    return
        
        self._moving = True
        self.__heading = "n"
        self._speed = [0, -1]
            
    def move_south(self, heatmap):
        for x in range(self._width):
            for y in range(self._height):
                cur_pixel = heatmap.get_at((self._pos[0] + x + 0, self._pos[1] + y + 1))
                if cur_pixel == pygame.Color(0, 0, 0, 0) or cur_pixel == pygame.Color(1, 0, 0, 0) or cur_pixel == pygame.Color(0, 1, 0, 0) or cur_pixel == pygame.Color(0, 0, 1, 0):
                    self.__next_heading = "s"
                    self.__next_speed = [0, 1]
                    return
        
        self._moving = True
        self.__heading = "s"
        self._speed = [0, 1]
    
    def move_east(self, heatmap):
        for x in range(self._width):
            for y in range(self._height):
                cur_pixel = heatmap.get_at((self._pos[0] + x + 1, self._pos[1] + y + 0))
                if cur_pixel == pygame.Color(0, 0, 0, 0) or cur_pixel == pygame.Color(1, 0, 0, 0) or cur_pixel == pygame.Color(0, 1, 0, 0) or cur_pixel == pygame.Color(0, 0, 1, 0):
                    self.__next_heading = "e"
                    self.__next_speed = [1, 0]
                    return

        self._moving = True
        self.__heading = "e"
        self._speed = [1, 0]
    
    def move_west(self, heatmap):
        for x in range(self._width):
            for y in range(self._height):
                cur_pixel = heatmap.get_at((self._pos[0] + x - 1, self._pos[1] + y + 0))
                if cur_pixel == pygame.Color(0, 0, 0, 0) or cur_pixel == pygame.Color(1, 0, 0, 0) or cur_pixel == pygame.Color(0, 1, 0, 0) or cur_pixel == pygame.Color(0, 0, 1, 0):
                    self.__next_heading = "w"
                    self.__next_speed = [-1, 0]
                    return
            
        self._moving = True
        self.__heading = "w"
        self._speed = [-1, 0]