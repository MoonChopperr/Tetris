from settings import *
from os.path import join
class Score:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING))
        self.rectangle = self.surface.get_rect(bottomright = (WINDOW_WIDTH-PADDING, WINDOW_HEIGHT-PADDING)) #returns rectangle around surface
        self.display_surface = pygame.display.get_surface()
        #font
        self.font = pygame.font.Font(join('..', 'Graphics','Russo_One.ttf'), 30)

        #increment
        self.increment_height = self.surface.get_height() / 3

    def display_text(self, pos, text):
        text_surface = self.font.render(text, True, 'white')
        text_rext = text_surface.get_rect(center=pos)
        self.surface.blit(text_surface, text_rext)

    def run(self):
        self.surface.fill(GRAY)
        for i, text in enumerate(['Score', 'Level', 'Lines']):
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            self.display_text((x,y), text)

        self.display_surface.blit(self.surface, (self.rectangle))
