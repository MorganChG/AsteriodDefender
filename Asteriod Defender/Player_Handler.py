from Ship import Ship
import pygame


class Player_Handler:
    def __init__(self, Win, radius):
        self.player = Ship(Win,radius)
        self.pressed = False

    def update(self):
        self.move()
        self.player.update()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.rotate_left()
        elif keys[pygame.K_RIGHT]:
            self.player.rotate_right()

        if keys[pygame.K_SPACE] and not self.pressed:
            self.pressed = True
            self.player.add_bullet()
        elif not keys[pygame.K_SPACE]:
            self.pressed = False

    def get_bullets(self):
        return self.player.get_bullets()