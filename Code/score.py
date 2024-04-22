from settings import *

class Score:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING))
        self.rectangle = self.surface.get_rect(bottomright = (WINDOW_WIDTH-PADDING, WINDOW_HEIGHT-PADDING)) #returns rectangle around surface
        self.display_surface = pygame.display.get_surface()
    def run(self):
        self.display_surface.blit(self.surface, (self.rectangle))
