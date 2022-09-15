import pygame, sys, random, math
from pygame.locals import QUIT
import Items
#please dont read this


#how to make a dictionary
#a = {"b":"beans"}
#print(a["b"])
#> beans


#this is a grid based pixel art game so we do everything in steps of 16 (x8 and x32 for convinience.)
class x:
	def x16(a):
		return a*16
	def x8(a):
		return a*8
	def x32(a):
		return a*32
	def x4(a):
		return a*4
#==============================

#initiate text and game
pygame.init()
pygame.font.init()

#just some vars for the diffrent screens
inGame = True
inStart = False
inMenu = False
inInventory = False
GameOver= False

#display
DISPLAYSURF = pygame.display.set_mode((640, 360))
pygame.display.set_caption('wraaa world')

#we need time.Clock() to make a fixed framerate
Time= pygame.time.Clock()

#need to give fonts a name (put them in var and give them a style(the font) and a size.)
#Then a rectangle for the font to be displayed on.
Gameovr_fnt = pygame.font.SysFont("Garamond", 64)
Gameovr_rect = pygame.Rect(320-(Gameovr_fnt.size("GAME OVER")[0])/2,180-(Gameovr_fnt.size("GAME OVER")[1])/2,100, 100)

colors = {
	"zombie":(40, 240, 20),
	"Player":(240, 200, 125),
	"hpbar":(255, 1, 1),
	"hpbarbg":(50, 50, 50)
}
#================================


#Player var using a dictionary
Player = {
	"x":16,
	"y":56,
	"w":16,
	"h":16,
	"color":(240, 200, 125),
	"hp":100,
	"health":64,
	"maxhp":64,
	"direction":"Right"
}
#- - - - - - - - - - - - - - - - - 

gun = Items.GUN(36)

#===============================

#the number at the end is so that every row is unique (i had a problem with that and this solves it)
Map = [
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 11],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 30]
]

#empty array for the walls al rects
walllist = []

#we need walls to stop the player from just running for now its just gonna be a map thought hoping to make it random later
class walls:

	#needed to make the x position of the cell
	cellnum = 0

	#stores the walls in a list
	def makewalls():

		#every row (the y axis) in map
		for row in Map:

			#reset cellnum(x axis) to 0
			walls.cellnum = 0

			#every cell/wall in a row
			for cell in row:

				#1 == wall so if it is add a wall to the list
				if cell == 1:
					walllist.append(pygame.Rect(walls.cellnum * 16, Map.index(row)*16 + 40, 16, 16))
				#add one to cellnum so the next cell is one block away
				walls.cellnum += 1

					
		
#==============================================

#enemies

enemies = []

class enemy:
	## you can now make an enemy with:
	#enemy1 = enemy(xpos, ypox, w, h, (color in rgb), "type of enemy")
	## Then you can use that because in this case self == enemy 
	## so you can just say enemy1.x to change the x var
	# enemy1.x += 16
	## you have just changed its x axis
	def __init__ (self, x, y, width, heigth, color, type, hp):
		self.x = x
		self.y = y
		self.w = width
		self.h = heigth
		self.color = color
		self.type = type
		self.hp = hp
		self.maxhp = hp
		self.a = 4

	def checkdeath(self):
		if self.hp <= 0:
			enemies.append(enemy(16*random.randrange(1, 10), 16*random.randrange(1, 10) + 40, 16, 16, colors["zombie"], "zombie", 20))
			enemies.remove(self)

	def move(self):
		if Player["x"] > self.x:
			if Player["y"] <= self.y:
				# left, top/ bigger, smaller
				if Player["x"] - self.x > Player["y"] - self.y:
					print("above, to left/ right")
					self.x = self.x + 16
				else:
					print("above , to left/ down")
					self.y = self.y + 16
			
			else:
				#left, bottom/ bigger, bigger
				if Player["x"] - self.x < self.y - Player["y"]:
					print("above, to left/ right")
					self.x = self.x - 16
				else:
					print("above, to left/ down")
					self.y = self.y + 16
							
		else:
						
			if Player["y"] < self.y:
				#right, top/ smaller, smaller
				if self.x - Player["x"] > self.y - Player["y"]:
					print("under, to right / left")
					self.x = self.x - 16
				else:
					print("under, to right / up")
					self.y = self.y - 16
			
			else:
				#right, bottom/ smaller, bigger
				if self.x - Player["x"] >= Player["y"] - self.y:
					print("above, to right / left")
					self.x = self.x - 16
				else:
					print("above, to right / down")
					self.y = self.y + 16

	def touchplayer(self):
		if Player["x"] + 16 == self.x and Player["y"] == self.y:
			return True
		elif Player["x"] - 16 == self.x and Player["y"] == self.y:
			return True
		elif Player["x"] == self.x and Player["y"] + 16 == self.y:
			return True
		elif Player["x"] == self.x and Player["y"] - 16 == self.y:
			return True
		else:
			return False

	def touchwall(self):
		for Wall in walllist:
			if Wall.x + 16 == self.x and Wall.y == self.y:
				return "left"
			elif Wall.x - 16 == self.x and Wall.y == self.y:
				return "right"
			elif Wall.x == self.x and Wall.y + 16 == self.y:
				return "above"
			elif Wall.x == self.x and Wall.y - 16 == self.y:
				return "under"
			else:
				return False

	def moveawayfromwall(self):
		pass

	def hit(self, damage):
		self.hp = self.hp - damage
	
	def move2player(self, speed):
		if self.a == speed:
			self.a = 0
			if inInventory == True or inMenu == True:
				pass
			else:
				if self.touchplayer():
					pass
				elif self.touchwall():
					self.moveawayfromwall()					
				else:
					self.move()
		else:
			self.a = self.a + 1


enemies.append(enemy(32, 104, 16, 16, colors["zombie"], "zombie", 20))
	

		
#==============================================

#called every frame.
#draws the shapes on screen
def draw():
	
	#if not dead
	if inGame:
		#erase everything by drawing bg
		DISPLAYSURF.fill((70, 130, 10))
		
		#draw player at its location with a width and height and a color
		pygame.draw.rect(DISPLAYSURF, Player["color"], pygame.Rect(Player["x"] ,Player["y"], Player["w"], Player["h"]))
		
		#draw background of the status bar (hp and maybe more like mana and items later)
		pygame.draw.rect(DISPLAYSURF, (100, 100, 100), pygame.Rect(0, 0, 640, 40))
		
		#draw the dark outline(a dark square) for the hp bar
		pygame.draw.rect(DISPLAYSURF, (50, 50, 50), pygame.Rect(376, 0, 384, 40))
		
		#draw the hp bar so that it goes down to the left(explanations for more)
		pygame.draw.rect(DISPLAYSURF, (255, 1, 1), pygame.Rect(640-x.x4(Player["health"])-4, 4, x.x4(Player["health"]), 14))
		
		#draw every wall
		for wall in walllist:
			pygame.draw.rect(DISPLAYSURF, (30, 30, 30), wall)

		#draw all enemies and hp bars
		for E in enemies:
			pygame.draw.rect(DISPLAYSURF, E.color, pygame.Rect(E.x, E.y, E.w, E.h))
			pygame.draw.rect(DISPLAYSURF, colors["hpbarbg"], pygame.Rect(E.x - E.maxhp/2 + 7, E.y - 8, E.maxhp + 2, 6))
			pygame.draw.rect(DISPLAYSURF, colors["hpbar"], pygame.Rect(E.x - E.maxhp/2 + 8, E.y - 7, E.hp, 4))
	
	#if dead
	elif GameOver:
		
		#make black screen and say gameover
		DISPLAYSURF.fill((50, 50, 50))
		DISPLAYSURF.blit(Gameovr_fnt.render("GAME OVER",False, (225, 0, 0)), Gameovr_rect)
#==============================================
		
#playermovement
class playermovement:

	#check if there is a wall
	def checkwalls(xory, a):
		#output
		hit = True
		#check for every wall
		for b in walllist:

			#if its on the x or y axis
			if xory == "x":
				#if the next step would be the same position as a block on x axis
				if b.x == Player["x"] + 16*a:
					#if its on the same y axis
					if b.y == Player["y"]:
						#you did hit something :( not good 
						hit = False

			#same thing as above but for y axis
			elif xory == "y":
				if b.y == Player["y"] - 16*a:
					if b.x == Player["x"]:
						hit = False

		#checks if bumped into enemy
		for E in enemies:

			#if its on the x or y axis
			if xory == "x":
				#if the next step would be the same position as a block on x axis
				if E.x == Player["x"] + 16*a:
					#if its on the same y axis
					if E.y == Player["y"]:
						#you did hit something :( not good 
						Player["health"] = Player["health"] - 4
						hit = False

			#same thing as above but for y axis
			elif xory == "y":
				if E.y == Player["y"] - 16*a:
					if E.x == Player["x"]:
						Player["health"] = Player["health"] - 4
						hit = False
		
		return hit
		
		
	
	def right():
		
		for E in enemies:
			E.hp = E.hp-1
		#if not going off screen or hitting wall then walk
		if Player["x"] + 16 < 632:
			if playermovement.checkwalls("x", 1):
				Player["x"] = Player["x"] + 16
			
	def left():
		
		if Player["x"] - 16 >= 0:
			if playermovement.checkwalls("x", -1):
				Player["x"] = Player["x"] - 16
			
	def up():
		
		if Player["y"] - 16 >= 32:
			if playermovement.checkwalls("y", 1):
				Player["y"] = Player["y"] - 16
			
	def down():
		
		if Player["y"] + 16 < 360:
			if playermovement.checkwalls("y", -1):
				Player["y"] = Player["y"] + 16
#==========================================

walls.makewalls()
def doUpdate():
	#check for gameover
	if Player["health"] <= 0:
	
		GameOver = True
		inGame = False

	

	for E in enemies:
		E.checkdeath()
		E.move2player(16)

	for bullet in Items.GUN.bullets:
		bullet.checkhit(enemies)
	
			
#game loop
while True:
	
	#framrate
	Time.tick(30)
	
	#for every possible event in pygame check the following
	for event in pygame.event.get():

		#is the event == a key press
		if event.type == pygame.KEYDOWN:
			
			#what key is it
			#checks for mevement with the arrow keys
			if event.key == pygame.K_RIGHT:
				playermovement.right()
			if event.key == pygame.K_LEFT:
				playermovement.left()
			if event.key == pygame.K_UP:
				playermovement.up()
			if event.key == pygame.K_DOWN:
				playermovement.down()
			if event.key == pygame.K_w:
				Player["direction"] = "up"
			if event.key == pygame.K_a:
				Player["direction"] = "left"
			if event.key == pygame.K_s:
				Player["direction"] = "down"
			if event.key == pygame.K_d:
				Player["direction"] = "right"
			if event.key == pygame.K_e:
				Gun.shoot(Player, enemies)
				
		
		#if you press the little cross at the top
		if event.type == QUIT:
			
			pygame.quit()
			sys.exit()		
	
	
	#draw stuff onto the screen and update
	draw()
	pygame.display.update()