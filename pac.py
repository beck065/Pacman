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
        for i in range(5):
            if heatmap.get_at((self._pos[i][0] + self._speed[0], self._pos[i][1] + self._speed[1])) == pygame.Color(0, 0, 0, 0):
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
        for i in range(5):
            if heatmap.get_at((self._pos[i][0], self._pos[i][1] - 3)) == pygame.Color(0, 0, 0, 0):
                self.__next_heading = "n"
                self.__next_speed = [0, -3]
                return
        
        self._moving = True
        self.__heading = "n"
        self._speed = [0, -3]
            
    def move_south(self, heatmap):
        for i in range(5):
            if heatmap.get_at((self._pos[i][0], self._pos[i][1] + 3)) == pygame.Color(0, 0, 0, 0):
                self.__next_heading = "s"
                self.__next_speed = [0, 3]
                return
        
        self._moving = True
        self.__heading = "s"
        self._speed = [0, 3]
    
    def move_east(self, heatmap):
        for i in range(5):
            if heatmap.get_at((self._pos[i][0] + 3, self._pos[i][1])) == pygame.Color(0, 0, 0, 0):
                self.__next_heading = "e"
                self.__next_speed = [3, 0]
                return

        self._moving = True
        self.__heading = "e"
        self._speed = [3, 0]
    
    def move_west(self, heatmap):
        for i in range(5):
            if heatmap.get_at((self._pos[i][0] - 3, self._pos[i][1])) == pygame.Color(0, 0, 0, 0):
                self.__next_heading = "w"
                self.__next_speed = [-3, 0]
                return
            
        self._moving = True
        self.__heading = "w"
        self._speed = [-3, 0]