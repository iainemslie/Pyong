import pygame
from settings import *
from random import randint
from entity import Entity


class Computer(Entity):
    def __init__(self, pos, group, ball):
        super().__init__(pos, group)

        self.side = 'left'
        self.ball = ball

    def check_ball_position(self):
        error = randint(-37, 37)
        self.speed = randint(300, 500)
        if self.ball.rect.centerx < SCREEN_WIDTH // 2:
            if self.ball.rect.centery > self.pos.y + error:
                self.direction.y = 1
            elif self.ball.rect.centery < self.pos.y + error:
                self.direction.y = -1
            else:
                self.direction.y = 0

    def update(self, dt):
        self.check_ball_position()
        self.move(dt)
        self.check_bounds(dt)
