import pygame, sys, pytmx, os, random, math, pdb
from pytmx import load_pygame
#in this version I'm shooting to make movement more realistic + accurate.
#Next will be player mechanics
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
ninjaImg = pygame.image.load(str(imagelocation) + "\\ninja32px.png")#importing a local image
ninx = xwindow/2#where the image will be placed
niny = ywindow/2

#Fonts + text + text size
myfont = pygame.font.Font('freesansbold.ttf', 32)#using fonts and text
fontsurface = myfont.render("Hello world!", True, colors["GREEN"])#(Text to write, ?,Text color, surface.)
fontrect = fontsurface.get_rect()#Get rectangle to place font surface on?
fontrect.center = (ninx, 50)#don't know.  Just include this

#music
pygame.mixer.music.load(musiclocation +"\Crusade.mp3")
#pygame.mixer.music.play(-1, 0.0)#Plays infinite times starting at 0.0

#object.play(), and object.stop() to start and stop sounds

#tmxdata = load_pygame("tiledstuff1.tmx")
#image = tmxdata.get_tile_image(0, 0, 0)
#tmxdata = pytmx.TiledMap("tiledstuff1.tmx")


#set_viewbox(self, top, bottom, left, right):
def set_cursor():
	cursor_strings = (#Really bad ninja star.
	"           XX           ",
	"          X..X          ",
	"         X.X..X         ",
	"         X.XX.X         ",
	"         X.XX.X         ",
	"        X.X..X.X        ",
	"        X.X..X.X        ",
	"        X.X..X.X        ",
	"     XXX.X....X.XXX     ",
	"   XX...XX....XX...XX   ",
	"  X..XXX..X..X..XXX..X  ",
	" X.XX......XX......XX.X ",
	" X..X......XX......X..X ",
	"  X..XXX..X..X..XXX..X  ",
	"   XX...XX....XX...XX   ",
	"     XXX.X....X.XXX     ",
	"        X.X..X.X        ",
	"        X.X..X.X        ",
	"        X.X..X.X        ",
	"         X.XX.X         ",
	"         X.XX.X         ",
	"         X.X..X         ",
	"          X..X          ",
	"           XX           ")
	cursor_ninja_star =(
 	"           X            ",
	"           XX           ",
	"           XX           ",
	"           XX           ",
	"          XXXX          ",
	"          XXXX          ",
	"          XXXX          ",
	"         XXXXXX         ",
	"         XXXXXX         ",
	"       XXXXXXXXXX       ",
	"    XXXXXXXXXXXXXXXX    ",
	"XXXXXXXXXXXXXXXXXXXXXXXX",
	" XXXXXXXXXXXXXXXXXXXXXX ",
	"    XXXXXXXXXXXXXXXX    ",
	"       XXXXXXXXXX       ",
	"         XXXXXX         ",
	"         XXXXXX         ",
	"          XXXX          ",
	"          XXXX          ",
	"          XXXX          ",
	"           XX           ",
	"           XX           ",
	"           XX           ",
 	"           X            ")
	
	ninja_star, mask = pygame.cursors.compile(cursor_ninja_star, black="X", white=".", xor="o")
	pygame.mouse.set_cursor((24,24), (0,0), ninja_star, mask)

class Menu_sprites(pygame.sprite.Sprite):
	def __init__(self, pic_path, pic_name):
		super(Enemy, self).__init__()
		pygame.sprite.Sprite.__init__(self)
		self.image = (os.getcwd + "/" + pic_path + "/" + pic_name)
		self.rect = self.image.get_rect()
		self.center_x = self.rect.center.x
		self.center_y = self.rect.center.y
	
	def animation(self, (startpos), (endpos), animation_time):
		#startpos and endpos are the starting and ending x and y positions
		#animation_time is how long you want the animation to take to occu in milliseconds
		self.start_x,self.start_y = startpos
		self.end_x, self.end_y = endpos
		if self.start_x != self.end_x:#if start_x is to the left, move it right
			self.x_diff = self.end_x - self.start_x

		if self.start_y != self.end_y:#if start_y is above, move it down
			self.y_diff = self.end_y - self.start_y

		self.clock_y = pygame.time.Clock()
		self.clock_x = pygame.time.Clock()
		
		if self.x_diff > 0:
			self.clock_x.set_timer((self.x_diff)/animation_time)
			
		elif self.x_diff < 0:
			self.clock_x.set_timer((self.x_diff -= (-self.x_diff)/animation_time), animation_time)
		else:
			self.clock_x.set_timer(None)
		while True:
			if self.x_diff > 0:
				self.clock.set_timer((self.x_diff)/animation_time)
				
		self.clock.set_timer(animation_time)

		

class Menu():
	
	def __init__(self, imagelocation):
	
		self.image_location = imagelocation
		self.menu_background = pygame.Surface((800,640))
		self.menu_background_pic = pygame.image.load("{}\{}".format(self.image_location, "mselect.png"))
		self.menu_main_background = pygame.image.load("{}\{}".format(self.image_location, "mbackground_pic.png"))
		#self.menu_background.rect = self.menu_background.get_rect()
		
		self.font = pygame.font.SysFont("ariblk.ttf", 32)#self.font = pygame.font.Font("ariblk.ttf", 32)#pygame.font.match_font("font name") - to get the font
		self.font_surface = self.font.render("The Last Ninja", True, colors["BLACK"])
		self.font_rect = self.font_surface.get_rect()
		
		#self.fx = 100
		self.font_y = 640
		#self.font_rect.center = (xwindow/2,self.font_y)
		self.font_width = self.font_surface.get_width()

	def Main_menu(self):
		self.menu_x = 250
		self.menu_y = 640
		#self.font_rect.x = self.fx
		#self.font_rect.y = self.fy
	def update(self, object):
		if object == "Main_menu":#Display main menu animation.
			if self.menu_y != 50:
				self.menu_y -= 10
				self.font_y -= 10
				self.font_rect.center = ((xwindow/2)-(self.font_width/2),self.font_y + 35)
			#if self.menu_y !=50:W
				#if self.font_rect.center[0] >= (xwindow/2):#not actual center, just a rough guess...
					#window.blit(self.font_surface,(self.font_rect.x, self.font_rect.y))
					#self.font_rect.x -=10
				#self.font_rect.y -= 10#self.menu_y + (self.menu_y/2)
			
					
			window.blit(self.menu_main_background,(-200,0))
			window.blit(self.menu_background_pic, (self.menu_x,self.menu_y))
			window.blit(self.font_surface,(self.font_rect.center))
			self.mouse_x,self.mouse_y = pygame.mouse.get_pos()
			if self.mouse_x >= self.menu_x:# and self.mouse_x <= self.menu_x +   and self.mouse_y 
				self.font_surface = self.font.render("The Last Ninja", True, colors["WHITE"])
				#self.font_rect = self.font_surface.get_rect()
			else:
				self.font_surface = self.font.render("The Last Ninja", True, colors["BLACK"])
				#self.font_rect = self.font_surface.get_rect()
start_menu = Menu(imagelocation)
start_menu.Main_menu()
set_cursor()
def main_menu():
	while active:
		for event in pygame.event.get():
			action = pygame.key.get_pressed()
			if event.type == pygame.QUIT:
				pygame.quit()
			#pygame.time.delay(120)
			if event.type == pygame.KEYDOWN:#change_speed(self,hchange,vchange)
				#if event.key == pygame.K_p:
					
			#if event.type == pygame.KEYUP:
				event = None
		start_menu.update("Main_menu")
			

		pygame.display.update()
		clock.tick(30)	#FPS
main_menu()
	
	
'''
class Enemy(pygame.sprite.Sprite):

	def __init__(self, xwindow, ywindow):#self, image using for sprite, xstartlocation and y start location
		super(Enemy, self).__init__()
		pygame.sprite.Sprite.__init__(self)  #pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((32,32))
		self.image.fill(colors["WHITE"])
		self.set_properties()
		self.vspeed = 0
		self.hspeed = 0
		#self.set_position(characterxpos, characterypos)
	def set_properties(self):
		self.rect = self.image.get_rect()
		self.origin_x = self.rect.centerx
		self.origin_y = self.rect.centery
		
	def set_image(self, imagelocation, filename):
		self.image = pygame.image.load("{}\{}".format(imagelocation, filename))
		self.set_properties()
		
	def change_speed(self,hchange,vchange):
		self.hspeed += hchange
		self.vspeed += vchange

	def set_position(self,x,y):
		self.rect.x = x #- self.origin_x
		self.rect.y = y #- self.origin_y
		
	def update(self):
		
		self.rect.x += self.hspeed
		self.rect.y += self.vspeed
		window.blit(self.image, self.rect)'''
