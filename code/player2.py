import pygame
from settings import *


class Player2(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.identity = 'computer'

        self.image = pygame.Surface((16, 64))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=pos)

        # movement
        self.direction = pygame.math.Vector2((0, 0))
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 500

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def move(self, dt):
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def check_bounds(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def update(self, dt):
        self.input()
        self.move(dt)
        self.check_bounds()
