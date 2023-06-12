from pac import Pacman
from ghost import Ghost
import pygame, sys

class Game():
    def __init__(self):
        pygame.init()

        x = 214
        y = 251
        self.screen = pygame.display.set_mode((x, y))
        self.clock = pygame.time.Clock()

        pygame.display.flip()

        self.key_up = False
        self.key_left = False
        self.key_right = False
        self.key_down = False

        self.sprites = []
        self.pac = Pacman(int(x/2), int(y/2), 14, 14)
        self.sprites.append(self.pac)
        # add the ghosts

        # create the data for the level
        self.heatmap = pygame.image.load("images/level1/level1_heat.png")

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

    # draw the basic level, then all the items currently on the level
    def draw_level(self):
        self.screen.blit(pygame.image.load("images/level1/level1_base.png"), (0, 0))

        #for pellets and other collectablesS
        #draw where they should be initalized on the heatmap,
        # record thier posiiton into an array of all the collectables,
        # when pman goes over that collectable, set that collectables flag to false
        # only draw the collectables that have true flags

if __name__ == '__main__':
    Game()