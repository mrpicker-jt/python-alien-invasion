import pygame

class Ship():
	"""这是飞船类"""
	def __init__(self, screen):
		"""初始化飞船并设置其初始位置"""

		#将飞船与视图绑定
		self.screen=screen

		# 加载飞船图像并获取其外接矩形
		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=self.screen.get_rect()

		#确定飞船位置在底部居中
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom

		self.movingRight=False
		self.movingLeft=False

	def updateSelf(self):
		if self.movingRight:
			self.rect.centerx += 1
		if self.movingLeft:
			self.rect.centerx -= 1

	def blitme(self):
		#在指定的位置绘制飞船
		self.screen.blit(self.image,self.rect)

