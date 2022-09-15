class GUN:
	def __init__(self, amo):
		self.ammo = amo

	def pew(self):
		if self.ammo > 0:
			self.ammo = self.ammo - 1
			print("pew pew")