import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """这是外星人"""

    def __init__(self, screen, settings):
        super().__init__()
        """初始化飞船并设置其初始位置"""

        self.ai_settings = settings

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

    def blitme(self):
        # 在指定的位置绘制外星人
        self.screen.blit(self.image, self.rect)
