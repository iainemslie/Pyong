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
        error = randint(-30, 30)
        self.speed = randint(300, 500)
        notice_range = randint(SCREEN_WIDTH // 2, SCREEN_WIDTH * 3 // 4)
        if self.ball.rect.centerx < notice_range:
            if self.ball.rect.centery > self.pos.y + error:
                self.direction.y = 1
            elif self.ball.rect.centery < self.pos.y + error:
                self.direction.y = -1
            else:
                self.direction.y = 0
        else:
            self.direction *= 0

    def update(self, dt):
        self.check_ball_position()
        self.move(dt)
        self.check_bounds(dt)
