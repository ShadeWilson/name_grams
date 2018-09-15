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
			self.size += v


	def subtract(self, other):
		for letter, v in other.inventory.items():
			if letter in self.inventory:
				self.inventory[letter] -= v
				self.size -= v
				new_count = self.inventory[letter]
				if new_count < 0:
					self.inventory[letter] = 0
					self.size -= new_count


	def is_empty(self):
		return self.size == 0
				

