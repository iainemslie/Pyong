import pygame
from settings import *
from entity import Entity


class Player2(Entity):
    def __init__(self, pos, group):
        super().__init__(pos, group)

        self.side = 'left'

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def update(self, dt):
        self.input()
        self.move(dt)
        self.check_bounds(dt)
