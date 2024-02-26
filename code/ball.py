import pygame
from settings import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, group, collision_sprites):
        super().__init__(group)

        self.image = pygame.Surface((32, 32))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=pos)

        self.collision_sprites = collision_sprites

        # movement
        self.direction = pygame.math.Vector2((1, 1))
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 500

    def move(self, dt):
        if self.direction:
            self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def check_bounds(self):
        # check bounds
        if self.pos.y >= SCREEN_HEIGHT:
            self.pos.y = SCREEN_HEIGHT
            self.direction.y *= -1
        elif self.pos.y < 0:
            self.pos.y = 0
            self.direction.y *= -1
        # check bounds
        if self.pos.x >= SCREEN_WIDTH:
            # self.pos.x = SCREEN_WIDTH
            # self.direction.x *= -1
            print("computer scores")
        elif self.pos.x < 0:
            # self.pos.x = 0
            # self.direction.x *= -1
            print("player scores")

    def check_collision(self):
        for sprite in self.collision_sprites:
            if (sprite.rect.colliderect(self.rect)):
                if sprite.identity == 'player':
                    self.pos.x = sprite.rect.centerx - (PLAYER_WIDTH * 2)
                    self.direction.x *= -1
                else:
                    self.pos.x = sprite.rect.centerx + (PLAYER_WIDTH * 2)
                    self.direction.x *= -1

    def update(self, dt):
        self.check_collision()
        self.move(dt)
        self.check_bounds()
