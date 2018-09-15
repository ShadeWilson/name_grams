class LetterInventory:

	def __init__(self, data):
		self.inventory = {}
		self.size = 0
		
		for letter in list(data.lower()):
			if letter in self.inventory:
				self.inventory[letter] += 1
			else:
				self.inventory[letter] = 1
			self.size += 1

		print("Inventory created: {}".format(self.__str__()))

	def __str__(self):
		str = ""
		for k, v in self.inventory.items():
			str += k * v

		return str + ", size {}".format(self.size)


	def add(self, other):
		for letter, v in other.inventory.items():
			if letter in self.inventory:
				self.inventory[letter] += v
			else:
				self.inventory[letter] = v
			self.size += 1


	def subtract(self, other):
		for letter, v in other.inventory.items():
			if letter in self.inventory:
				self.inventory[letter] -= v
				if self.inventory[letter] < 0:
					self.inventory[letter] = 0
				self.size -= 1

