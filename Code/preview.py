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
        self.shape_surfaces = {shape: load(path.join('..','Graphics',f'{shape}.png')).convert_alpha() for shape in TETROMINOS.keys()}

        #images
        self.increment_height = self.surface.get_height() / 3

    def display_pieces(self, shapes):
        for i, shape in enumerate(shapes):
            shape_surface = self.shape_surfaces[shape]
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            rect = shape_surface.get_rect(center = (x,y))
            self.surface.blit(shape_surface,rect)

    def run(self, next_shapes):
        self.surface.fill(GRAY)
        self.display_pieces(next_shapes)
        self.display_surface.blit(self.surface, (self.rectangle))
        pygame.draw.rect(self.display_surface, LINE_COLOR, self.rectangle,2, 2)
