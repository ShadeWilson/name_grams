import re
from inventory import LetterInventory

class Parser:
	def parse(self, file):
		s = open(file, "r").read()
		s = re.sub('[^a-zA-Z0-9]', ' ', s)
		return s.split()


	def inventory(self, file):
		inventory = {}
		l = self.parse(file)
		for word in l:
			inventory[word] = LetterInventory(word)

		return inventory

