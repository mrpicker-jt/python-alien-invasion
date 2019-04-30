import sys

import pygame

from alien import Alien
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


def update_aliens(aliens):
    aliens.update()
    for alien in aliens.copy():
        if alien.rect.top > alien.screen_rect.bottom:
            aliens.remove(alien)


def create_multi_aliens(aliens, screen, ai_settings):
    image_rect = pygame.image.load('images/alien.bmp').get_rect()
    max_raw_alien_count = int((ai_settings.width - image_rect.width * 2) / (2 * image_rect.width))
    max_col_alien_count = int((ai_settings.height - image_rect.height * 4) / (2 * image_rect.height))
    for x in range(max_raw_alien_count):
        for y in range(max_col_alien_count):
            alien = Alien(screen, ai_settings)
            alien.set_position(image_rect.width + 2 * x * image_rect.width,
                               image_rect.height + 2 * y * image_rect.height)
            aliens.add(alien)


def update_screen(screen, settings, ship, bullets, aliens):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    for alien in aliens.sprites():
        alien.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
