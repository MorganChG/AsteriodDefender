import pygame

class TextPresenter:
    def __init__(self, Win):
        self.Win = Win

        self.font = pygame.font.SysFont('Consolas', 128)
        self.text_surface = None

        self.color = (100, 100, 100)

    def update_text(self, text):
        self.text_surface = self.font.render(text, True, self.color)

    def render_text(self):
        rect = self.text_surface.get_rect(center=(300,300))
        self.Win.blit(self.text_surface, rect)





