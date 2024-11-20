from Enemy import Enemy


class Enemy_Handler:
    def __init__(self, Win):
        self.Win = Win
        self.enemies = []
        self.spawn_timer = 0

    def update(self, bullets):
        self.increment_timers()
        self.add_enemy()
        self.update_enemies(bullets)

    def update_enemies(self, bullets):
        for enemy in self.enemies:
            enemy.update()
            if enemy.is_hit(bullets):
                index = self.enemies.index(enemy)
                self.enemies.pop(index)

    def increment_timers(self):
        self.spawn_timer += 1

    def add_enemy(self):
        if self.spawn_timer % 200 == 0:
            self.enemies.append(Enemy(self.Win))

    def get_enemies(self):
        return self.enemies