import pygame

class Ship:
    """Uma classe para gerenciar a espaçonave."""

    def __init__(self, ai_game):
        """Inicializa a espaçonave e define sua posição inicial."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega a imagem da espaçonave e obtém seu rect.
        self.image = pygame.image.load('imagens/ship.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela.
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazena um valor decimal para o atributo y da espaçonave.
        self.y = float(self.rect.y)

        # Flags de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza a posição da espaçonave com base nas flags de movimento."""
        # Atualiza o valor x da espaçonave, não o rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.y += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.y -= self.settings.ship_speed

        # Atualiza o rect object a partir de self.x.
        self.rect.y = self.y

    def blitme(self):
        """Desenha a espaçonave em sua posição atual."""
        self.screen.blit(self.image, self.rect)

