from pac import Pacman
from ghost import Ghost
from dot import Dot
from pellet import Pellet
import pygame, sys, random

class Game():
    def __init__(self):
        pygame.init()
        random.seed()

        self.debug = False

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
        self.ghosts = []

        # create the data for the level
        self.heatmap = pygame.image.load("images/level1/level1_heat.png")
        
        self.dots = []
        self.pellets = []
        self.pellet_timer = None

        self.init_level()

        self.items = self.dots + self.pellets # use items to iterate through all items for drawing

        self.draw()

    def draw(self):
        while True:
            # for loop on sprite array
            # update every sprite
            for sprite in self.sprites:
                if self.is_ghost(sprite):
                    sprite.update(self.heatmap, self.pac.get_position())
                else:
                    sprite.update(self.heatmap)

            if self.pellet_timer != None and self.pellet_timer > 0:
                self.pellet_timer -= self.clock.get_rawtime()
            elif self.pellet_timer != None and self.pellet_timer <= 0:
                self.pellet_timer = None
                for ghost in self.ghosts:
                    ghost.set_vulnerable(False)

            if (self.debug):
                print(self.pellet_timer)

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

            self.update_level()

            self.draw_level()

            for sprite in self.sprites:
                if sprite.is_alive():
                    self.screen.blit(pygame.image.load(sprite.get_image()), sprite.get_position()) # sprite array

            pygame.display.flip()
            pygame.event.pump()
            self.clock.tick(60)

    def init_level(self):
        # for black squares in heatmap, add a dot
        # for white squares in heatmap, add a pellet
        # place pacman where the yellow square is
        # place ghosts where their corresponding color is
        for x in range(self.heatmap.get_width()):
            for y in range(self.heatmap.get_height()):
                cur_pixel = self.heatmap.get_at((x, y))
                if (cur_pixel == pygame.Color(0, 0, 0, 255) or cur_pixel == pygame.Color(1, 0, 0, 255) or cur_pixel == pygame.Color(0, 1, 0, 255) or cur_pixel == pygame.Color(0, 0, 1, 255) or
                    cur_pixel == pygame.Color(1, 1, 0, 255) or cur_pixel == pygame.Color(1, 0, 1, 255) or cur_pixel == pygame.Color(0, 1, 1, 255) or cur_pixel == pygame.Color(1, 1, 1, 255)):
                    self.dots.append(Dot(x, y))
                if cur_pixel == pygame.Color(255, 255, 255, 255) or cur_pixel == pygame.Color(254, 255, 255, 255) or cur_pixel == pygame.Color(255, 254, 255, 255) or cur_pixel == pygame.Color(255, 255, 254, 255):
                    self.pellets.append(Pellet(x, y))
                if cur_pixel == pygame.Color(255, 255, 0, 255):
                    self.pac = Pacman(x, y, 14, 14)
                    self.sprites.append(self.pac)
                if cur_pixel == pygame.Color(136, 136, 136, 255):
                    self.blinky = Ghost(x, y, 14, 14)
                    self.ghosts.append(self.blinky)
                    self.sprites.append(self.blinky)
                
                if (self.debug):
                    if (self.heatmap.get_at((x, y)) != pygame.Color(0, 0, 0, 0) and self.heatmap.get_at((x, y)) != pygame.Color(1, 0, 0, 0) and self.heatmap.get_at((x, y)) != pygame.Color(0, 1, 0, 0) and self.heatmap.get_at((x, y)) != pygame.Color(0, 0, 1, 0) and cur_pixel != pygame.Color(255, 255, 255, 255) and cur_pixel != pygame.Color(254, 255, 255, 255) and cur_pixel != pygame.Color(255, 254, 255, 255) and cur_pixel != pygame.Color(255, 255, 254, 255)
                        and self.heatmap.get_at((x, y)) != pygame.Color(255, 0, 0, 255) and self.heatmap.get_at((x, y)) != pygame.Color(254, 0, 0, 255) and self.heatmap.get_at((x, y)) != pygame.Color(255, 1, 0, 255) and self.heatmap.get_at((x, y)) != pygame.Color(255, 0, 1, 255) and self.heatmap.get_at((x, y)) != pygame.Color(255, 1, 1, 255) and self.heatmap.get_at((x, y)) != pygame.Color(254, 1, 0, 255) and self.heatmap.get_at((x, y)) != pygame.Color(254, 0, 1, 255) and self.heatmap.get_at((x, y)) != pygame.Color(254, 1, 1, 255)
                        and cur_pixel != pygame.Color(198, 0, 255, 255) and cur_pixel != pygame.Color(198, 0, 254, 255) and cur_pixel != pygame.Color(198, 1, 255, 255) and cur_pixel != pygame.Color(199, 0, 255, 255)):
                        print(self.heatmap.get_at((x, y)))
                

    # draw the basic level, then all the items currently on the level
    def draw_level(self):
        self.screen.blit(pygame.image.load("images/level1/level1_base.png"), (0, 0))

        #for pellets and other collectables
        #draw where they should be initalized on the heatmap,
        # record thier posiiton into an array of all the collectables,
        # when pman goes over that collectable, set that collectables flag to false
        # only draw the collectables that have true flags
        for pellet in self.pellets:
            if pellet.is_collected() != True:
                self.screen.blit(pygame.image.load("images/items/power_pellet.png"), pellet.get_position())

        for dot in self.dots:
            if dot.is_collected() != True:
                self.screen.blit(pygame.image.load("images/items/dot.png"), dot.get_position())

    def update_level(self):
        # check pman's position
        # is its on a white or black square, consume that item
        for item in self.items:
            # iterate through pman's position, check every position against
            if self.pac.is_inside(item.get_position()) and item.is_collected() == False:
                pellet_timer = item.collect()
                if pellet_timer != None:
                    self.pellet_timer = pellet_timer
                    for ghost in self.ghosts:
                        ghost.set_vulnerable(True)

        for ghost in self.ghosts:
            for x in range(ghost.get_width()):
                for y in range(ghost.get_height()):
                    cur_pos = ghost.get_position()
                    if self.pac.is_inside((cur_pos[0] + x, cur_pos[1] + y)):
                        if ghost.is_vulnerable() == True:
                            ghost.kill()
                        else:
                            # kill pac, end game
                            pygame.quit()
                            sys.exit()

        flags = []
        for dot in self.dots:
            flags.append(dot.is_collected())

        if all(flags):
            pygame.quit()
            sys.exit()

    def is_ghost(self, sprite):
        for ghost in self.ghosts:
            if sprite == ghost:
                return True
            
        return False

if __name__ == '__main__':
    Game()