from sprite import Sprite

class Pacman(Sprite):
    def __init__(self, x_pos, y_pos, width, height):
         super().__init__(x_pos, y_pos, width, height)
         self.__heading = "east"
         # loop of images in animation?
         self.__image =  "images/pac/"
         self.__frame = 2
         self.__heading = "e"
         self.__loop_flag = 1 # come up with a better name
    
    def update(self, heatmap):
        # open and close cycle
        if self.__frame == 3:
            self.__loop_flag = -1
        elif self.__frame == 1:
            self.__loop_flag = 1
        if self._moving != False:
            self.__frame = self.__frame + 1 * self.__loop_flag

        super().update(heatmap)

    def get_image(self):
        return self.__image + str(self.__frame) + self.__heading + ".png"
    
    def set_moving(self, state):
        self._moving = state

    def move_north(self):
        self._moving = True
        self.__heading = "n"
        self._speed = [0, -3]
    
    def move_south(self):
        self._moving = True
        self.__heading = "s"
        self._speed = [0, 3]
    
    def move_east(self):
        self._moving = True
        self.__heading = "e"
        self._speed = [3, 0]
    
    def move_west(self):
        self._moving = True
        self.__heading = "w"
        self._speed = [-3, 0]