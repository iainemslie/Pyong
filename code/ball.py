import pygame
from settings import *
from timer import Timer
from random import choice


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, group, collision_sprites, score):
        super().__init__(group)

        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=pos)

        self.collision_sprites = collision_sprites

        # movement
        self.direction = pygame.math.Vector2((choice([-1, 1]), 1))
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = BALL_SPEED

        self.timers = {
            'reset timer': Timer(1000),
        }

        self.score = score

    def reset_ball(self):
        if self.timers['reset timer'].active:
            if self.pos.x > SCREEN_WIDTH:
                self.score[0] += 1
            else:
                self.score[1] += 1
            self.pos.x = SCREEN_WIDTH // 2
            self.pos.y = SCREEN_HEIGHT // 2
            self.rect.centerx = self.pos.x
            self.rect.centery = self.pos.y
            self.direction.x *= -1
            self.timers['reset timer'].deactivate()

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
        if self.pos.y >= SCREEN_HEIGHT:
            self.pos.y = SCREEN_HEIGHT
            self.direction.y *= -1
        elif self.pos.y < 0:
            self.pos.y = 0
            self.direction.y *= -1

        if self.pos.x >= SCREEN_WIDTH + BALL_SIZE:
            self.timers['reset timer'].activate()
        elif self.pos.x < 0 - BALL_SIZE:
            self.timers['reset timer'].activate()

    def check_collision(self):
        for sprite in self.collision_sprites:
            if (sprite.rect.colliderect(self.rect)):
                if sprite.side == 'right':
                    self.pos.x = sprite.rect.centerx - (PLAYER_WIDTH * 2)
                    self.direction.x *= -1
                else:
                    self.pos.x = sprite.rect.centerx + (PLAYER_WIDTH * 2)
                    self.direction.x *= -1

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def update(self, dt):
        if not self.timers['reset timer'].active:
            self.check_collision()
            self.move(dt)
            self.check_bounds()
            self.update_timers()
            self.reset_ball()
