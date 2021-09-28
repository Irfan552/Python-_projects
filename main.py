import pygame
import time
from pygame.locals import * #this will import global variable for us such as KEYDOWN

class Snake:        # we are using classes to keep code clean and not all code in main function
    def __init__(self, parent_screen):    # we need parent screen so we are adding as new class member
        self.parent_screen = parent_screen   #stored parent screen as new class memeber
        self.block = pygame.image.load("resources/block.jpg").convert()  # block from our resources
        self.x = 100  # where you want to place block on screen
        self.y = 100
    def draw(self):
        self.parent_screen.fill((110, 110, 5))  # if we don't use this we will see draw where ever we go. this will clear trail
        self.parent_screen.blit(self.block, (self.x, self.y))  # blit is used to drop object on screen
        # we used parent screen which we stored in above function
        pygame.display.flip()

    def move_left(self):
        self.x -=10
        self.draw()

    def move_right(self):
        self.x +=10
        self.draw()

    def move_up(self):
        self.y -=10
        self.draw()

    def move_down(self):
        self.y +=10
        self.draw()

class Game:
    def __init__(self):         # using class and self. to keep code clean and not all in main function
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.surface.fill((110, 110, 5))
        self.snake = Snake(self.surface) # snake constractor parent screen (from snake class) = self.surface
        self.snake.draw()

    def run(self):
        running = True  # we want to stop screen when we press something instead of time
        # we will do this with while loop using running as variable
        while running:
            for event in pygame.event.get():  # if came for pygame.locals import module as in start
                if event.type == KEYDOWN:

                    if event.key == K_UP:  # we are creating methods with self.snake moves or we could use old way where we want to move block by 10 by pressing keys
                        self.snake.move_up()    # as we are using methods so we need to write methods in snake class for these
                        #block_y -= 10 not needed now as we are using classes
                        #draw_block()  # we want to draw behind block when it moves
                    if event.key == K_DOWN:
                        self.snake.move_down()   # from methods in snake class
                        #block_y += 10
                        #draw_block()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                        #block_x -= 10 not needed now as we are using classes
                        #draw_block()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                        #block_x += 10
                        #draw_block()
                elif event.type == QUIT:
                    running = False




if __name__ == "__main__":

    game = Game()
    game.run()



