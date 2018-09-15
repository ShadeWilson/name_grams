class LetterInventory:

	def __init__(self, data):
		self.inventory = {}
		self.size = 0
		
		for letter in list(data.lower()):
			if letter in self.inventory:
				self.inventory[letter] += 1
			else:
				self.inventory[letter] = 1
		print("Inventory created: {}".format(self.__str__()))

	def __str__(self):
		str = ""
		for k, v in self.inventory.items():
			str += k * v
		return str


	#def add()

