from sprite import Sprite

class Pacman(Sprite):
    def __init__(self, x_pos, y_pos):
         super().__init__(x_pos, y_pos)
         self.heading = "east"
         # loop of images in animation?
         self.image =  "/images/pac/"
         self.animation_num = 1
         