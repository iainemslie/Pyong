import pygame
from settings import *


class Welcome:
    def __init__(self, start_game):
        self.display_surface = pygame.display.get_surface()

        self.start_game = start_game

        self.display_welcome_message()

    def display_welcome_message(self):

        # Pyong name
        font = pygame.font.Font("pixelfont.ttf", 64)
        welcome_string = "PYONG"
        text = font.render(welcome_string, False, 'white')
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.display_surface.blit(text, textRect)

        # Continue
        font = pygame.font.Font("pixelfont.ttf", 18)
        reset_string = "PRESS SPACEBAR TO START"
        reset_text = font.render(reset_string, False, 'white')
        reset_rect = reset_text.get_rect()
        reset_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 // 4)
        self.display_surface.blit(reset_text, reset_rect)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.start_game()

    def run(self, dt):
        self.input()
