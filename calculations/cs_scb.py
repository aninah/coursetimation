from concentration import Concentration
from pathway import Pathway
from pathway import pathways

def naive_argmax(arr):
	best = 0
	curr = arr[0]
	for i in range(len(arr)):
		if arr[i] > curr:
			curr = arr[i]
			best = i
	return best
class Computer_Science_SCB(Concentration):
	"""
	satisfied:
		given list of classes taken, 
		returns list of classes fulfilling the concentration
		** takes into account pathway requirements this time ** 
	"""	 
	def satisfied(self, classes_taken):
		classes = list(classes_taken)
		satisfied = Concentration.satisfied(self, classes_taken)
		
		# clear the upper levels T.T
		for i in range(8, 16):
			satisfied[i] = 0

		# figure out which pathways we're closest to completing
		percent = [path.percent_complete(classes) for path in pathways]
		ind = 8

		# add pathways.
		x = naive_argmax(percent)
		y = pathways[x].satisfied(classes)[-2:]
		satisfied[ind] = y[0]
		satisfied[ind + 1] = y[1]
		ind += 2
		if y[0] != 0: classes.remove(y[0])
		if y[1] != 0: classes.remove(y[1])

		percent = [path.percent_complete(classes) for path in pathways]
		percent[x] = -1
		x2 = naive_argmax(percent)
		y = pathways[x2].satisfied(classes)[-2:]
		satisfied[ind] = y[0]
		satisfied[ind + 1] = y[1]
		ind += 2

		# clear classes of satisfied reqs.
		for i in satisfied:
			if i != 0 and i in classes:
				classes.remove(i)

		non_core_related = list(set(pathways[x].get_non_core_related(thousand_level)).intersection(pathways[x2].get_non_core_related(thousand_level)))
		
		# get the rest!
		rest = [non_core_related, upper_level,thousand_level,thousand_level]
		for r in range(len(rest)):
			for c in rest[r]:
				if c in classes:
					satisfied[ind+r] = c
					classes.remove(c)
					break

		return satisfied

class Computer_Science_AB(Concentration):
	

	"""
	satisfied:
		given list of classes taken, 
		returns list of classes fulfilling the concentration
		** takes into account pathway requirements this time ** 
	"""	 
	def satisfied(self, classes_taken):
		classes = list(classes_taken)
		satisfied = Concentration.satisfied(self, classes_taken)
		
		# clear the upper levels T.T
		for i in range(6, 10):
			satisfied[i] = 0

		# figure out which pathways we're closest to completing
		percent = [path.percent_complete(classes) for path in pathways]
		ind = 6

		# add pathway
		x = naive_argmax(percent)
		y = pathways[x].satisfied(classes)[-2:]
		print(y)
		satisfied[ind] = y[0]
		satisfied[ind + 1] = y[1]
		ind += 2

		# clear classes of satisfied reqs.
		for i in satisfied:
			if i != 0:
				classes.remove(i)

		# get the rest!
		rest = [pathways[x].get_non_core_related(thousand_level), thousand_level]
		for r in range(len(rest)):
			for c in rest[r]:
				if c in classes:
					satisfied[ind+r] = c
					classes.remove(c)
					break

		return satisfied


# /*     ----- TESTING -----     */

all_classes = ['CSCI 0020', 'CSCI 0030', 'CSCI 0081', 'CSCI 0082', 'CSCI 0100', 'CSCI 0111', 'CSCI 0130', 'CSCI 0150', 'CSCI 0160', 'CSCI 0170', 'CSCI 0180', 'CSCI 0190', 'CSCI 0220', 'CSCI 0320', 'CSCI 0330', 'CSCI 0530', 'CSCI 1010', 'CSCI 1230', 'CSCI 1234', 'CSCI 1250', 'CSCI 1260', 'CSCI 1270', 'CSCI 1280', 'CSCI 1300', 'CSCI 1320', 'CSCI 1370', 'CSCI 1380', 'CSCI 1410', 'CSCI 1420', 'CSCI 1430', 'CSCI 1450', 'CSCI 1460', 'CSCI 1470', 'CSCI 1550', 'CSCI 1570', 'CSCI 1575', 'CSCI 1600', 'CSCI 1650', 'CSCI 1670', 'CSCI 1680', 'CSCI 1690', 'CSCI 1730', 'CSCI 1800', 'CSCI 1805', 'CSCI 1810', 'CSCI 1820', 'CSCI 1870', 'CSCI 1900', 'CSCI 1950N', 'CSCI 1950Y', 'CSCI 1951A', 'CSCI 1951C', 'CSCI 1951I', 'CSCI 1951K', 'CSCI 1951R', 'CSCI 1970', 'CSCI 1971', 'CSCI 1972', 'CSCI 2240', 'CSCI 2270', 'CSCI 2470', 'CSCI 2500B', 'CSCI 2890', 'CSCI 2950V', 'CSCI 2951F', 'CSCI 2951I', 'CSCI 2951K', 'CSCI 2951U', 'CSCI 2952F', 'CSCI 2952G', 'CSCI 2980', 'CSCI 2990']

prereqs = ["MATH 100", "MATH 170", "MATH 190"]
intro1 = ["CSCI 0150", "CSCI 0170", "CSCI 0190"]
intro2 = ["CSCI 0160", "CSCI 0180", "CSCI 0320", "CSCI 0330"]
foundations = ["CSCI 0220", "CSCI 1010"]
math = ["MATH 0520", "MATH 540", "MATH 0180", "MATH 0200", "MATH 0350", "APMA 1650", "APMA 1655", "CSCI 1450", "CSCI 540"]
systems = ["CSCI 0330", "CSCI 0320"]
intermediates = foundations + math + systems
upper_level = all_classes[12:]
thousand_level = upper_level[3:]
  


cs_scb = [prereqs, intro1, intro2, foundations, math, systems, intermediates,intermediates,upper_level,thousand_level,thousand_level,thousand_level,thousand_level,thousand_level,thousand_level,thousand_level]
cs_scb_names = ["prereqs", 'intro1', 'intro2', 'foundations', 'math', 'systems', 'intermediates','intermediates','pathway','pathway','pathway','pathway','upper_level','thousand_level','thousand_level','thousand_level',]
cs_ab_names = ['prereqs', 'intro1', 'intro2', 'intermediates', 'intermediates', 'intermediates', 'pathway', 'pathway', 'thousand_level', 'thousand_level']
cs_ab = [prereqs, intro1, intro2, intermediates, intermediates, intermediates, thousand_level, thousand_level, thousand_level, thousand_level]
computer_science_ab = Concentration(10, cs_ab, cs_ab_names, "", "Computer Science AB")
computer_science_scb = Computer_Science_SCB(16, cs_scb, cs_scb_names, "One of the pathway courses must be your senior capstone", "Computer Science SCB")


