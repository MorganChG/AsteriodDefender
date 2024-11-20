import pygame

from Asteroid_Handler import Asteroid_Handler
from Enemy_Handler import Enemy_Handler
from Player_Handler import Player_Handler
from TextPresenter import TextPresenter

class World:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.Win = pygame.display.set_mode((600,600), pygame.NOFRAME)

        self.asteroid_handler = Asteroid_Handler(self.Win)
        self.text_presenter = TextPresenter(self.Win)
        self.enemy_handler = Enemy_Handler(self.Win)

        self.player_handler = Player_Handler(self.Win, self.asteroid_handler.asteroid.get_radius())

        self.run = True

    def update(self):
        while self.run:
            self.check_for_events()
            self.update_background()

            self.player_handler.update()
            self.enemy_handler.update(self.player_handler.get_bullets())
            self.asteroid_handler.update(self.enemy_handler.get_enemies())
            self.text_presenter.update_text(str(self.asteroid_handler.get_HP()))
            self.text_presenter.render_text()

            self.update_screen()
            self.update_clock()

    def check_for_events(self):
        for event in pygame.event.get():
            self.run = not self.is_exit_pressed(event)

    def update_clock(self):
        self.clock.tick(60)

    def update_background(self):
        self.Win.fill((40, 40, 40))

    @staticmethod
    def update_screen():
        pygame.display.update()

    @staticmethod
    def is_exit_pressed(event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                return True
        return False