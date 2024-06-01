#preview of next 3 pieces
from settings import *
from pygame.image import load
from os import path

class  Preview:

    def __init__(self, next_shapes):
        self.display_surface = pygame.display.get_surface()
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION))
        self.rectangle = self.surface.get_rect(topright = (WINDOW_WIDTH - PADDING,PADDING)) #returns rectangle around surface

    # shapes
        # self.next_shapes = next_shapes
        # self.shape_surfaces = {shape: load('../graphics/T.png') for shape in TETROMINOS.keys()}
        self.shape_surfaces = {shape: load(path.join('..','graphics',f'{shape}.png')).convert_alpha() for shape in TETROMINOS.keys()}

    def display_pieces(self, shapes):
        for shape in shapes:
            print(shape)

    def run(self, next_shapes):
        self.surface.fill(GRAY)
        self.display_pieces(self.next_shapes)
        self.display_surface.blit(self.surface, (self.rectangle))
        pygame.draw.rect(self.display_surface, LINE_COLOR, self.rectangle,2, 2)
