from Bullet import Bullet
import pygame, math


class Ship:
    def __init__(self, Win, radius):
        self.Win = Win
        self.radius = radius

        self.facing_point = ()
        self.left_point = ()
        self.right_point = ()

        self.color = (200, 200, 200)

        self.size = 20
        self.speed = 1
        self.facing_angle = 0
        self.circle_angle = 0
        self.acc = 0

        self.pos = self.get_pos()
        self.get_points()

        self.bullets = []

    def update(self):
        self.get_points()
        self.draw()
        self.update_pos()
        self.update_facing_angle()
        self.update_bullets()

    def update_facing_angle(self):
        self.facing_angle = self.get_angle() + 180

    def draw(self):
        pygame.draw.line(self.Win, self.color, self.facing_point, self.left_point, 2)
        pygame.draw.line(self.Win, self.color, self.facing_point, self.right_point, 2)

        pygame.draw.line(self.Win, self.color, self.pos, self.right_point, 2)
        pygame.draw.line(self.Win, self.color, self.pos, self.left_point, 2)

        #pygame.draw.circle(Win, self.color, (300, 300), self.radius, 2)

    def rotate_left(self):
        self.circle_angle -= 0.025

    def rotate_right(self):
        self.circle_angle += 0.025

    def get_angle(self):
        x, y = self.pos
        x2, y2 = (300,300)
        deltaX = x2 - x
        deltaY = y2 - y
        return math.atan2(deltaY, deltaX) * (180 / 3.14)

    def get_points(self):
        self.facing_point = self.get_point(self.size, self.facing_angle)
        self.left_point = self.get_point(self.size, self.facing_angle - 225)
        self.right_point = self.get_point(self.size, self.facing_angle + 225)

    def get_point(self, distance, angle):
        vector = pygame.Vector2()
        vector.from_polar((distance, angle))
        return vector + self.pos

    def get_pos(self):
        x = 300 + self.radius * math.cos(self.circle_angle)
        y = 300 + self.radius * math.sin(self.circle_angle)
        return x,y

    def get_bullets(self):
        return self.bullets

    def add_bullet(self):
        self.bullets.append(Bullet(self.Win,self.facing_point, self.facing_angle))

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.update()
            if bullet.is_off_screen():
                index = self.bullets.index(bullet)
                self.bullets.pop(index)

    def update_pos(self):
        self.pos = self.get_pos()