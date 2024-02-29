import pygame
from settings import *
from random import randint


class Computer(pygame.sprite.Sprite):
    def __init__(self, pos, group, ball):
        super().__init__(group)

        self.identity = 'computer'
        self.ball = ball

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

    def check_ball_position(self):
        error = randint(-40, 40)
        self.speed = randint(300, 500)
        if self.ball.rect.centerx < SCREEN_WIDTH // 2:
            if self.ball.rect.centery > self.pos.y + error:
                self.direction.y = 1
            elif self.ball.rect.centery < self.pos.y + error:
                self.direction.y = -1
            else:
                self.direction.y = 0

    def check_bounds(self, dt):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.pos.y -= self.direction.y * self.speed * dt
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.pos.y -= self.direction.y * self.speed * dt

    def update(self, dt):
        self.check_ball_position()
        self.move(dt)
        self.check_bounds(dt)
