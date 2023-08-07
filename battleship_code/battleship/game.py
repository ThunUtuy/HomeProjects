import pygame
from .constants import BLUE, LIGHT_BLUE, FONT, WHITE, BLACK
from .board import Board
from .player import Player
pygame.font.init()
pygame.mixer.init()

class Game:
    def __init__(self, win):
        self.game_stage = 1
        self.win = win
        self.player1_ships = 0
        self.player2_ships = 0
        self.player_ship_length = 5
        self.board = Board(win)
        self.player1 = Player()
        self.player2 = Player()
        text = FONT.render("Player 1 deploy", 1, "white")
        self.win.blit(text, (50, 630))
        ship_length_text = FONT.render(f"ship_length {self.player_ship_length}",1,"white")
        self.win.blit(ship_length_text, (350, 630))
        self.win_sound_1 = pygame.mixer.Sound("sounds/player1_won.mp3")
        self.win_sound_2 = pygame.mixer.Sound("sounds/player2_won.mp3")
        #sound

    def select(self, row1, col1, row2, col2):
        if self.game_stage == 1:
            if self.player1_ships < 4:
                if self.player1.check_ship_valid(row1, col1, row2, col2, self.player_ship_length, self.board, self.win) == 0:
                    self.player1_ships += 1
                    self.player_ship_length -= 1
                    print("ships deployed: ", self.player1_ships)
                    print(self.player1.list_location)
                #text below
                if self.player_ship_length > 1:
                    ship_length_text = FONT.render(f"ship_length {self.player_ship_length}",1,"white")
                    pygame.draw.rect(self.win, BLUE, (350, 600, 250, 100))
                else:
                    ship_length_text = FONT.render(f"done!",1,"white")
                    pygame.draw.rect(self.win, BLUE, (350, 600, 250, 100))
                self.win.blit(ship_length_text, (350, 630))
                self.board.draw_small_circle(self.win, row1, col1)
                self.board.draw_small_circle_black(self.win, row2, col2)
            else:
                self.game_stage += 1
                self.player_ship_length = 5
                self.board.draw_squares(self.win)
                self.board.draw_small_circle(self.win, row1, col1)
                self.board.draw_small_circle_black(self.win, row2, col2)
                text = FONT.render("Player 2 deploy", 1, "white")
                self.win.blit(text, (50, 630))
                ship_length_text = FONT.render(f"ship_length {self.player_ship_length}",1,"white")
                self.win.blit(ship_length_text, (350, 630))
                return

        
        if self.game_stage == 2:
            if self.player2_ships < 4:
                if self.player2.check_ship_valid(row1, col1, row2, col2, self.player_ship_length, self.board, self.win) == 0:
                    self.player2_ships += 1
                    self.player_ship_length -= 1
                    print("ships deployed: ", self.player1_ships)
                    print(self.player2.list_location)
                #text below
                if self.player_ship_length > 1:
                    ship_length_text = FONT.render(f"ship_length {self.player_ship_length}",1,"white")
                    pygame.draw.rect(self.win, BLUE, (350, 600, 250, 100))
                else:
                    ship_length_text = FONT.render(f"done!",1,"white")
                    pygame.draw.rect(self.win, BLUE, (350, 600, 250, 100))
                self.win.blit(ship_length_text, (350, 630))
                self.board.draw_small_circle(self.win, row1, col1)
                self.board.draw_small_circle_black(self.win, row2, col2)
            else:
                self.game_stage += 1
                self.board.draw_squares_black(self.win)
                text = FONT.render("Player 1 attack", 1, "white")
                self.win.blit(text, (50, 630))
                text = FONT.render(f"ship_counter {self.player2.ship_counter}",1,"white")
                pygame.draw.rect(self.win, BLACK, (350, 600, 250, 100))
                self.win.blit(text, (350, 630))
                return

        if self.game_stage == 4:
            if self.player1.ship_counter > 0:
                self.player1.check_attack(row1, col1, self.board, self.win)

                text = FONT.render(f"ship_counter {self.player1.ship_counter}",1,"white")
                pygame.draw.rect(self.win, BLACK, (350, 600, 250, 100))
                self.win.blit(text, (350, 630))
            else:
                self.game_stage += 1
                self.board.draw_squares_black(self.win)
                text = FONT.render("The Battle's Finished, Click For The Result", 1, "white")
                self.win.blit(text, (0, 610))
                return

        if self.game_stage == 3:
            if self.player2.ship_counter > 0:
                self.player2.check_attack(row1, col1, self.board, self.win)

                text = FONT.render(f"ship_counter {self.player2.ship_counter}",1,"white")
                pygame.draw.rect(self.win, BLACK, (350, 600, 250, 100))
                self.win.blit(text, (350, 630))
            else:
                self.game_stage += 1
                self.board.draw_squares_black(self.win)
                text = FONT.render("Player 2 attack", 1, "white")
                self.win.blit(text, (50, 630))
                text = FONT.render(f"ship_counter {self.player1.ship_counter}",1,"white")
                pygame.draw.rect(self.win, BLACK, (350, 600, 250, 100))
                self.win.blit(text, (350, 630))
                return

        if self.game_stage == 5:
            player1_text = FONT.render(f"player1 attempts {self.player2.atk_attempts}",1,"white")
            player2_text = FONT.render(f"player2 attempts {self.player1.atk_attempts}",1, "white")
            print("player2 attempts", self.player1.atk_attempts)
            print("player1 attempts", self.player2.atk_attempts)
            if self.player1.atk_attempts == self.player2.atk_attempts:
                text = FONT.render("An Equal Fight", 1, "white")
                self.win.blit(text, (200, 200))
                pygame.mixer.Sound.play(self.win_sound_1)
            elif self.player1.atk_attempts > self.player2.atk_attempts:
                text = FONT.render("Player 1 Won", 1, "white")
                self.win.blit(text, (200, 200))
                pygame.mixer.Sound.play(self.win_sound_2)
            else:
                text = FONT.render("Player 2 Won", 1, "white")
                self.win.blit(text, (200, 200))
                pygame.mixer.Sound.play(self.win_sound_2)
            self.win.blit(player1_text, (200, 300))
            self.win.blit(player2_text, (200, 400))

            return 0
        



            