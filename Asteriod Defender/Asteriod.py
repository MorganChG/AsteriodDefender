import pygame, random, math
class Asteroid:
    def __init__(self, Win):
        self.Win = Win
        self.pos = pygame.Vector2(300, 300)

        self.color = (200, 200, 200)
        self.size = 150

        self.hit_boxes = []
        self.radi = []

        self.points = self.get_points()

        self.get_attributes()


    def update(self):
        self.draw()

    def draw(self):
        pygame.draw.polygon(self.Win, self.color, self.points, 2)

    def get_attributes(self):
        for point in self.points:
            middle_point = self.get_middle_point(point)
            self.add_middle_point(middle_point)
            self.get_radi(middle_point)

    def get_radi(self, middle_point):
        distance = self.distance_formula(middle_point[0], middle_point[1], self.pos[0], self.pos[1])
        self.radi.append(distance / 1.5)

    def add_middle_point(self, middle_point):
        self.hit_boxes.append(middle_point)

    def get_middle_point(self, point):
        middle_point = ((self.pos[0] + point[0]) / 2, (self.pos[1] + point[1]) / 2)
        return middle_point

    def get_points(self):
        angle = 0
        points = []
        while angle < 360:
            angle = self.update_angle(angle)
            points.append(self.get_point(self.pos, random.randint(math.floor(self.size / 1.75), self.size), angle))
        return points

    def update_angle(self, angle):
        return self.increment_angle(angle) if angle < 360 else 360

    def is_hit(self, bullets):
        for bullet in bullets:
            for i in range(len(self.hit_boxes)):
                if (bullet.pos[0] - self.hit_boxes[i][0]) ** 2 + (bullet.pos[1] - self.hit_boxes[i][1]) ** 2 < \
                        self.radi[i] ** 2:
                    bullets.pop(bullets.index(bullet))
                    return True
        return False

    def get_radius(self):
        radius = 0
        for point in self.points:
            point_distance_to_center = self.distance_formula(point[0], self.pos[0], point[1], self.pos[1])
            if point_distance_to_center > radius:
                radius = point_distance_to_center
        return radius

    @staticmethod
    def increment_angle(angle):
        return angle + random.randint(10, 50)

    @staticmethod
    def get_point(position, distance, angle):
        vector = pygame.Vector2()
        vector.from_polar((distance, angle))
        return vector + position

    @staticmethod
    def distance_formula(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
