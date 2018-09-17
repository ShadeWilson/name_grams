import re

class LetterInventory:

	def __init__(self, data):
		self.inventory = {}
		self.size = 0
		
		# sanitize string: alphabetic only
		data = re.sub(r'[^a-zA-Z]', "", data).lower()

		for letter in list(data):
			if letter in self.inventory:
				self.inventory[letter] += 1
			else:
				self.inventory[letter] = 1
			self.size += 1

		#print("Inventory created: {}".format(self.__str__()))

	def __str__(self):
		str = ""
		for k, v in self.inventory.items():
			str += k * v

		return str


	def add(self, other):
		new = self.copy()
		for letter, v in other.inventory.items():
			if letter in new.inventory:
				new.inventory[letter] += v
			else:
				new.inventory[letter] = v
			new.size += v
		return new


	def subtract(self, other):
		new = self.copy()
		for letter, v in other.inventory.items():
			if letter in new.inventory and new.inventory[letter] >= v:
				new.inventory[letter] -= v
				new.size -= v
			else:
				return None
		return new


	def is_empty(self):
		return self.size == 0
				

	def copy(self):
		new = LetterInventory("")
		new.inventory = self.inventory.copy()
		new.size = self.size
		return new
