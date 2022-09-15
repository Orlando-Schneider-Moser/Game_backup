class GUN:
	bullets = []
	def __init__(self, amo):
		self.ammo = amo

	class bullet:
		def __init__(self, x, y, w, h):
			self.x = x
			self.y = y
			self.w = w
			self.h = h
			self.image = 0
			self.position = 0

		def checkhit(self, en):
			for E in en:
				if E.x == self.x and E.y == self.y:
					E.hit(5)
				else:
					self.y + self.y + 16
	
	def shoot(self, player, enemies):

		if Player["direction"] == "up":
			GUN.bullets.append(bullet(player["x"]))

			
			