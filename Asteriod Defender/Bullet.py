import pygame
class Bullet:
    def __init__(self, Win, pos, angle):
        self.Win = Win
        self.pos = pygame.Vector2(pos[0], pos[1])
        self.vector = pygame.Vector2()
        self.angle = angle
        self.delta = 0
        self.speed = 10
        self.color = (200, 200, 200)

    def update(self):
        self.draw()
        self.move()

    def get_point(self, distance, angle):
        vector = pygame.Vector2()
        vector.from_polar((distance, angle))
        return vector + self.pos

    def draw(self):
        pygame.draw.circle(self.Win, self.color, self.pos, 2)

    def move(self):
        self.vector.from_polar((1, self.angle))
        self.pos += self.vector * self.speed

    def is_off_screen(self):
        return self.pos[0] < 0 or self.pos[0] > 600 or self.pos[1] < 0 or self.pos[1] > 600