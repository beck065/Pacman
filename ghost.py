from sprite import Sprite
import random, pygame

class Ghost(Sprite):
    def __init__(self, x_pos, y_pos, width, height):
        super().__init__(x_pos, y_pos, width, height)
        self.__image =  "images/ghosts/blinky/"
        self.__heading = "w"
        self.__vulnerable = False
        self._speed = [0, -1]
        self._moving = True
        self.__next_heading, self.__next_speed = self.choose_direction()

    def get_image(self):
        if self.__vulnerable == True:
            return "images/ghosts/vulnerable/1.png"
        else:
            return self.__image + self.__heading + ".png"
         
    def set_vulnerable(self, bool):
        self.__vulnerable = bool

    def is_vulnerable(self):
        return self.__vulnerable
    
    def update(self, heatmap):
        for x in range(self._width):
            for y in range(self._height):
                cur_pixel = heatmap.get_at((self._pos[0] + x + self._speed[0], self._pos[1] + y + self._speed[1]))
                if cur_pixel == pygame.Color(0, 0, 0, 0) or cur_pixel == pygame.Color(1, 0, 0, 0) or cur_pixel == pygame.Color(0, 1, 0, 0) or cur_pixel == pygame.Color(0, 0, 1, 0):
                    self.__heading = self.__next_heading
                    self._speed = self.__next_speed
                    self.__next_heading, self.__next_speed = self.choose_direction()
                    break

        while True:
            super().update(heatmap)
            if self._moving == False:
                self.__heading, self._speed = self.choose_direction()
                self._moving = True
            else:
                self._next_heading, self.__next_speed = self.choose_direction()
                break


    def choose_direction(self):
        directions = [("n", [0, -1]), ("s", [0, 1]), ("e", [1, 0]), ("w", [-1, 0])]
        direction = random.choice(directions)

        return direction