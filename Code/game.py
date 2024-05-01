from settings import *
from random import choice #random from object

class Game:
    def __init__(self):
        # general setup
        self.surface = pygame.Surface(
            (GAME_WIDTH, GAME_HEIGHT)
        )  # placing these surfaces ontop of the display_surface
        self.display_surface = pygame.display.get_surface()  # returns displays surface
        self.rect = self.surface.get_rect(topleft=(PADDING, PADDING))
        self.sprites = pygame.sprite.Group()

        # lines layer where we adjust the alpha opacity
        self.line_surface = self.surface.copy()  # copy of above
        self.line_surface.fill((0, 255, 0))  # green
        self.line_surface.set_colorkey(
            (0, 255, 0)
        )  # sets color key to green hides green
        self.line_surface.set_alpha(30)  # max 255, opacity, higher = less transparent

        #tetromino
        self.tetronimo = Tetromino(choice(list(TETROMINOS.keys())), self.sprites)

        #test
        # self.block = Block(self.sprites,pygame.Vector2(3,5), 'blue')
    def draw_grid(self):
        for col in range(1, COLUMNS):  # adding 1 removes first line at 0
            x = col * CELL_SIZE
            pygame.draw.line(
                self.line_surface, LINE_COLOR, (x, 0), (x, self.surface.get_height()), 1
            )

        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(
                self.line_surface, LINE_COLOR, (0, y), (self.surface.get_width(), y), 1
            )

        self.surface.blit(self.line_surface, (0, 0))
        # Pygame blit() The Pygame blit() method is one of the methods to place an image onto the screens of pygame applications. It intends to put an image on the screen. It just copies the pixels of an image from one surface to another surface just like that.


    def run(
        self,
    ):  # block image transfer = one surface ontop of another surface 2 args (surface, position(x,y))

        # drawing
        self.surface.fill(GRAY)
        self.sprites.draw(self.surface)

        self.draw_grid()
        self.display_surface.blit(self.surface, (PADDING, PADDING))  # padding of window
        pygame.draw.rect(self.display_surface, (255, 255, 255), self.rect, 1)  # border

class Tetromino: #organizes multiple blocks into a shape
    def __init__(self, shape, group):
        #setup
        self.block_positions = TETROMINOS[shape]['shape']
        self.color=TETROMINOS[shape]['color']

        #create blocks
        self.blocks = [Block(group, pos, self.color) for pos in self.block_positions] #list comprehension of creating a block instance of each block

class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        super().__init__(group)
        #gen
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)

        #position
        self.pos = pygame.Vector2(pos) + pygame.Vector2(BLOCK_OFFSET)
        x= self.pos.x * CELL_SIZE # needed to per grid
        y= self.pos.y * CELL_SIZE
        self.rect = self.image.get_rect(topleft=(x, y))
