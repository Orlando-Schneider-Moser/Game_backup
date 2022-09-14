import pygame, sys
from pygame.locals import QUIT
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

#just some vars for the gameover screen
inGame = True 
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
}
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
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22],
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

					
		
#==============================================d

#enemies
class enemy:
	enemies = []

	for i in range(2):
		enemies.append(pygame.Rect(32*(i+1), 104, 16, 16))

				
#==============================================

#called every frame.
#draws the shapes on screen
def draw():
	
	#if not dead
	if inGame:
		#erase everything by drawing bg
		DISPLAYSURF.fill((70, 130, 10))
		
		#draw player at its location with a width and height and a color(see Player dict)
		pygame.draw.rect(DISPLAYSURF, Player["color"], pygame.Rect(Player["x"] ,Player["y"], Player["w"], Player["h"]))
		
		#draw background of the status bar (hp and maybe more like mana and items later)
		pygame.draw.rect(DISPLAYSURF, (100, 100, 100), pygame.Rect(0, 0, 640, 40))
		
		#draw the dark outline(a dark square) for the hp bar
		pygame.draw.rect(DISPLAYSURF, (50, 50, 50), pygame.Rect(376, 0, 384, 40))
		
		#draw the hp bar so that it goes down to the left(explanations for more)
		pygame.draw.rect(DISPLAYSURF, (255, 1, 1), pygame.Rect(640-x.x4(Player["health"])-4, 4, x.x4(Player["health"]), 14))

		#draw all enemies
		for E in enemy.enemies:
			pygame.draw.rect(DISPLAYSURF, (50, 225, 70), E)

		#draw every wall
		for wall in walllist:
			pygame.draw.rect(DISPLAYSURF, (30, 30, 30), wall)
	
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
		for b in enemy.enemies:

			#if its on the x or y axis
			if xory == "x":
				#if the next step would be the same position as a block on x axis
				if b.x == Player["x"] + 16*a:
					#if its on the same y axis
					if b.y == Player["y"]:
						#you did hit something :( not good 
						Player["health"] = Player["health"] - 4
						hit = False

			#same thing as above but for y axis
			elif xory == "y":
				if b.y == Player["y"] - 16*a:
					if b.x == Player["x"]:
						Player["health"] = Player["health"] - 4
						hit = False
		
		return hit
		
		
	
	def right():
		
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
			
#game loop
while True:
	
	#framrate
	Time.tick(60)
	
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
		
		#if you press the little cross at the top
		if event.type == QUIT:
			
			pygame.quit()
			sys.exit()		
	
	#check for gameover
	if Player["health"] <= 0:
	
		GameOver = True
		inGame = False

	#draw stuff onto the screen and update
	draw()
	pygame.display.update()