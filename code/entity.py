import pygame
from settings import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.identity = None

        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=pos)

        # movement
        self.direction = pygame.math.Vector2((0, 0))
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = PLAYER_SPEED

    def move(self, dt):
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def check_bounds(self, dt):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.pos.y -= self.direction.y * self.speed * dt
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.pos.y -= self.direction.y * self.speed * dt
