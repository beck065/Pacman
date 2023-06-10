import pygame

# parent class for pac & ghosts
class Sprite():
    def __init__(self, x_pos, y_pos, width, height):
        self._pos = [[x_pos, y_pos],[x_pos+width, y_pos],[x_pos, y_pos+height],[x_pos+width, y_pos+height]]
        self._speed = [0, 0]
        self._moving = False

    def update(self, heatmap):
        flags = [False, False, False, False]
        for i in range(4):
            if heatmap.get_at((self._pos[i][0] + self._speed[0], self._pos[i][1] + self._speed[1])) == heatmap.get_at((0,0)):
                flags[i] = True
                print("One flag is true.")
            else:
                self._moving = False
                self._speed = [0, 0]
                print("One flag is false.")
                break
        print("Done.")

        if flags == [True, True, True, True]: # wtf am i doing??
            print("All flags are true.")
            for pos in self._pos:
                pos[0] += self._speed[0]
                pos[1] += self._speed[1]
 
    def get_position(self):
        print("TL: (" + str(self._pos[0][0]) + ", " + str(self._pos[0][1]) + ")")
        print("TR:(" + str(self._pos[1][0]) + ", " + str(self._pos[1][1]) + ")")
        print("BL:(" + str(self._pos[2][0]) + ", " + str(self._pos[2][1]) + ")")
        print("BR:(" + str(self._pos[3][0]) + ", " + str(self._pos[3][1]) + ")")
        return self._pos[0][0], self._pos[0][1] # returns pos of tl corner