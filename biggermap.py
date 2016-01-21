import pygame, pytmx, random
pygame.init()



xwindow = (800)#window x and y dimensions.   Don't have to define them separately
ywindow = (640)
window = pygame.display.set_mode((xwindow, ywindow))#Setting the window with the x and y dimensions
pygame.display.set_caption("Ninja RPG")#naming the window


active = True #keeping the while loop going until not active
clock = pygame.time.Clock()#in order to set fps with clock.tick(fps)
imagelocation = (str(os.getcwd()) + "\Pictures")
musiclocation = (str(os.getcwd()) +  "\Music")
pygame.display.set_icon('ninjafront.png')
'''
pygame.mixer.music.load(musiclocation +"\Crusade.mp3")
pygame.mixer.music.play(-1, 0.0)#Plays infinite times starting at 0.0
'''
class map():
	
	def __init__(self, imagelocation, filename, winsizex, winsizey, playerlocx, playerlocationy, tilexstart, tileystart):
		self.tmxdata = load_pygame("{}\{}".format(imagelocation, filename))
		self.xdisplay,self.ydisplay = (winsizex,winsizey)
		self.xtilelimit,self.ytilelimit = (winsizex/32,winsizey/32)
		self.xtileplace, self.ytileplace = (tilexstart,tileystart)
		self.placex, self.placey = (0,0)
		#build_rects(tmxmap, layer, tileset=None, real_gid=None)
		#getTileProperties(x,y,l)
	def place_tiles(self):
		tiles = True
		while tules:
			image = self.tmxdata.get_tile_image(self.)
			window.blit(image,[self.placex, self.placey])
			if self.placey == (self.ydisplay-32) and self.placex == (self.xdisplay-32):
				tiles = False
			elif self.placex == (self.xdisplay-32):
				self.placey += 32
				self.tilex = 0
				self.tiley += 1
				self.placex = 0
			else:
				self.tilex += 1
				self.placex += 32
	def tilecollision(self, playerxpos, playerypos, spritemovedir):
		playerxpos = playerxpos/32
		playerypos = playerypos/32
		surface_layer = 2
		if spritemovedir == "up":
			tile = [playerxpos, playerypos - 1]
		elif spritemovedir == "down":
			tile = [playerxpos, playerypos + 1]
		elif spritemovedir == "left":
			tile = [playerxpos - 1, playerypos]
		elif spritemovedir == "right":
			tile = [playerxpos + 1, playerypos]
		else:
			return("none")
		tile_to_check = getTileProperties(tile[0], tile[1], surface_layer)
#
#
#
#
			
def place_tiles(filename, xwindow, ywindow):#add x and y offset here too.
	#when placex equals screen size restart placex and add 32 to placey
	tmxdata = load_pygame("{}\{}".format(imagelocation, filename))
	tilex,tiley = 0,0#the tile being placed
	placex,placey = 0,0#the location where the tile is being placed
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





