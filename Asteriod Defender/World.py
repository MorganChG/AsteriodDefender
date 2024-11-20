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

            self.update_player()
            self.update_enemies()
            self.update_asteroid()
            self.update_text_presenter()

            self.on_game_over()

            self.update_screen()
            self.update_clock()

    def update_text_presenter(self):
        self.text_presenter.update_text(str(self.asteroid_handler.get_HP()))
        self.text_presenter.render_text()

    def update_asteroid(self):
        self.asteroid_handler.update(self.enemy_handler.get_enemies())

    def update_enemies(self):
        self.enemy_handler.update(self.player_handler.get_bullets())

    def update_player(self):
        self.player_handler.update()

    def check_for_events(self):
        for event in pygame.event.get():
            self.run = not self.is_exit_pressed(event)

    def update_clock(self):
        self.clock.tick(60)

    def update_background(self):
        self.Win.fill((40, 40, 40))

    def reset(self):
        self.asteroid_handler = Asteroid_Handler(self.Win)
        self.text_presenter = TextPresenter(self.Win)
        self.enemy_handler = Enemy_Handler(self.Win)

        self.player_handler = Player_Handler(self.Win, self.asteroid_handler.asteroid.get_radius())

    def on_game_over(self):
        if self.is_game_over():
            self.reset()

    def is_game_over(self):
        return self.asteroid_handler.is_dead()

    @staticmethod
    def update_screen():
        pygame.display.update()

    @staticmethod
    def is_exit_pressed(event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                return True
        return False