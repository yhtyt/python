import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        # 加载图片
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self, *args):
        self.x += (self.ai_settings.alien_speed *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right > screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
