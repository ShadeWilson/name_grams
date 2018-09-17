from inventory import LetterInventory

class AnagramSolver:

	def __init__(self, words):
		"""
		Expects words to be a dictionary of words
		-> letter inventories. Combines all letter
		inventories together to initialize a letter box
		"""
		self.dictionary = words
		self.solution = [] # set of anagram solutions, maybe shouldnt be an attribute


	def screen_dict(self, dictionary, inventory):
		"""
		Screen all words in dictionary, removing those that
		don't match the inventory at all. Returns a 
		screened dictionary
		"""
		copy = dictionary.copy()
		for word, inv in copy.copy().items(): # better way to do this?
			if inventory.subtract(inv) == None:
				del copy[word]
		return copy


	def solve(self, inventory, max_words):
		screened = self.screen_dict(self.dictionary, inventory)
		self.solution = [] # clear last solution
		self.solve_helper(screened, inventory, max_words, [])
		return self.solution


	def solve_helper(self, dictionary, inventory, max_words, words):
		"""
		Pass in a letter inventory and a number of
		words to solve for. Returns a list of lists, 
		where each list contains an anagram solution
		to the given letter inventory based on the 
		AnagramSolver's word dictionary
		"""
		# base case 1: we're out of letters
		if inventory.is_empty():
			word_set = set(words)
			if not word_set in self.solution: # check so different permutations of words are dropped
				print(words)
				self.solution.append(word_set)
		elif max_words == 0: # base case 2: reached the word limit before running out of letters
			return 
		else: # recursive case: backtrack through all words in dictionary
			screened = self.screen_dict(dictionary, inventory)
			for w, inv in screened.items():
				choose = inventory.subtract(inv)
				if choose != None: # if we can subtract word from inventory
					words.append(w)
					print(words)
					self.solve_helper(screened, choose, max_words - 1, words)
					words.pop()


