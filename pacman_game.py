from pac import Pacman
from ghost import Ghost
from dot import Dot
from pellet import Pellet
import pygame, sys

class Game():
    def __init__(self):
        pygame.init()

        x = 224
        y = 256
        self.screen = pygame.display.set_mode((x, y))
        self.clock = pygame.time.Clock()

        pygame.display.flip()

        self.key_up = False
        self.key_left = False
        self.key_right = False
        self.key_down = False

        self.sprites = []
        # add the ghosts

        # create the data for the level
        self.heatmap = pygame.image.load("images/level1/level1_heat.png")
        
        self.dots = []
        self.pellets = []

        self.init_level()

        self.draw()

    def draw(self):
        while True:
            # for loop on sprite array
            # update every sprite
            for sprite in self.sprites:
                sprite.update(self.heatmap)

            for event in pygame.event.get():
                # accounts for holding a key
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    # use keys flags to account for holding a key
                    if event.key == pygame.K_UP:
                        self.key_up = not self.key_up
                    if event.key == pygame.K_LEFT:
                        self.key_left = not self.key_left
                    if event.key == pygame.K_RIGHT:
                        self.key_right = not self.key_right
                    if event.key == pygame.K_DOWN:
                        self.key_down = not self.key_down
           
            # pacman movement (could use something similar for ghosts?)
            if self.key_up:
                self.pac.move_north(self.heatmap)
            elif self.key_down:
                self.pac.move_south(self.heatmap)
            elif self.key_right:
                self.pac.move_east(self.heatmap)
            elif self.key_left:
                self.pac.move_west(self.heatmap)
            
            self.draw_level()

            for sprite in self.sprites:
                self.screen.blit(pygame.image.load(sprite.get_image()), sprite.get_position()) # sprite array

            pygame.display.flip()
            pygame.event.pump()
            self.clock.tick(15)

    def init_level(self):
        # for black squares in heatmap, add a dot
        # for white squares in heatmap, add a pellet
        # place pacman where the yellow square is
        # place ghosts where their corresponding color is
        for x in range(self.heatmap.get_width()):
            for y in range(self.heatmap.get_height()):
                match self.heatmap.get_at((x, y)):
                    case [pygame.Color(0, 0, 0, 255)]:
                        self.dots.append(Dot(x, y))
                    case [pygame.Color(255, 255, 255, 255)]:
                        self.pellets.append(Pellet(x, y))
                    case [pygame.Color(255, 255, 0, 255)]:
                        self.pac = Pacman(x, y, 12, 12)
                        self.sprites.append(self.pac)

    # draw the basic level, then all the items currently on the level
    def draw_level(self):
        self.screen.blit(pygame.image.load("images/level1/level1_base.png"), (0, 0))

        #for pellets and other collectables
        #draw where they should be initalized on the heatmap,
        # record thier posiiton into an array of all the collectables,
        # when pman goes over that collectable, set that collectables flag to false
        # only draw the collectables that have true flags
        for pellet in self.pellets:
            if pellet.get_status() == True:
                self.screen.blit(pygame.image.load("images/items/power_pellet.png"), pellet.get_position())

        for dot in self.dots:
            if dot.get_status() == True:
                self.screen.blit(pygame.image.load("images/items/dot.png"), dot.get_position())

    def update_level(self):
        return


if __name__ == '__main__':
    Game()