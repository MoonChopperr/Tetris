from settings import *
from sys import exit # helps with our exit
#Creating the window using class main

#components
from game import Game
from score import Score
from preview import Preview

from random import choice
class Main:
    def __init__(self):
        # general setup
        pygame.init() #starts pygame
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Ryou's Tetris") #name
        self.clock = pygame.time.Clock() #

        #shapes for preview
        self.next_shapes = [choice(list(TETROMINOS.keys()))for shape in range(3)]
        # print(self.next_shapes)

        #components
        self.game = Game(self.get_next_shape)
        self.score = Score()
        self.preview = Preview()

    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        return next_shape

    def run(self):
        while True:
            for event in pygame.event.get(): #gets user input
                if event.type == pygame.QUIT:
                    pygame.quit() #closes pygame
                    # after quit happens want to exit everything otherwise error.
                    exit()
            #display
            self.display_surface.fill(GRAY) #bg color

            #components
            self.game.run()
            self.score.run()
            self.preview.run(self.next_shapes)
            #updating game
            pygame.display.update() #updates what happens in the game
            self.clock.tick(144) #obj in pygame that controls the framerate, blank = as many fps

if __name__ == '__main__':
    main = Main()
    main.run() #runs the window
