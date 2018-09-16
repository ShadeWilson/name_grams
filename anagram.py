from inventory import LetterInventory

class AnagramSolver:

	def __init__(self, words):
		"""
		Expects words to be a dictionary of words
		-> letter inventories. Combines all letter
		inventories together to initialize a letter box
		"""
		self.words = words


	def solve(self, inventory, num_words):
		"""
		Pass in a letter inventory and a number of
		words to solve for. Returns a list of lists, 
		where each list contains an anagram solution
		to the given letter inventory based on the 
		AnagramSolver's word dictionary
		"""
		for w in self.words:
			

