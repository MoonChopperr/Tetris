#preview of next 3 pieces
from settings import *

class  Preview:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION))
        self.rectangle = self.surface.get_rect(topright = (WINDOW_WIDTH - PADDING,PADDING)) #returns rectangle around surface
    def run(self):
        self.display_surface.blit(self.surface, (self.rectangle))
# pause
