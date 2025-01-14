import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, screen, ai_settings):
        """初始化飞船的位置"""
        super().__init__()
        self.screen = screen
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        '''将飞船放在底部中央'''
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_left and self.rect.centerx > 0:
            self.centerx -= self.ai_settings.ship_speed
        if self.move_right and self.rect.centerx < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed
        if self.move_up and self.rect.centery > 0:
            self.centery -= self.ai_settings.ship_speed
        if self.move_down and self.rect.centery < self.ai_settings.screen_height:
            self.centery += self.ai_settings.ship_speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def center_ship(self):
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom - 20