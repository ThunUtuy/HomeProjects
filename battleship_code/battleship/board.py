import pygame
from .constants import ROWS, COLS, BLUE, LIGHT_BLUE, SQUARE_SIZE, BLACK, GREY, RED

class Board:
    def __init__(self, win):
        #initialise board
        self.draw_squares(win)

    def draw_squares(self, win):
        win.fill(BLUE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, LIGHT_BLUE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE) )
    
    def draw_squares_black(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, GREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE) )

    def draw_ship_token(self, win, row, col):
        pygame.draw.circle(win, BLACK, ( col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE //2, ), SQUARE_SIZE // 2)
    
    def draw_sea_tile(self, win, row, col):
        pygame.draw.rect(win, BLUE, ( col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE) )

    def draw_small_circle(self, win, row, col):
        pygame.draw.circle(win, RED, ( col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE //2, ), 5)

    def draw_small_circle_black(self, win, row, col):
        pygame.draw.circle(win, BLACK, ( col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE //2, ), 5)

    


    

    





