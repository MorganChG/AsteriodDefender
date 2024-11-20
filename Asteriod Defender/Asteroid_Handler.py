from Asteroid import Asteroid

class Asteroid_Handler:
    def __init__(self, Win):
        self.asteroid = Asteroid(Win)
        self.HP = 5

    def update(self, bullets):
        self.asteroid.update()
        self.decrement_HP(bullets)

    def decrement_HP(self, bullets):
        if self.asteroid.is_hit(bullets):
            self.HP -= 1

    def get_HP(self):
        return self.HP