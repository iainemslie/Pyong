import pygame
from settings import *
from timer import Timer


class Welcome:
    def __init__(self, start_game):
        self.display_surface = pygame.display.get_surface()

        self.num_players = 1

        self.start_game = start_game
        self.display_welcome_message()

        self.selection_timer = Timer(100)

    def display_welcome_message(self):
        # Pyong name
        font = pygame.font.Font("pixelfont.ttf", 64)
        welcome_string = "PYONG"
        text = font.render(welcome_string, False, 'white')
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.display_surface.blit(text, textRect)

        # 1P or 2P
        font = pygame.font.Font("pixelfont.ttf", 18)
        one_player_string = "1 Player"
        one_player_text = font.render(one_player_string, False, 'white')
        one_player_rect = one_player_text.get_rect()
        one_player_rect.center = (SCREEN_WIDTH * 4 // 10, SCREEN_HEIGHT // 2)
        self.display_surface.blit(one_player_text, one_player_rect)

        two_player_string = "2 Player"
        two_player_text = font.render(two_player_string, False, 'white')
        two_player_rect = two_player_text.get_rect()
        two_player_rect.center = (SCREEN_WIDTH * 6 // 10, SCREEN_HEIGHT // 2)
        self.display_surface.blit(two_player_text, two_player_rect)

        # selection rectangle
        if self.num_players == 1:
            select_rect = pygame.Rect(
                one_player_rect.left - 10, one_player_rect.top - 10, one_player_rect.w + 20, one_player_rect.h + 20)
            pygame.draw.rect(self.display_surface, 'white', select_rect, 4)
        elif self.num_players == 2:
            select_rect = pygame.Rect(
                two_player_rect.left - 10, two_player_rect.top - 10, two_player_rect.w + 20, two_player_rect.h + 20)
            pygame.draw.rect(self.display_surface, 'white', select_rect, 4)

        # Continue
        font = pygame.font.Font("pixelfont.ttf", 18)
        reset_string = "PRESS SPACEBAR TO START"
        reset_text = font.render(reset_string, False, 'white')
        reset_rect = reset_text.get_rect()
        reset_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 // 4)
        self.display_surface.blit(reset_text, reset_rect)

    def input(self):
        keys = pygame.key.get_pressed()
        self.selection_timer.update()

        if keys[pygame.K_SPACE]:
            self.start_game(self.num_players)

        if not self.selection_timer.active:
            if keys[pygame.K_RIGHT]:
                self.num_players = 2
                self.selection_timer.activate()
            if keys[pygame.K_LEFT]:
                self.num_players = 1
                self.selection_timer.activate()

    def run(self, dt):
        self.display_surface.fill('black')
        self.input()
        self.display_welcome_message()
