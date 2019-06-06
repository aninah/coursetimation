import numpy as np

class Concentration:
	def __init__(self, num_classes, requirement_list, requirement_names, additional_notes):
		self.num_classes = num_classes
		self.reqs = requirement_list
		self.additional_notes = additional_notes
		self.req_names = req_names
		self.classes = []

	"""
	satisfied:
		returns list of all possible classes that satisfy a requirement
	"""	 
	def all_valid_classes():
		if self.classes:
			return self.classes
		all_classes = set()
		for req in self.reqs:
			all_classes.update(req)
		all_classes = list(all_classes)
		self.classes = all_classes
		return all_classes
	
	"""
	satisfied:
		given list of classes taken, 
		returns list of classes fulfilling the concentration
	"""	  
	def satisfied(self, classes_taken):
		satisfied = [0] * self.num_classes
		classes = list(classes_taken)
		for r in range(len(self.reqs)):
			for c in self.reqs[r]:
				if c in classes:
					satisfied[r] = c
					classes.remove(c)
					break
		return satisfied

	"""
	how_many_left:
 		gives number of classes left to fill the major
	"""
	def how_many_left(self, classes_taken):
		left = 0
		satisfied = satisfied(classes_taken)
		for s in satisfied:
			if s == 0:
				left+=1
		return left

	"""
	get_additional_notes:
		returns any additional notes to be aware of to finish the major
	"""
	def get_additional_notes():
		return self.additional_notes





def Computer_Science_SCB(Concentration):
	def __init__(self, num_classes, requirement_list, requirement_names, additional_notes):
		Concentration.__init__(self, num_classes, requirement_list, requirement_names, additional_notes)

	def satisfied(self, classes_taken):
		satisfied = Concentration.satisfied(classes_taken)
		return satisfied

""" /*     ----- PATHWAYS -----     */ """
pathway_names = ["intermediate", "intermediate", "intermediate", "core", "core/related"]
stats = ['APMA 1650', 'APMA 1655', 'CSCI 1450']
linear = ['MATH 0520', 'MATH 0540', 'CSCI 0530']
systems_pathway = Concentration(4, [
	['CSCI 0330'], 
	['CSCI 0320', 'CSCI 0220'], 
	['CSCI 1380', 'CSCI 1670','CSCI 1680'], 
	['CSCI 1950Y', 'ENGN 1640', 'CSCI 1380', 'CSCI 1670','CSCI 1680', 'CSCI 1270', 'CSCI 1320', 'CSCI 1600', 'CSCI 1650', 'CSCI 1660', 'CSCI 1730', 'CSCI 1760']], pathway_names[1:], "")
software_pathway = Concentration(5, [['CSCI 0330'], ['CSCI 0320'], ['CSCI 0220'], ['CSCI 1950Y', 'CSCI 1260', 'CSCI 1320', 'CSCI 1600', 'CSCI 1730' ], ['CSCI 1260', 'CSCI 1320', 'CSCI 1600', 'CSCI 1730', 'CSCI 1950Y', 'CSCI 1270', 'CSCI 1380', "CSCI 1650"]], pathway_names, "")
data_pathway = Concentration(5, [stats, ['CSCI 0320', 'CSCI 0330'], linear, ['CSCI 1270', 'CSCI 1420', 'CSCI 1951A'], ['ECON1660','CSCI 1270', 'CSCI 1420', 'CSCI 1951A', 'CSCI 1550', 'CSCI 1580']], pathway_names, "")
ai_ml_pathway = Concentration(4, [stats,linear,['CSCI 1410', 'CSCI 1420', 'CSCI 1430', 'CSCI 1460', 'CSCI 1470', 'CSCI 1951R'],['CSCI 1951C', 'CSCI 1951K', 'ENGN 1610','CSCI 1410', 'CSCI 1420', 'CSCI 1430', 'CSCI 1460', 'CSCI 1470', 'CSCI 1951R', 'CSCI 1550', 'CSCI 1580', 'CSCI 1951A']], pathway_names[1:], "")
theory_pathway = Concentration(5, [stats, linear, ['CSCI 1010'], ['CSCI 1510', 'CSCI 1550', 'CSCI 1570', 'CSCI 1760'], ['CSCI 1510', 'CSCI 1550', 'CSCI 1570', 'CSCI 1760', 'CSCI 1590', 'CSCI 1810', 'CSCI 1820', 'CSCI 1950H', 'CSCI 1950Y', 'CSCI 1951G', 'CSCI 1951K']], pathway_names, "")
security_pathway = Concentration(5, [['CSCI 0330'],['CSCI 1010'], ['CSCI 0220'] + stats, ['CSCI 1510', 'CSCI 1660', 'CSCI 1650'],['CSCI 1510', 'CSCI 1660', 'CSCI 1650', 'CSCI 1320', 'CSCI 1380', 'CSCI 1670', 'CSCI 1730', 'CSCI 1800', 'CSCI 1950Y', 'CSCI 1951B', 'CSCI 1951F'].reverse()], pathway_names, "")
# visual_pathway = Concentration(4, [['CSCI 0320', 'CSCI 0330'], ['CSCI 1230', 'CSCI 1250', 'CSCI 1280'], ['CSCI 1230', 'CSCI 1250', 'CSCI 1280']])
# Core Courses: Computer Graphics (1230), Introduction to Computer Animation (1250), Intermediate Computer Animation (1280),  Computational Photography (1290), UI/UX (1300), Virtual Reality (1370), Computer Vision (1430), Advanced Animation (1950T), Virtual Reality Software Review (1951S), Interactive Computer Graphics (2240)
# Related Courses: Game Engines (1950U, 1950N), Image Understanding (ENGN1610), Computational Vision (CLPS1520)
# Intermediate Courses: (320 or 330), linear algebra

#consider: making pathway class, return the core + related courses when asked, return list of courses NOT in core/related? 


# concept: pathways are basically mini concentrations. 

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
  
print(upper_level[0])
print(thousand_level[0])

cs_scb = [prereqs, intro1, intro2, foundations, math, systems, intermediates,intermediates,upper_level,thousand_level,thousand_level,thousand_level,thousand_level,thousand_level,thousand_level,thousand_level]
cs_scb_names = ["prereqs", 'intro1', 'intro2', 'foundations', 'math', 'systems', 'intermediates','intermediates','upper_level','thousand_level','thousand_level','thousand_level','thousand_level','thousand_level','thousand_level','thousand_level',]

cs_ab_names = ['prereqs', 'intro1', 'intro2', 'intermediates', 'intermediates', 'intermediates', 'thousand_level', 'thousand_level', 'thousand_level', 'thousand_level']
cs_ab = [prereqs, intro1, intro2, intermediates, intermediates, intermediates, thousand_level, thousand_level, thousand_level, thousand_level]
student_a = ["CSCI 0220", "CSCI 0320", "CSCI 0330", "MATH 0180", "APMA 1650", "CSCI 0150", "MATH 0520", "CSCI 1730", 'CSCI 2240']

computer_science_ab = Concentration(10, cs_ab, cs_ab_names, "")
computer_science_scb = Concentration(16, cs_scb, cs_scb_names, "One of the pathway courses must be your senior capstone")
print(computer_science_scb.satisfied(student_a))
print(computer_science_ab.satisfied(student_a))

