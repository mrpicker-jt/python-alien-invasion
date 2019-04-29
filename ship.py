import pygame


class Ship:
    """这是飞船类"""

    def __init__(self, screen, settings):
        """初始化飞船并设置其初始位置"""

        self.ai_settings = settings

        # 将飞船与视图绑定
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 确定飞船位置在底部居中
        self.center = float(self.screen_rect.centerx)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.movingRight = False
        self.movingLeft = False

    def update_self(self):
        # 这里更新center而不是centerx，因为rect.centerx只能是整数值，所以需要float的center满足带小数的速度
        if self.movingRight and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.movingLeft and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        # 在指定的位置绘制飞船
        self.screen.blit(self.image, self.rect)
