import pygame
from ball import Ball
from player import Player
from computer import Computer
from settings import *


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.game_over = False
        self.winner = None

        # score
        self.font = pygame.font.Font("pixelfont.ttf")
        self.score = [0, 0]
        self.score_string = f"{self.score[0]} : {self.score[1]}"
        self.text = self.font.render(self.score_string, False, 'white')
        self.textRect = self.text.get_rect()
        self.textRect.center = (SCREEN_WIDTH / 2, 16)

        self.setup()

    def setup(self):
        ball = Ball((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), self.all_sprites,
                    self.collision_sprites, self.score)
        player1 = Player(
            (SCREEN_WIDTH - 60, SCREEN_HEIGHT // 2), (self.all_sprites, self.collision_sprites))
        computer = Computer(
            (60, SCREEN_HEIGHT // 2), (self.all_sprites, self.collision_sprites))

    def reset(self):
        self.__init__()

    def update_score(self):
        self.score_string = f"{self.score[0]} : {self.score[1]}"
        self.text = self.font.render(self.score_string, False, 'white')

    def check_score(self):
        if self.score[0] > SCORE_TO_WIN:
            self.winner = "COMPUTER"
            self.game_over = True
        elif self.score[1] > SCORE_TO_WIN:
            self.winner = "PLAYER"
            self.game_over = True

    def display_winner(self):
        win_string = f"{self.winner} WINS!"
        winner_text = self.font.render(win_string, False, 'white')
        winner_rect = winner_text.get_rect()
        winner_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.display_surface.blit(winner_text, winner_rect)

        reset_string = "PRESS SPACEBAR TO RESET"
        reset_text = self.font.render(reset_string, False, 'white')
        reset_rect = reset_text.get_rect()
        reset_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 // 4)
        self.display_surface.blit(reset_text, reset_rect)

    def check_gameover_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.reset()

    def run(self, dt):
        if not self.game_over:
            self.display_surface.fill('black')
            self.all_sprites.draw(self.display_surface)
            self.all_sprites.update(dt)
            self.update_score()
            self.check_score()
            self.display_surface.blit(self.text, self.textRect)
        else:
            self.display_winner()
            self.check_gameover_input()
