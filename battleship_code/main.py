import pygame
from battleship.constants import WIDTH, HEIGHT, SQUARE_SIZE
from battleship.board import Board
from battleship.player import Player
from battleship.game import Game

pygame.display.set_caption("battleship")
FPS = 60

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row,col

def main():
    run = True
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    #board = Board(WIN)
    #player1 = Player()
    game = Game(WIN)
    clock = pygame.time.Clock()
    row1, col1 = 69,69

    #testing
    #player1.check_ship_valid(0, 0, 0, 2, 3)
    #print(player1.list_location)


    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = get_row_col_from_mouse(pos)
                if x <= 5: 
                    row2, col2 = row1, col1
                    row1, col1 = get_row_col_from_mouse(pos)
                    game.select(row1, col1, row2, col2)

            pygame.display.update()
        
    pygame.quit()

main()