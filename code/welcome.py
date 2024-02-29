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
        self.write_message((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3), "PYONG", 64)

        # 1P or 2P
        one_player_rect = self.write_message(
            (SCREEN_WIDTH * 4 // 10, SCREEN_HEIGHT // 2), "1 Player", 18)
        two_player_rect = self.write_message(
            (SCREEN_WIDTH * 6 // 10, SCREEN_HEIGHT // 2), "2 Player", 18)

        # selection rectangle
        self.draw_selection_rect(
            one_player_rect) if self.num_players == 1 else self.draw_selection_rect(two_player_rect)

        # Continue
        self.write_message((SCREEN_WIDTH / 2, SCREEN_HEIGHT *
                           2 // 3), "PRESS SPACEBAR TO START", 18)

    def write_message(self, pos, message, font_size):
        font = pygame.font.Font("pixelfont.ttf", font_size)
        text = font.render(message, False, 'white')
        text_rect = text.get_rect()
        text_rect.center = pos
        self.display_surface.blit(text, text_rect)
        return text_rect

    def draw_selection_rect(self, selected):
        select_rect = pygame.Rect(
            selected.left - 10, selected.top - 10, selected.w + 20, selected.h + 20)
        pygame.draw.rect(self.display_surface, 'white', select_rect, 4)

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
