import sys

import pygame

from bullet import Bullet


def handle_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire_bullets(ai_settings, screen, ship, bullets)
            if event.key == pygame.K_RIGHT:
                ship.movingRight = True
            if event.key == pygame.K_LEFT:
                ship.movingLeft = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.movingRight = False
            if event.key == pygame.K_LEFT:
                ship.movingLeft = False


def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        bullets.add(Bullet(ai_settings, screen, ship))


def update_bullets(bullets):
    bullets.update()
    # 删除已经出上边界的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)


def update_screen(screen, settings, ship, bullets):
    screen.fill(settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
