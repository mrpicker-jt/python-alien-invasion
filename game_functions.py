import pygame
import sys

def handle_events(ship):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					ship.movingRight=True
				if event.key == pygame.K_LEFT:
					ship.movingLeft=True
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					ship.movingRight=False
				if event.key == pygame.K_LEFT:
					ship.movingLeft=False

def update_screen(screen,settings,ship):
	screen.fill(settings.bg_color)
	ship.blitme()
	# 让最近绘制的屏幕可见
	pygame.display.flip()