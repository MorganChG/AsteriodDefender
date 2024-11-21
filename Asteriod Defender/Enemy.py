from Bullet import Bullet

import pygame, math, random

class Enemy:
    def __init__(self, Win):
        self.Win = Win
        self.size = 20
        self.width = 2
        self.shoot_timer = 0
        self.pos = self.get_position()
        self.vector = pygame.Vector2()
        self.color = (200,200,200)

        self.facing_angle = self.get_angle()
        self.facing_point = pygame.Vector2()

        self.hit_box = pygame.Rect(0,0,self.size * 2,self.size * 2)

        self.inside_points = []
        self.outside_points = []
        self.bullets = []
        self.get_points()

    def update(self):
        self.increment_shoot_timer()
        self.get_points()
        self.update_hit_box_pos()
        self.update_bullets()
        self.draw()
        self.can_move()
        self.can_shoot()

    def can_move(self):
        if not self.is_at_distance():
            self.move()

    def update_hit_box_pos(self):
        self.hit_box.center = self.pos

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.update()
            if bullet.is_off_screen():
                index = self.bullets.index(bullet)
                self.bullets.pop(index)

    def move(self):
        self.vector.from_polar((1, self.facing_angle))
        self.pos += self.vector * 1

    def draw(self):
        self.draw_inner_box()
        self.draw_wings()
        self.draw_gun()

    def draw_gun(self):
        pygame.draw.line(self.Win, self.color, self.pos, self.facing_point, self.width)

    def draw_wings(self):
        for i in range(len(self.outside_points)):
            pygame.draw.line(self.Win, self.color, self.outside_points[i], self.inside_points[i], self.width)
        pygame.draw.line(self.Win, self.color, self.outside_points[0], self.outside_points[-1], self.width)
        pygame.draw.line(self.Win, self.color, self.outside_points[1], self.outside_points[-2], self.width)

    def draw_inner_box(self):
        for i in range(len(self.inside_points)):
            pygame.draw.line(self.Win, self.color, self.inside_points[i - 1], self.inside_points[i], 1)

    def get_points(self):
        self.inside_points = []
        self.outside_points = []
        self.facing_point = self.get_point(self.size / 2, self.facing_angle)
        angle = 45 + (self.facing_angle - 90)
        for i in range(4):
            self.inside_points.append(self.get_point(self.size / 2, angle))
            self.outside_points.append(self.get_point(self.size, angle))
            angle += 90

    def get_point(self, distance, angle):
        vector = pygame.Vector2()
        vector.from_polar((distance, angle))
        return vector + self.pos

    def get_angle(self):
        x, y = self.pos
        x2, y2 = (300, 300)
        deltaX = x2 - x
        deltaY = y2 - y
        return math.atan2(deltaY, deltaX) * (180 / 3.14)

    def get_position(self):
        x,y = 0,0
        match self.get_side(["T", "B", "L", "R"]):
            case "T":
                x = random.randint(0, 600)
                y = 0 - self.size
            case "B":
                x = random.randint(0, 600)
                y = 600 + self.size
            case "L":
                x = 0 - self.size
                y = random.randint(0, 600)
            case "R":
                x = 600 + self.size
                y = random.randint(0, 600)
        return pygame.Vector2(x,y)

    def add_bullet(self):
        self.bullets.append(Bullet(self.Win,self.facing_point, self.facing_angle))

    def is_at_distance(self):
        return self.get_distance(self.pos[0], self.pos[1], 300, 300) < 275

    def is_hit(self, bullets):
        for bullet in bullets:
            if self.hit_box.collidepoint(bullet.pos):
                bullets.pop(bullets.index(bullet))
                return True
        return False

    @staticmethod
    def get_side(sides):
        return random.choice(sides)

    @staticmethod
    def get_distance(x, y, x2, y2):
        return math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2)

    def increment_shoot_timer(self):
        self.shoot_timer += 1

    def can_shoot(self):
        if self.shoot_timer % 100 == 0:
            self.add_bullet()
