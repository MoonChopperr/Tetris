from settings import *

class Game:
    def __init__(self):
        #general setup
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT)) #placing these surfaces ontop of the display_surface
        self.display_surface = pygame.display.get_surface() #returns displays surface

    def draw_grid(self):
        for col i

    def run(self): #block image transfer = one surface ontop of another surface 2 args (surface, position(x,y))
        self.display_surface.blit(self.surface, (PADDING, PADDING)) # padding of window
