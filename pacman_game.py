from pac import Pacman
from ghost import Ghost
import pygame, sys

class Game():
    def __init__(self):
        pygame.init()

        x = 800
        y = 600
        self.screen = pygame.display.set_mode((x, y))
        self.clock = pygame.time.Clock()

        pygame.display.flip()

        self.key_up = False
        self.key_left = False
        self.key_right = False
        self.key_down = False

        self.sprites = []
        self.sprites.append(Pacman(x/2, y/2))
        # add the ghosts
        
        self.draw()

    def draw(self):
        while True:
            # for loop on sprite array
            # update every sprite
            for sprite in self.sprites:
                sprite.update()

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
            if self.penguin.moving == False:
                if self.key_up and self.key_left:
                    self.penguin.move_northwest()
                elif self.key_up and self.key_right:
                    self.penguin.move_northeast()
                elif self.key_up:
                    self.penguin.move_north()
                elif self.key_down and self.key_left:
                    self.penguin.move_southwest()
                elif self.key_down and self.key_right:
                    self.penguin.move_southeast()
                elif self.key_down:
                    self.penguin.move_south()
                elif self.key_right:
                    self.penguin.move_east()
                elif self.key_left:
                    self.penguin.move_west()
            
            self.screen.fill((255, 255, 255))
            self.screen.blit(pygame.image.load()) # sprite array

            pygame.display.flip()
            pygame.event.pump()
            self.clock.tick(10)

if __name__ == '__main__':
    Game()