from sprite import Sprite

class Ghost(Sprite):
    def __init__(self, x_pos, y_pos, width, height):
         super().__init__(x_pos, y_pos, width, height)
         self.__image =  "images/ghosts/blinky/"
         self.__heading = "w"
         self.__vulnerable = False

    def get_image(self):
         if self.__vulnerable == True:
             return "images/ghosts/vulnerable/1.png"
         else:
            return self.__image + self.__heading + ".png"
         
    def set_vulnerable(self, bool):
        self.__vulnerable = bool

    def is_vulnerable(self):
        return self.__vulnerable