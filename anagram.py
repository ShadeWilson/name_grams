from inventory import LetterInventory

class AnagramSolver:

	def __init__(self, words):
		"""
		Expects words to be a dictionary of words
		-> letter inventories. Combines all letter
		inventories together to initialize a letter box
		"""
		self.dictionary = words
		self.solution = [] # list of anagram solutions, maybe shouldnt be an attribute



	def solve(self, inventory, num_words):
		self.solution = [] # clear last solution
		solve_helper(self, inventory, num_words, [])


	def solve_helper(self, inventory, num_words, words):
		"""
		Pass in a letter inventory and a number of
		words to solve for. Returns a list of lists, 
		where each list contains an anagram solution
		to the given letter inventory based on the 
		AnagramSolver's word dictionary
		"""
		# base case 1: we're out of letters
		if inventory.is_empty:
			self.solution.append(words)
		elif num_words == 0: # base case 2: reached the word limit before running out of letters
			return 
		else: # recursive case: backtrack through all words in dictionary
			for w in self.dictionary:
				choose = inventory.subtract(self.dictionary[w])
				if choose != None: # if we can subtract word from inventory
					words.append(w)
					solve_helper(self, choose, num_words - 1, words)
					words.remove(w)


