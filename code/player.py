import pygame
from settings import *
from entity import Entity


class Player(Entity):
    def __init__(self, pos, group, side):
        super().__init__(pos, group)

        self.controls = {'left': {'up': pygame.K_w, 'down': pygame.K_s},
                         'right': {'up': pygame.K_UP, 'down': pygame.K_DOWN}}

        self.side = side

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[self.controls[self.side]['up']]:
            self.direction.y = -1
        elif keys[self.controls[self.side]['down']]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def update(self, dt):
        self.input()
        self.move(dt)
        self.check_bounds(dt)
