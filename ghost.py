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
    
    def update(self, heatmap, pac_pos):
        for x in range(self._width):
            for y in range(self._height):
                cur_pixel = heatmap.get_at((self._pos[0] + x + self._speed[0], self._pos[1] + y + self._speed[1]))
                if cur_pixel == pygame.Color(0, 0, 0, 0) or cur_pixel == pygame.Color(1, 0, 0, 0) or cur_pixel == pygame.Color(0, 1, 0, 0) or cur_pixel == pygame.Color(0, 0, 1, 0):
                    self.__heading = self.__next_heading
                    self._speed = self.__next_speed
                    self.__next_heading, self.__next_speed = self.choose_direction(heatmap, pac_pos)
                    break

        while True:
            super().update(heatmap)
            if self._moving == False:
                self.__heading, self._speed = self.choose_direction(heatmap, pac_pos)
                self._moving = True
            else:
                self.__next_heading, self.__next_speed = self.choose_direction(heatmap, pac_pos)
                break

    def choose_direction(self, heatmap, pac_pos):
        pos = [self._pos[0], self._pos[1]]
        speed = [self._speed[0], self._speed[1]]
        direction_changes = []
        direction_changes_l = []
        direction_changes_r = []

        match (self.__heading):
                case ["n"]:
                    l_speed = [-1, 0, "w"]
                    r_speed = [1, 0, "e"]
                case ["e"]:
                    l_speed = [0, -1, "n"]
                    r_speed = [0, 1, "s"]
                case ["s"]:
                    l_speed = [1, 0, "e"]
                    r_speed = [-1, 0, "w"]
                case ["w"]:
                    l_speed = [0, 1, "s"]
                    r_speed = [0, -1, "n"]

        cur_pixel = heatmap.get_at((pos[0] + speed[0], pos[1] + speed[1]))

        # go until pac is found forward or wall it hit
        while (pos[0] != pac_pos[0] and pos[1] != pac_pos[1] and 
        (cur_pixel_left != pygame.Color(0, 0, 0, 0) or cur_pixel_left != pygame.Color(1, 0, 0, 0) or cur_pixel_left != pygame.Color(0, 1, 0, 0) or cur_pixel_left != pygame.Color(0, 0, 1, 0))):
            # check only front left and right (not backwards!)
            # can move 1 pixel if able to move left
            # can move 15 pixels if able to move right
            # can move 1 pixel if able to move up
            # can move 15 pixels if able to move down

            # 3 paths
            # straight
            # left (recursive)
            # right (recursive)
            # go straight until left or right path open
            # call recursive func on that path, return the path with the least amount of changes
            # keep going straight until either the ghost reaches pac man (return an array with no direction changes)
            # or hits a wall
            # then return the direction changes array (with the least amount of changes)
            # possible problem: path with the least amount of direction changes might not be the shortest path!
            
            cur_pixel = heatmap.get_at((pos[0] + speed[0], pos[1] + speed[1]))
            cur_pixel_left = heatmap.get_at((pos[0] + l_speed[0], pos[1] + l_speed[1]))
            cur_pixel_right = heatmap.get_at((pos[0] + r_speed[0], pos[1] + r_speed[1]))

            if (cur_pixel_left != pygame.Color(0, 0, 0, 0) or cur_pixel_left != pygame.Color(1, 0, 0, 0) or cur_pixel_left != pygame.Color(0, 1, 0, 0) or cur_pixel_left != pygame.Color(0, 0, 1, 0)):
                direction_changes_l.append(l_speed[2])
                direction_changes_l = self.choose_direction_rec(heatmap, pac_pos, [pos[0], pos[1]], [l_speed[0], l_speed[1]], l_speed[2], direction_changes_l)
            elif (cur_pixel_right != pygame.Color(0, 0, 0, 0) or cur_pixel_right != pygame.Color(1, 0, 0, 0) or cur_pixel_right != pygame.Color(0, 1, 0, 0) or cur_pixel_right != pygame.Color(0, 0, 1, 0)):
                direction_changes_r.append(r_speed[2])
                direction_changes_r = self.choose_direction_rec(heatmap, pac_pos, [pos[0], pos[1]], [r_speed[0], r_speed[1]], r_speed[2], direction_changes_r)
            elif (cur_pixel != pygame.Color(0, 0, 0, 0) or cur_pixel != pygame.Color(1, 0, 0, 0) or cur_pixel != pygame.Color(0, 1, 0, 0) or cur_pixel != pygame.Color(0, 0, 1, 0)):
                pos[0] += speed[0]
                pos[1] += speed[1]

        # TODO return smallest direction changes
        if pos[0] == pac_pos[0] and pos[1] == pac_pos[1]:
            return None # no direction changes needed
        # return the shorter of the two
        elif direction_changes_l.__len__() < direction_changes_r.__len__():
            return direction_changes_l
        else:
            return direction_changes_r
    
    # these variable names suck
    def choose_direction_rec(self, heatmap, pac_pos, pos, speed, heading, direction_changes_prev):
        direction_changes = direction_changes_prev
        direction_changes_l = []
        direction_changes_r = []

        match (heading):
                case ["n"]:
                    l_speed = [-1, 0, "w"]
                    r_speed = [1, 0, "e"]
                case ["e"]:
                    l_speed = [0, -1, "n"]
                    r_speed = [0, 1, "s"]
                case ["s"]:
                    l_speed = [1, 0, "e"]
                    r_speed = [-1, 0, "w"]
                case ["w"]:
                    l_speed = [0, 1, "s"]
                    r_speed = [0, -1, "n"]

        cur_pixel = heatmap.get_at((pos[0] + speed[0], pos[1] + speed[1]))

        while (pos[0] != pac_pos[0] and pos[1] != pac_pos[1] and 
        (cur_pixel_left != pygame.Color(0, 0, 0, 0) or cur_pixel_left != pygame.Color(1, 0, 0, 0) or cur_pixel_left != pygame.Color(0, 1, 0, 0) or cur_pixel_left != pygame.Color(0, 0, 1, 0))):
            cur_pixel = heatmap.get_at((pos[0] + speed[0], pos[1] + speed[1]))
            cur_pixel_left = heatmap.get_at((pos[0] + l_speed[0], pos[1] + l_speed[1]))
            cur_pixel_right = heatmap.get_at((pos[0] + r_speed[0], pos[1] + r_speed[1]))

            if (cur_pixel_left != pygame.Color(0, 0, 0, 0) or cur_pixel_left != pygame.Color(1, 0, 0, 0) or cur_pixel_left != pygame.Color(0, 1, 0, 0) or cur_pixel_left != pygame.Color(0, 0, 1, 0)):
                direction_changes_temp = []
                direction_changes_temp.append(l_speed[2])
                direction_changes_temp = self.choose_direction_rec(heatmap, pac_pos, [pos[0], pos[1]], [l_speed[0], l_speed[1]], l_speed[2], direction_changes)
                # save the path if it is shorter
                if direction_changes_l == [] or direction_changes_temp.__len__() < direction_changes_l.__len__():
                    direction_changes_l = direction_changes_temp
            elif (cur_pixel_right != pygame.Color(0, 0, 0, 0) or cur_pixel_right != pygame.Color(1, 0, 0, 0) or cur_pixel_right != pygame.Color(0, 1, 0, 0) or cur_pixel_right != pygame.Color(0, 0, 1, 0)):
                direction_changes_temp = []
                direction_changes_temp.append(l_speed[2])
                direction_changes_temp = self.choose_direction_rec(heatmap, pac_pos, [pos[0], pos[1]], [r_speed[0], r_speed[1]], r_speed[2], direction_changes)
                # save the path if it is shorter
                if direction_changes_r == [] or direction_changes_temp.__len__() < direction_changes_r.__len__():
                    direction_changes_r = direction_changes_temp
            elif (cur_pixel != pygame.Color(0, 0, 0, 0) or cur_pixel != pygame.Color(1, 0, 0, 0) or cur_pixel != pygame.Color(0, 1, 0, 0) or cur_pixel != pygame.Color(0, 0, 1, 0)):
                pos[0] += speed[0]
                pos[1] += speed[1]

        # TODO return smallest direction changes
        if pos[0] == pac_pos[0] and pos[1] == pac_pos[1]:
            return direction_changes # no direction changes needed
        # return the shorter of the two
        elif direction_changes_l.__len__() < direction_changes_r.__len__():
            return direction_changes_l
        else:
            return direction_changes_r