import pygame
from settings import *


class Computer(pygame.sprite.Sprite):
    def __init__(self, pos, group, ball):
        super().__init__(group)

        self.identity = 'computer'
        self.ball = ball

        self.image = pygame.Surface((16, 64))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=pos)

        # movement
        self.direction = pygame.math.Vector2((0, 0))
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 500

    def move(self, dt):
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def check_ball_position(self):
        self.pos.y = self.ball.rect.centery

    def check_bounds(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def update(self, dt):
        self.move(dt)
        self.check_ball_position()
