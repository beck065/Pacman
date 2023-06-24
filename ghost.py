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
        self.__next_directions = self.choose_direction(heatmap, pac_pos)

        if self.__next_directions != [] or self.__next_directions != None:
            match self.__next_directions[0][2]:
                case "e":
                    offset = [13, 0]
                case "s":
                    offset = [0, 13]
                case _:
                    offset = [0, 0]

            if self.check_direction(heatmap, self._pos, [self.__next_directions[0][0], self.__next_directions[0][1]], offset):
                self.__heading = self.__next_directions[0][2]
                self._speed = [self.__next_directions[0][0], self.__next_directions[0][1]]
                self.__next_directions.pop(0)
                super().update(heatmap)
                return

        super().update(heatmap)

    def choose_direction(self, heatmap, pac_pos):
        # start with pac_pos work its way back
        # travel towards pos, go around obsticals if needed
        pos = [self._pos[0], self._pos[1]]
        directions = []
        while pos[0] != pac_pos[0] or pos[1] != pac_pos[1]: #?
            if pos[1] - pac_pos[1] > 0:
                while self.check_direction(heatmap, pos, [0, -1], [0, 0]) != True:
                    # move west
                    # update pos
                    pos[0] -= 1
                    # add direction (if it changed)
                    if directions.__len__() == 0 or directions[directions.__len__()-1][2] != "w":
                        directions.append([-1, 0, "w"])
                # move north
                # update pos
                pos[1] -= 1
                # add direction (if it changed)
                if directions.__len__() == 0 or directions[directions.__len__()-1][2] != "n":
                    directions.append([0, -1, "n"])
            elif pos[1] - pac_pos[1] < 0:
                while self.check_direction(heatmap, pos, [0, 1], [0, 13]) != True:
                    # move west
                    # update pos
                    pos[0] -= 1
                    # add direction (if it changed)
                    if directions.__len__() == 0 or directions[directions.__len__()-1][2] != "w":
                        directions.append([-1, 0, "w"])
                # move south
                # update pos
                pos[1] += 1
                # add direction (if it changed)
                if directions.__len__() == 0 or directions[directions.__len__()-1][2] != "s":
                    directions.append([0, 1, "s"])
            elif pos[0] - pac_pos[0] > 0:
                while self.check_direction(heatmap, pos, [-1, 0], [0, 0]) != True:
                    # move north
                    # update pos
                    pos[1] -= 1
                    # add direction (if it changed)
                    if directions.__len__() == 0 or directions[directions.__len__()-1][2] != "n":
                        directions.append([0, -1, "n"])
                # move west
                # update pos
                pos[0] -= 1
                # add direction (if it changed)
                if directions.__len__() == 0 or directions[directions.__len__()-1][2] != "w":
                    directions.append([-1, 0, "w"])
            elif pos[0] - pac_pos[0] < 0: 
                while self.check_direction(heatmap, pos, [1, 0], [13, 0]) != True:
                    # move north
                    # update pos
                    pos[1] -= 1
                    # add direction (if it changed)
                    if directions.__len__() == 0 or directions[directions.__len__()-1][2] != "n":
                        directions.append([0, -1, "n"])
                # move east
                # update pos
                pos[0] += 1
                # add direction (if it changed)
                if directions.__len__() == 0 or directions[directions.__len__()-1][2] != "e":
                    directions.append([1, 0, "e"])

        return directions
        
    def check_direction(self, heatmap, pos, speed, offset):
        for x in range(self._width):
            for y in range(self._height):
                cur_pixel = heatmap.get_at((pos[0] + x + speed[0] + offset[0], pos[1] + y + speed[1] + offset[1]))
                if cur_pixel == pygame.Color(0, 0, 0, 0) or cur_pixel == pygame.Color(1, 0, 0, 0) or cur_pixel == pygame.Color(0, 1, 0, 0) or cur_pixel == pygame.Color(0, 0, 1, 0):
                        return False
        return True