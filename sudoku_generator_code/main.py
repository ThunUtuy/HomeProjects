import pygame
from sudoku_generator.constants import WIDTH, HEIGHT, SQUARE_SIZE
from sudoku_generator.game import Game

def get_row_col_from_mouse(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return (row, col)

def main():
    run = True
    pygame.display.set_caption("Sudoku")
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(WIN)

    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
                
        
    pygame.quit()

main()

