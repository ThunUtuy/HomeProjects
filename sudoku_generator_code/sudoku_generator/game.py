import pygame
from .board import Board

class Game():

    def __init__(self, win):
        self.game_stage = 1
        self.win = win
        self.board = Board(self.win)


    def select(self, row, col):
        
        if self.game_stage == 1:
            print(row,col)
            #diff select
            if (row,col) == (4, 1):
                self.board.generate_sudoku(2)
                self.game_stage += 1
            if (row,col) == (4, 4):
                self.board.generate_sudoku(3)
                self.game_stage += 1
            if (row,col) == (4, 7):
                self.board.generate_sudoku(4)
                self.game_stage += 1

            if self.game_stage == 2:
                self.board.draw_sudoku()

        if self.game_stage == 2:
            if row == 9:
                self.board.solve()
                self.board.draw_sudoku()
                self.game_stage += 1
        
            
            
