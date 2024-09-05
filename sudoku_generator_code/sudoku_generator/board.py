import pygame
import random
from .constants import SQUARE_SIZE, GREEN, YELLOW, RED, BLACK, ROWS, COLS, WHITE, FONT_SANS, WIDTH, HEIGHT

pygame.init()

class Board():

    def __init__(self, win):
        #first screen
        self.win = win
        self.draw_diff_select()
        self.sdk_board = [
                        [],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0]
                        ]

    def draw_diff_select(self):
        pygame.draw.rect(self.win, GREEN, pygame.Rect(SQUARE_SIZE, SQUARE_SIZE * 4, SQUARE_SIZE, SQUARE_SIZE))
        pygame.draw.rect(self.win, YELLOW, pygame.Rect(SQUARE_SIZE * 4, SQUARE_SIZE * 4, SQUARE_SIZE, SQUARE_SIZE))
        pygame.draw.rect(self.win, RED, pygame.Rect(SQUARE_SIZE * 7, SQUARE_SIZE * 4, SQUARE_SIZE, SQUARE_SIZE))
        #text
        text = FONT_SANS.render("Easy", 1, "black")
        self.win.blit(text, (SQUARE_SIZE, SQUARE_SIZE * 4))
        text = FONT_SANS.render("Mid", 1, "black")
        self.win.blit(text, (SQUARE_SIZE * 4, SQUARE_SIZE * 4))
        text = FONT_SANS.render("Hard", 1, "black")
        self.win.blit(text, (SQUARE_SIZE * 7, SQUARE_SIZE * 4))

    def generate_sudoku(self, min_blank):
        list = [1,2,3,4,5,6,7,8,9]
        random.shuffle(list)
        random.shuffle(list)
        #print(list)
        for i in list:
            self.sdk_board[0].append(i)

        col = random.randrange(1, 9)
        done = False

        while done == False:
            list = [1,2,3,4,5,6,7,8,9]
            random.shuffle(list)
            random.shuffle(list)
            for i in range(len(self.sdk_board)):
                for j in range(len(list)):
                    if self.check_valid(self.sdk_board, list[j], (col,i)):
                        self.sdk_board[col][i] = list[j]
                        list.pop(j)
                        break
            if self.sdk_board[col][8] != 0:
                done = True

        self.solve()
        #add blank spaces
        for i in range(len(self.sdk_board)):
            num_blank = random.randrange(min_blank, 9)
            list = [0,1,2,3,4,5,6,7,8]
            random.shuffle(list)
            random.shuffle(list)
            for j in range(num_blank):
                self.sdk_board[i][list[j]] = 0
        


    def draw_sudoku(self):
        self.win.fill(WHITE)
        #draw numbers
        for row in range(ROWS):
            for col in range(COLS):
                if self.sdk_board[row][col] == 0:
                    pass
                else:
                    text = FONT_SANS.render(str(self.sdk_board[row][col]), 1, "black")
                    self.win.blit(text, (col * SQUARE_SIZE + 40, row * SQUARE_SIZE + 30))
        #draw lines
        bigLine = WIDTH // 3
        smallLine = WIDTH // 9

        for i in range(bigLine, WIDTH, bigLine):
            pygame.draw.rect(self.win, BLACK, pygame.Rect((i - 5, 0, 10, WIDTH)))
            pygame.draw.rect(self.win, BLACK, pygame.Rect((0, i - 5, WIDTH, 10)))
        for i in range(smallLine, WIDTH, smallLine):
            pygame.draw.rect(self.win, BLACK, pygame.Rect((i - 1, 0, 2, WIDTH)))
            pygame.draw.rect(self.win, BLACK, pygame.Rect((0, i - 1, WIDTH, 2)))
        #draw solve_text
        text = FONT_SANS.render("Click Here To Solve", 1, "black")
        self.win.blit(text, (WIDTH/2 - 130, HEIGHT - 65))

                
        

    def print_board(self, bo):
        for i in range(len(bo)):
            print("")
            if i % 3 == 0 and i != 0 :
                print("- - - - - - - - - - - - -")
            for j in range(len(bo[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end = " ") 
                
                print(bo[i][j] , end = " ")


    def find_empty(self, bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i,j)
        return None

    def check_valid(self, bo, num, pos):
        #check row
        for i in range(len(bo[0])):
            if bo[pos[0]][i] == num and pos[1] != i:
                return False
        #check col
        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False
        #check the square
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_x * 3, box_x * 3 + 3):
            for j in range(box_y * 3, box_y * 3 + 3):
                if bo[j][i] == num and pos != (j, i):
                    return False

        return True

    def solve(self):
        find = self.find_empty(self.sdk_board)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.check_valid(self.sdk_board, i, (row, col)):
                self.sdk_board[row][col] = i
                #print_board(bo)
                #print("\n")
                
                if self.solve():
                    return True

                self.sdk_board[row][col] = 0
                #print_board(bo)
                #print("\n")

        return False

