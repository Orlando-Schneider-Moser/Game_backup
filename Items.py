
class bullet:
		def __init__(self, x, y, w, h, dir1, dir2, dmg):
			self.x = x
			self.y = y
			self.w = w
			self.h = h
			self.direction = dir1
			self.direction2 = dir2
			self.dmg = dmg

		def checkhit(self, en):
			for E in en:
				if self.direction == "y":
					if E.x == self.x -6 and E.y == self.y:
						E.hit(self.dmg)
						GUN.bullets.remove(self)
					else:
						self.y = self.y + 16 * self.direction2
				elif self.direction == "x":
					if E.x == self.x and E.y == self.y -6:
						E.hit(self.dmg)
						GUN.bullets.remove(self)
					else:
						self.x = self.x + 16 * self.direction2
				if self.x < 0:
					GUN.bullets.remove(self)
				if self.x > 640:
					GUN.bullets.remove(self)
				if self.y > 360:
					GUN.bullets.remove(self)
				if self.y < 40:
					GUN.bullets.remove(self)
					
			

class GUN:
	bullets = []
	def __init__(self, inmag, magsize):
		self.inmag = inmag
		self.magsize = magsize

	def reload(self, x):
		self.inmag = x
		
	def shoot(self, player, enemies):
		
		if self.inmag > 0:
			if player["direction"] == "up":
				GUN.bullets.append(bullet(player["x"]+6, player["y"], 4, 16, "y", -1, 5))
				self.inmag = self.inmag - 1
			if player["direction"] == "down":
				self.inmag = self.inmag - 1
				GUN.bullets.append(bullet(player["x"]+6, player["y"], 4, 16, "y", 1, 5))
			if player["direction"] == "left":
				self.inmag = self.inmag - 1
				GUN.bullets.append(bullet(player["x"], player["y"] + 6, 16, 4, "x", -1, 5))
			if player["direction"] == "right":
				self.inmag = self.inmag - 1
				GUN.bullets.append(bullet(player["x"], player["y"] + 6, 16, 4, "x", 1, 5))
				
