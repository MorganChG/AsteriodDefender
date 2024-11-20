from Asteroid import Asteroid

class Asteroid_Handler:
    def __init__(self, Win):
        self.asteroid = Asteroid(Win)
        self.HP = 5

    def update(self, enemies):
        self.asteroid.update()
        self.can_lose_HP(enemies)

    def can_lose_HP(self, enemies):
        if self.is_hit(enemies):
            self.decrement_HP()


    def decrement_HP(self):
        self.HP -= 1

    def is_hit(self, enemies):
        for enemy in enemies:
            if self.asteroid.is_hit(enemy.bullets):
                return True
        return False

    def get_HP(self):
        return self.HP