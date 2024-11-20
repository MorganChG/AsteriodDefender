import pygame

from Asteriod import Asteroid
from Enemy_Handler import Enemy_Handler
from Player_Handler import Player_Handler

pygame.init()

Win = pygame.display.set_mode((600,600), pygame.NOFRAME)
clock = pygame.time.Clock()

def main():
    run = True
    asteroid = Asteroid(Win)
    player = Player_Handler(Win,asteroid.get_radius())
    enemies = Enemy_Handler(Win)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    run = False
        Win.fill((40,40,40))
        asteroid.update()
        player.update()
        enemies.update(player.get_bullets())
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()