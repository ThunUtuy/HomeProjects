import pygame
from .constants import ROWS
pygame.mixer.init()

class Player:
    def __init__(self):
        self.atk_attempts = 0
        self.ship_counter = 14
        self.list_location = []
        self.list_revealed = []
        self.water_sound = pygame.mixer.Sound("sounds/cannon_water.mp3")
        self.cannon_sound = pygame.mixer.Sound("sounds/cannon.mp3")
        self.ship_sound = pygame.mixer.Sound("sounds/ship_deployed.mp3")
        for _ in range(ROWS):
            self.list_location.append([0, 0, 0, 0, 0, 0])
            self.list_revealed.append([0, 0, 0, 0, 0, 0])
    

    def check_hor_or_vert(self, row1, col1, row2, col2):
        if row1 == row2 and col1 != col2:
            return 2 #horizontal
        elif col1 == col2 and row1 != row2:
            return 1 #vertical
        else:
            return 0

    def check_ship_valid(self, row1, col1, row2, col2, ship_length, board, win):
        #assuming row col are not out of range
        direction = self.check_hor_or_vert(row1, col1, row2, col2)
        if direction == 0:
            print("wrong angle")
            return
        #horizontal
        if direction == 2:
            if col1 > col2:
                step = -1
            else:
                step = 1

            if abs(col1 - col2) != ship_length - 1:
                print("wrong length")
                return
            for i in range(col1, col2 + step, step):
                if self.list_location[row1][i] != 0:
                    print("occupied")
                    return
            for i in range(col1, col2 + step, step):
                self.list_location[row1][i] = 1
                board.draw_ship_token(win, row1, i)
            pygame.mixer.Sound.play(self.ship_sound)
            return 0

        #vertical
        if direction == 1:
            if row1 > row2:
                step = -1
            else:
                step = 1

            if abs(row1 - row2) != ship_length - 1:
                print("wrong length")
                return
            for i in range(row1, row2 + step, step):
                if self.list_location[i][col1] != 0:
                    print("occupied")
                    return

            for i in range(row1, row2 + step, step):
                self.list_location[i][col1] = 1 
                board.draw_ship_token(win, i, col1)
            pygame.mixer.Sound.play(self.ship_sound)
            return 0

    def check_attack(self, row, col, board, win):
        if self.list_revealed[row][col] == 0:
            self.list_revealed[row][col] = 1
            self.atk_attempts += 1
            self.reveal(row, col, board, win)

    def reveal(self, row, col, board, win):
        if self.list_location[row][col] == 1:
            pygame.mixer.Sound.play(self.cannon_sound)
            board.draw_sea_tile(win, row, col)
            board.draw_ship_token(win, row, col)
            self.ship_counter -= 1
        if self.list_location[row][col] == 0:
            board.draw_sea_tile(win, row, col)
            pygame.mixer.Sound.play(self.water_sound)

            
        

            
