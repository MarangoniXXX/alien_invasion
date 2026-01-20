import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Uma classe que administra projéteis disparados pela espaçonave."""

    def __init__(self, ai_game):
        """Cria um objeto para o projétil na posição atual da espaçonave."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # cria um retângulo para o projétil em (0, 0) e, em seguida, define a posição correta.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Armazena a posição do projétil como um valor decimal
        self.y = float(self.rect.y)

    def update(self):
        """Move o projétil para cima na tela."""
        # Atualiza a posição decimal do projétil
        self.y -= self.settings.bullet_speed
        # Atualiza a posição de rect
        self.rect.y = self.y   

    def draw_bullet(self):
        """Desenha o projétil na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)