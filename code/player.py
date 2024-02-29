import pygame
from settings import *
from entity import Entity


class Player(Entity):
    def __init__(self, pos, group):
        super().__init__(pos, group)

        self.side = 'right'

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def update(self, dt):
        self.input()
        self.move(dt)
        self.check_bounds(dt)
