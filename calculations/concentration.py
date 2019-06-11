import numpy as np

# representation of a brown concentration
class Concentration:
	def __init__(self, num_classes, requirement_list, requirement_names, additional_notes, name):
		self.num_classes = num_classes
		self.reqs = requirement_list
		self.additional_notes = additional_notes
		self.req_names = requirement_names
		self.classes = []
		self.name = name

	"""
	percent_complete:
		returns how close you are to completing a pathway
	"""
	def percent_complete(self, classes_taken):
		left = 0
		satisfied = Concentration.satisfied(self, classes_taken)
		for s in satisfied:
			if s != 0:
				left+=1
		return float(left)/self.num_classes

	"""
	all_valid_classes:
		returns list of all possible classes that satisfy a requirement
	"""	 
	def all_valid_classes(self):
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
	def get_additional_notes(self):
		return self.additional_notes

	"""
	get_req:
		returns requirement list for that index
	"""
	def get_req(self, index):
		return self.reqs[index]

	"""
	get_req_name:
		returns requirement name for that index
	"""
	def get_req_name(self, index):
		return self.req_names[index]
