class Ninja(pygame.sprite.Sprite):

	def __init__(self, imagename, xwindow, ywindow, characterxpos, characterypos):#self, image using for sprite, xstartlocation and y start location
		pygame.sprite.Sprite.__init__(self)  #pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.image.load("{}\{}".format(imagelocation, imagename))
				#self.image = self.image.convert_alpha()
		self.rect = self.image.get_rect()
				#self.rect.topleft = [xposition, yposition]
		self.xrange = xwindow
		self.yrange = ywindow
		self.x = characterxpos
		self.y = characterypos
		self.pos = [self.x, self.y]
		
	def move_up(self):
		if self.y > 31:
			self.y -= 32
			
	def move_down(self):
		if self.y < (self.yrange - 32):
			self.y += 32
			
	def move_left(self):
		if self.x > 31:
			self.x -= 32

	def move_right(self):
		if posx < self.xrange - 32:
			posx += 32

	def update(self):
		window.blit(self.image, self.pos)