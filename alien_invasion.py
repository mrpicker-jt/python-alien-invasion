import time

import pygame

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption(settings.title)

    ship = Ship(screen, settings)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.handle_events(ship)
        ship.update_self()
        gf.update_screen(screen, settings, ship)
        time.sleep(0.002)


run_game()
