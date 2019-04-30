# 存放alien_invasion所有设置的模块

class Settings:
    """docstring for Settings"""

    def __init__(self):
        self.title = 'Alien Invasion'
        self.width = 1200
        self.height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 2

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 160, 60, 160
        self.bullets_allowed = 9

        # 外星人设置
        self.alien_speed_factor = 1
