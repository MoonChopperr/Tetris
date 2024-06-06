from settings import *
from random import choice #random from object
from timer import Timer

class Game:
    def __init__(self, get_next_shape):
        # general setup
        self.surface = pygame.Surface(
            (GAME_WIDTH, GAME_HEIGHT)
        )  # placing these surfaces ontop of the display_surface
        self.display_surface = pygame.display.get_surface()  # returns displays surface
        self.rect = self.surface.get_rect(topleft=(PADDING, PADDING))
        self.sprites = pygame.sprite.Group()

        # game connection
        self.get_next_shape = get_next_shape

        # lines layer where we adjust the alpha opacity
        self.line_surface = self.surface.copy()  # copy of above
        self.line_surface.fill((0, 255, 0))  # green
        self.line_surface.set_colorkey((0, 255, 0))  # sets color key to green hides green
        self.line_surface.set_alpha(30)  # max 255, opacity, higher = less transparent

        #tetromino
        self.field_data=[[0 for x in range(COLUMNS)] for y in range(ROWS)]
        self.tetromino = Tetromino(
            choice(list(TETROMINOS.keys())),
            self.sprites,
            self.create_new_tetromino,
            self.field_data)

        #timer
        self.timers={
            'vertical move': Timer(UPDATE_START_SPEED, True, self.move_down),
            'horizontal move': Timer(MOVE_WAIT_TIME),
            'rotate': Timer(ROTATE_WAIT_TIME)
        }
        #test
        # self.block = Block(self.sprites,pygame.Vector2(3,5), 'blue')
        self.timers['vertical move'].activate()


        #score
        self.current_level=1
        self.current_score=0
        self.current_lines=0

    def calculate_score(self, num_lines):

    def timer_update(self):
        for timer in self.timers.values():
            timer.update()

    def move_down(self):
        # print('timer')
        self.tetromino.move_down()

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

    def input(self):
        keys=pygame.key.get_pressed() #built in ds returns for all possible inputs
        if not self.timers['horizontal move'].active:
            if keys[pygame.K_LEFT]:
                self.tetromino.move_horizontal(-1)
                self.timers['horizontal move'].activate()
            if keys[pygame.K_RIGHT]:
                self.tetromino.move_horizontal(1)
                self.timers['horizontal move'].activate()


        #rotation input
        if not self.timers['rotate'].active:
            if keys[pygame.K_UP]:
                self.tetromino.rotate()
                self.timers['rotate'].activate()

    def create_new_tetromino(self):
        self.check_finished_rows()
        self.tetromino = Tetromino(
            self.get_next_shape(),
            self.sprites,
            self.create_new_tetromino,
            self.field_data)

    def check_finished_rows(self):  #check if row is filled with blocks
        #get row indexes
        delete_rows = []
        for i, row in enumerate(self.field_data):
            if all(row):
                delete_rows.append(i)
        if delete_rows:
            for delete_row in delete_rows:

                #delete full rows
                for sprite in self.sprites.sprites():
                    if int(sprite.pos.y) == delete_row:
                        sprite.kill()
                    # print('cleared row')
                #move down blocks
                for sprite in self.sprites.sprites():
                    if int(sprite.pos.y) < delete_row:
                        sprite.pos.y += 1
            #rebuild field data
            self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]
            for block in self.sprites:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block
        #update score
        self.calculate_score(len(delete_rows))
    def run(
        self,
    ):  # block image transfer = one surface ontop of another surface 2 args (surface, position(x,y))
        self.input()
        #update timer
        self.timer_update()
        self.sprites.update()
        # drawing
        self.surface.fill(GRAY)
        self.sprites.draw(self.surface)

        self.draw_grid()
        self.display_surface.blit(self.surface, (PADDING, PADDING))  # padding of window
        pygame.draw.rect(self.display_surface, (255, 255, 255), self.rect, 1)  # border

class Tetromino: #organizes multiple blocks into a shape
    def __init__(self, shape, group, create_new_tetromino, field_data):
        #setup
        self.block_positions = TETROMINOS[shape]['shape']
        self.color=TETROMINOS[shape]['color']
        self.create_new_tetromino = create_new_tetromino
        self.field_data=field_data
        self.shape = shape
        #create blocks
        self.blocks = [Block(group, pos, self.color) for pos in self.block_positions] #list comprehension of creating a block instance of each block
    def move_horizontal(self, amount):
        for block in self.blocks:
            block.pos.x += amount

    def move_down(self):
        if not self.next_move_vertical_collide(self.blocks, 1):
            for block in self.blocks:
                block.pos.y += 1
        else:
            for block in self.blocks:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = 1
            self.create_new_tetromino()

    #collisions if piece on the farthest right of window, aka below 0 do not allow movement
    def next_move_horizontal_collide(self, blocks, amount):
        #imaginery tetrimono
        collision_list = [block.horizontal_collide(int(block.pos.x + amount), self.field_data) for block in self.blocks]
        return True if any(collision_list) else False
    #movement
    def move_horizontal(self, amount):
        if not self.next_move_horizontal_collide(self.blocks, amount):
            for block in self.blocks:
                block.pos.x += amount

    def next_move_vertical_collide(self, blocks, amount):
        collision_list = [block.vertical_collide(int(block.pos.y+ amount), self.field_data) for block in self.blocks]
        return True if any(collision_list)else False

    def rotate(self):
        if self.shape != 'O':
            pivot_pos = self.blocks[0].pos
            new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]
            #collision check
            for pos in new_block_positions:
                if pos.x < 0 or pos.x >= COLUMNS:
                    return
                if self.field_data[int(pos.y)][int(pos.x)]:
                    return
                if pos.y > ROWS:
                    return
            #new pos
            for i, block in enumerate(self.blocks):
                block.pos = new_block_positions[i]
class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        super().__init__(group)
        #gen
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)

        #position
        self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
        # x= self.pos.x * CELL_SIZE # needed to per grid
        # y= self.pos.y * CELL_SIZE
        self.rect = self.image.get_rect(topleft=self.pos * CELL_SIZE)
    def rotate(self, pivot_pos):
        distance = self.pos - pivot_pos
        rotated = distance.rotate(90)
        new_pos = pivot_pos + rotated
        return new_pos
    def horizontal_collide(self, x, field_data):
        if not 0 <= x < COLUMNS:
            return True
        if field_data[int(self.pos.y)][x]:
            return True
    def vertical_collide(self, y, field_data):
        if y >= ROWS:
            return True
        if y >=0 and field_data[y][int(self.pos.x)]:
            return True
    def update(self):
        # print(self.pos)
        self.pos * 40
        self.rect.topleft = self.pos * CELL_SIZE
