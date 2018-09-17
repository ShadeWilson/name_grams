import re
from inventory import LetterInventory

class Parser:
	def parse(self, file):
		s = open(file, "r").read()
		s = re.sub('[^a-zA-Z0-9]', ' ', s)
		return s.split()


	def inventory_dict(self, file):
		"""
		Expects a file of words, one to a line,
		and creates a dictionary: word -> LetterInventory
		"""
		inventory = {}
		l = self.parse(file)
		for word in l:
			inventory[word] = LetterInventory(word)

		return inventory


	def inventory(self, file):
		"""
		Expects a file of words, one to a line,
		and creates a LetterInventory that is the combination of
		all words in the file
		"""
		inventory = LetterInventory("")
		l = self.parse(file)
		for word in l:
			inventory.add(LetterInventory(word))

		return inventory

