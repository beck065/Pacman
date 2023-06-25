from sprite import Sprite
import random, pygame

class Ghost(Sprite):
    def __init__(self, x_pos, y_pos, width, height):
        super().__init__(x_pos, y_pos, width, height)
        self.__image =  "images/ghosts/blinky/"
        self.__heading = "w"
        self.__vulnerable = False
        self._speed = [-1, 0]
        self._moving = True
        # bad code mode
        self.__move_x_around = False
        self.__move_y_around = False

    def get_image(self):
        if self.__vulnerable == True:
            return "images/ghosts/vulnerable/1.png"
        else:
            return self.__image + self.__heading + ".png"
         
    def set_vulnerable(self, bool):
        self.__vulnerable = bool

    def is_vulnerable(self):
        return self.__vulnerable
    
    def update(self, heatmap, pac_pos):
        if self._alive:
            self._speed, self.__heading = self.choose_direction(heatmap, pac_pos)
            print("moving to (" + str(self._pos[0] + self._speed[0]) + ", " + str(self._pos[1] + self._speed[1]) + ")")
            print("heading: " + self.__heading)

            super().update(heatmap)

    def choose_direction(self, heatmap, pac_pos):
        # start with pac_pos work its way back
        # travel towards pos, go around obsticals if needed
        
        # if vulnerable, do the opposite
        if self._pos[0] != pac_pos[0] or self._pos[1] != pac_pos[1]: #?
            if self._pos[1] - pac_pos[1] > 0:
                print("trying to move north")
                if self.check_direction(heatmap, self._pos, [0, -1]) != True:
                    # move west
                    # update pos
                    # add direction (if it changed)
                    print("cannot move north, moving west around")
                    if self.check_direction(heatmap, self._pos, [-1, 0]) != True or self.__move_x_around != True:
                        print("cannot move west around, move east around")
                        self.__move_x_around = False
                        return [1, 0], "e"
                    print("can move west around")
                    self.__move_x_around = True
                    return [-1, 0], "w"
                # move north
                # update pos
                # add direction (if it changed)
                print("can move north")
                return [0, -1], "n"
            elif self._pos[1] - pac_pos[1] < 0:
                print("trying to move south")
                if self.check_direction(heatmap, self._pos, [0, 1]) != True:
                    # move west
                    # update pos
                    # add direction (if it changed)
                    print("cannot move south, trying to move west around")
                    if self.check_direction(heatmap, self._pos, [-1, 0]) != True or self.__move_x_around != True:
                        print("cannot move west around, move east around")
                        self.__move_x_around = False
                        return [1, 0], "e"
                    print("can move west around")
                    self.__move_x_around = True
                    return [-1, 0], "w"
                # move south
                # update pos
                # add direction (if it changed)
                print("can move south")
                return [0, 1], "s"
            elif self._pos[0] - pac_pos[0] > 0:
                print("trying to move west")
                if self.check_direction(heatmap, self._pos, [-1, 0]) != True:
                    # move north
                    # update pos
                    # add direction (if it changed)
                    print("cannot move west, trying to move north around")
                    if self.check_direction(heatmap, self._pos, [0, -1]) != True or self.__move_y_around != True:
                        print("cannot move north around, move south around")
                        self.__move_y_around = False
                        return[0, 1], "s"
                    print("can move north around")
                    self.__move_y_around = True
                    return [0, -1], "n"
                # move west
                # update pos
                # add direction (if it changed)
                print("can move west")
                return [-1, 0], "w"
            elif self._pos[0] - pac_pos[0] < 0: 
                print("trying to move east")
                if self.check_direction(heatmap, self._pos, [1, 0]) != True:
                    # move north
                    # update pos
                    # add direction (if it changed)
                    print("cannot move east, trying to move north around")
                    if self.check_direction(heatmap, self._pos, [0, -1]) != True or self.__move_y_around != True:
                        print("cannot move north around, move south around")
                        self.__move_y_around = False
                        return[0, 1], "s"
                    print("can move north around")
                    self.__move_y_around = True
                    return [0, -1], "n"
                # move east
                # update pos
                # add direction (if it changed)
                print("can move east")
                return [1, 0], "e"
            
        return [], None
        
    def check_direction(self, heatmap, pos, speed):
        for x in range(self._width):
            for y in range(self._height):
                cur_pixel = heatmap.get_at((pos[0] + x + speed[0], pos[1] + y + speed[1]))
                if cur_pixel == pygame.Color(0, 0, 0, 0) or cur_pixel == pygame.Color(1, 0, 0, 0) or cur_pixel == pygame.Color(0, 1, 0, 0) or cur_pixel == pygame.Color(0, 0, 1, 0):
                        return False
        return True