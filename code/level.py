import pygame
from ball import Ball
from player import Player


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.player1 = Player(
            (900, 270), (self.all_sprites, self.collision_sprites))
        self.ball = Ball((480, 270), self.all_sprites, self.collision_sprites)

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
