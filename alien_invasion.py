import sys
import pygame 
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamento do jogo."""

    def __init__(self):
        """Inicializa o jogo e cria recursos do jogo."""
        pygame.init()
        self.settings = Settings()

        # Cria a janela do jogo
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Cria a nave
        self.ship = Ship(self)

        # Relógio para controlar FPS
        self.clock = pygame.time.Clock()

    def run_game(self):
        """Inicia o loop principal do jogo."""
        while True:
            # Observa eventos de teclado e de mouse.
            self._check_events()
            
            # Atualiza a posição da nave
            self.ship.update()

            # Atualiza a tela
            self._update_screen()
            self.clock.tick(60)
    
    def _update_screen(self):
        """Atualiza as imagens na tela e alterna para a nova tela."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()   

    def _check_events(self):
        """Responde a eventos de pressionamento de teclas e de mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responde a pressionamentos de tecla."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """Responde a solturas de tecla."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


if __name__ == '__main__':
    # Cria uma instância e executa o jogo.
    ai = AlienInvasion()
    ai.run_game()


