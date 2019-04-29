import time

import pygame
from pygame.sprite import Group

import game_functions as gf
from alien import Alien
from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption(settings.title)

    ship = Ship(screen, settings)
    alien = Alien(screen, settings)
    # 创建一个子弹组
    bullets = Group()
    aliens = Group()

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.handle_events(settings, screen, ship, bullets)
        ship.update_self()
        gf.update_bullets(bullets)
        gf.update_screen(screen, settings, ship, bullets, alien)
        time.sleep(0.002)


run_game()
