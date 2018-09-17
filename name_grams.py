from anagram import AnagramSolver
from parser import Parser

name_file = "simple_names.txt"
dictionary = "pbfs.txt"


p = Parser()

names_inventory = p.inventory(name_file)
dict_names = p.inventory_dict(dictionary)

solver = AnagramSolver(dict_names)

solutions = solver.solve(names_inventory, 2)

for s in solutions:
	print(s)

