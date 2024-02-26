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

        # score
        self.font = pygame.font.Font("pixelfont.ttf")
        self.score = [0, 0]
        self.score_string = f"{self.score[0]} : {self.score[1]}"
        self.text = self.font.render(self.score_string, False, 'white')
        self.textRect = self.text.get_rect()
        self.textRect.center = (SCREEN_WIDTH / 2, 16)

        self.setup()

    def setup(self):
        ball = Ball((480, 270), self.all_sprites,
                    self.collision_sprites)
        player1 = Player(
            (900, 270), (self.all_sprites, self.collision_sprites))
        computer = Computer(
            (60, 270), (self.all_sprites, self.collision_sprites))

    def update_score(self):
        self.score_string = f"{self.score[0]} : {self.score[1]}"

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
        self.update_score()
        self.display_surface.blit(self.text, self.textRect)
