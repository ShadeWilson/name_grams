from anagram import AnagramSolver
from parser import Parser

name_file = "simple_names.txt"
dictionary = "names.txt"

max_words = input("What is the max number of words allowed?  ")


p = Parser()

names_inventory = p.inventory(name_file)
dict_names = p.inventory_dict(dictionary)

solver = AnagramSolver(dict_names)

solutions = solver.solve(names_inventory, max_words)

print("Anagram solutions for {}:".format(", ".join(p.parse(name_file))))
for s in solutions:
	print(s)

