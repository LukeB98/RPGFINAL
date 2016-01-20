import pygame, sys, pytmx, os, random
from pytmx import load_pygame

pygame.init() #initilizing the pygame window

colors = {#My color dictionary
	"WHITE": [255, 255, 255],
	"BLACK": [0, 0, 0],
	"BLUE": [24, 74, 142],
	"RED": [155, 30, 35],
	"GREEN": [65, 167, 72]
}

xwindow = (800)#window x and y dimensions.   Don't have to define them separately
ywindow = (640)
window = pygame.display.set_mode((xwindow, ywindow))#Setting the window with the x and y dimensions
pygame.display.set_caption("Ninja RPG")#naming the window

active = True #keeping the while loop going until not active
clock = pygame.time.Clock()#in order to set fps with clock.tick(fps)

#ninja image that I made
imagelocation = (str(os.getcwd()) + "\Pictures")
musiclocation = (str(os.getcwd()) +  "\Music")
ninjaImg = pygame.image.load(str(imagelocation) + "\\ninja32px.png").convert()#importing a local image
ninx = xwindow/2#where the image will be placed
niny = ywindow/2

#Fonts + text + text size
myfont = pygame.font.Font('freesansbold.ttf', 32)#using fonts and text
fontsurface = myfont.render("Hello world!", True, colors["GREEN"])#(Text to write, ?,Text color, surface.)
fontrect = fontsurface.get_rect()#Get rectangle to place font surface on?
fontrect.center = (ninx, 50)#don't know.  Just include this

#music
pygame.mixer.music.load(musiclocation +"\Festival.mp3")
pygame.mixer.music.play(-1, 0.0)#Plays infinite times starting at 0.0

#object.play(), and object.stop() to start and stop sounds

#tmxdata = load_pygame("tiledstuff1.tmx")
#image = tmxdata.get_tile_image(0, 0, 0)
#tmxdata = pytmx.TiledMap("tiledstuff1.tmx")
def place_tiles(filename, xwindow, ywindow):#add x and y offset here too.
	#when placex equals screen size restart placex and add 32 to placey
	tmxdata = load_pygame("{}\{}".format(imagelocation, filename))
	tilex = 0#the tile being placed
	tiley = 0
	placex = 0#the location where the tile is being placed
	placey = 0
	tiles = True
	while tiles:#while there are still tiles
		image = (tmxdata.get_tile_image(tilex, tiley, 0)).convert_alpha()
		window.blit(image, [placex, placey])
		if placey == (ywindow-32) and placex == (xwindow-32):
			tiles = False
		elif placex == (xwindow-32):
			placey += 32
			tilex = 0
			tiley += 1
			placex = 0
		else:
			tilex += 1
			placex += 32
	return()

#
#ENEMY CLASS
#ENEMY CLASS
#

class Enemy(pygame.sprite.Sprite):

	def __init__(self, imagename, xwindow, ywindow, enemyxpos, enemyypos):#self, image using for sprite, xstartlocation and y start location
		pygame.sprite.Sprite.__init__(self)  #pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("{}\{}".format(imagelocation, imagename))
		self.rect = self.image.get_rect()
		self.xrange = xwindow
		self.yrange = ywindow
		self.x = enemyxpos 
		self.y = enemyypos
		self.move_dir = "none"
		self.times = 0
	
	def AI(self, charx, chary):
		if self.x < (charx - 32): #Enemy is to the left, needs to move right
			self.move_dir = "right"
			return("right")
		elif self.x > (charx + 32):
			self.move_dir = "left"
			return("left")
		elif self.y < (chary - 32):
			self.move_dir = "down"
			return("down")
		elif self.y > (chary + 32):
			self.move_dir = "up"
			return("up")
		else:
			return("none")
			
	def move_up(self):
		if self.y > 31:
			#self.move_dir = "up"
			self.times = 4
			
	def move_down(self):
		if self.y < (self.yrange - 32):
			#self.move_dir = "down"
			self.times = 4

	def move_left(self):
		if self.x > 31:
			#self.move_dir = "left"
			self.times = 4

	def move_right(self):
		if self.x < self.xrange - 32:
			#self.move_dir = "right"
			self.times = 4
			
	def update(self):
		#cycle = 0
		window.blit(self.image, [self.x, self.y])
		while self.times > 0:
			window.blit(self.image, [self.x, self.y])
			self.times -= 1
			
			if self.move_dir == "up":
				self.y -= 8
				
			elif self.move_dir == "down":
				self.y += 8
			
			elif self.move_dir == "left":
				self.x -= 8
			
			elif self.move_dir == "right":
				self.x += 8
			
			else:
				window.blit(self.image, [self.x, self.y])
#
#ENEMY CLASS
#ENEMY CLASS
#

class Ninja(pygame.sprite.Sprite):

	def __init__(self, imagename, xwindow, ywindow, characterxpos, characterypos):#self, image using for sprite, xstartlocation and y start location
		pygame.sprite.Sprite.__init__(self)  #pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("{}\{}".format(imagelocation, imagename))
		self.rect = self.image.get_rect()
		self.xrange = xwindow
		self.yrange = ywindow
		self.x = characterxpos
		self.y = characterypos
		self.move_dir = "none"
		self.times = 0
		
	def move_up(self):
		if self.y > 31:
			self.move_dir = "up"
			self.times = 4
			
	def move_down(self):
		if self.y < (self.yrange - 32):
			self.move_dir = "down"
			self.times = 4

	def move_left(self):
		if self.x > 31:
			self.move_dir = "left"
			self.times = 4

	def move_right(self):
		if self.x < self.xrange - 32:
			self.move_dir = "right"
			self.times = 4
			
	def update(self):
		cycle = 0
		window.blit(self.image, [self.x, self.y])
		while self.times > 0:
			window.blit(self.image, [self.x, self.y])
			self.times -= 1
			
			if self.move_dir == "up":
				self.y -= 8
				
			elif self.move_dir == "down":
				self.y += 8
			
			elif self.move_dir == "left":
				self.x -= 8
			
			elif self.move_dir == "right":
				self.x += 8
			
			else:
				window.blit(self.image, [self.x, self.y])
		return [self.x, self.y]

		
xloc = 0
yloc = 0
enemyxloc = 64*4
enemyyloc = 64*4
MAP = "tiledstuff1.tmx"
place_tiles("tiledstuff1.tmx", xwindow, ywindow)
ninja = Ninja("ninja32px.png", xwindow, ywindow, xloc, yloc)#(self, filename, xloc, yloc)
enemy1 = Enemy("redenemy.png", xwindow, ywindow, enemyxloc, enemyyloc)
while active:
	chance_move = 9
#filename, xwindow, ywindow, xposition, yposition, replace_tiles
	for event in pygame.event.get():
		action = pygame.key.get_pressed()
		if event.type == pygame.QUIT:
			pygame.quit()
		#pygame.time.delay(120)
		if action[pygame.K_w]:
			ninja.move_up()
			chance_move = random.randint(0, 9)
		elif action[pygame.K_s]:
			ninja.move_down()
			chance_move = random.randint(0, 9)
		elif action[pygame.K_a]:
			ninja.move_left()
			chance_move = random.randint(0, 9)
		elif action[pygame.K_d]:
			ninja.move_right()			
			chance_move = random.randint(0, 9)
	#window.blit(ninja.image, ninja.rect)
			#pygame.mixer.music.stop()	
	place_tiles("tiledstuff1.tmx", xwindow, ywindow)#Placing background with pytmx + tiled
	#window.blit(fontsurface, fontrect)
	updatelocations = ninja.update()
	xloc = int(updatelocations[0])
	yloc = int(updatelocations[1])
	if chance_move < 5:
		enemy_move_dir = enemy1.AI(xloc, yloc)
		if enemy_move_dir == "up":
			enemy1.move_up()
		elif enemy_move_dir == "down":
			enemy1.move_down()
		elif enemy_move_dir == "left":
			enemy1.move_left()
		elif enemy_move_dir == "right":
			enemy1.move_left()
	enemy1.update()
	pygame.display.update()
	clock.tick(40)	#FPS
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
