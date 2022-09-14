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
	"x":32,
	"y":32,
	"w":16,
	"h":16,
	"color":(240, 200, 125),
	"health":64,
	"maxhp":64,
}
#===============================

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
		pygame.draw.rect(DISPLAYSURF, (100, 100, 100), pygame.Rect(0, 0, 640, 32))
		
		#draw the dark outline(a dark square) for the hp bar
		pygame.draw.rect(DISPLAYSURF, (50, 50, 50), pygame.Rect(640-x.x4(Player["maxhp"])-8, 0, 640-x.x4(Player["maxhp"]), 32))
		
		#draw the hp bar so that it goes down to the left(explanations for more)
		pygame.draw.rect(DISPLAYSURF, (255, 1, 1), pygame.Rect(640-x.x4(Player["health"])-4, 4, x.x4(Player["health"]), 24))
	
	#if dead
	elif GameOver:
		
		#make black screen and say gameover
		DISPLAYSURF.fill((50, 50, 50))
		DISPLAYSURF.blit(Gameovr_fnt.render("GAME OVER",False, (225, 0, 0)), Gameovr_rect)
#==============================================

#playermovement
class playermovement:
	
	def right():
		
		#if not going off screen the walk
		if Player["x"] + 16 < 632:
			Player["x"] = Player["x"] + 16
			
	def left():
		
		if Player["x"] - 16 >= 0:
			Player["x"] = Player["x"] - 16
			
	def up():
		
		if Player["y"] - 16 >= 32:
			Player["y"] = Player["y"] - 16
			
	def down():
		
		if Player["y"] + 16 < 360:
			Player["y"] = Player["y"] + 16
#==========================================
			
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