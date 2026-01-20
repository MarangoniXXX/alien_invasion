import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamento do jogo."""

    def __init__(self):
        """Inicializa o jogo e cria recursos do jogo."""
        pygame.init()
        self.settings = Settings()

        # Tela cheia
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Nave e projéteis
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Controle de FPS
        self.clock = pygame.time.Clock()

    def run_game(self):
        """Inicia o loop principal do jogo."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._remove_offscreen_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _remove_offscreen_bullets(self):
        """Remove projéteis que saíram da tela."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Atualiza as imagens na tela."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def _check_events(self):
        """Responde a eventos de teclado."""
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
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responde a solturas de tecla."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Cria um novo projétil se o limite não foi atingido."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

