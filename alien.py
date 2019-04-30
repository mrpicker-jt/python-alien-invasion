import random

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """这是外星人"""

    def __init__(self, screen, settings):
        super().__init__()
        """初始化飞船并设置其初始位置"""

        self.ai_settings = settings

        self.speed_factor = settings.alien_speed_factor

        # 将外星人与视图绑定
        self.screen = screen

        # 加载外星人图像并获取其外接矩形
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = True

    def update(self):
        if self.moving_right:
            self.x += self.speed_factor / random.randint(1, 10)
            if self.rect.right > self.screen_rect.right:
                self.moving_right = False
        else:
            self.x -= self.speed_factor / random.randint(1, 10)
            if self.rect.left < self.screen_rect.left:
                self.moving_right = True
        self.y += self.speed_factor / random.randint(5, 10)

    def blitme(self):
        self.rect.x = self.x
        self.rect.y = self.y
        # 在指定的位置绘制外星人
        self.screen.blit(self.image, self.rect)

    def set_position(self, x, y):
        self.x = x
        self.y = y
