# parent class for pac & ghosts
class Sprite():
    def __init__(self, x_pos, y_pos):
        self.__pos = [x_pos, y_pos]
        self.__speed = [0, 0]
        self.__acceleration = [0, 0]

    def update(self):
        self.__speed += self.__acceleration 
        self.__pos += self.__speed