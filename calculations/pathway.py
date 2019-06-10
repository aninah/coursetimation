from concentration import Concentration

# representation of a computer science pathway
class Pathway(Concentration):
	def __init__(self, x, y, z, a):
		Concentration.__init__(self, x, y, z, a)

	"""
	get_core_related:
		returns the core and related classes for the pathway
	"""
	def get_core_related(self):
		return self.reqs[-1]

	"""
	non_get_core_related:
		returns all classes given that are not in core/related for the pathway
	"""
	def get_non_core_related(self, class_selection):
		return [c for c in class_selection if c not in self.get_core_related()]

	"""
	percent_complete:
		returns how close you are to completing a pathway
	"""
	def percent_complete(self, classes_taken):
		left = 0
		satisfied = Concentration.satisfied(self, classes_taken)
		for s in satisfied:
			if s == 0:
				left+=1
		return float(left)/self.num_classes



"""     ----- ALL PATHWAYS -----      """
pathway_names = ["intermediate", "intermediate", "intermediate", "core", "core/related"]
stats = ['APMA 1650', 'APMA 1655', 'CSCI 1450']
linear = ['MATH 0520', 'MATH 0540', 'CSCI 0530']

systems = Pathway(4, [
	['CSCI 0330'], 
	['CSCI 0320', 'CSCI 0220'], 
	['CSCI 1380', 'CSCI 1670','CSCI 1680'], 
	['CSCI 1950Y', 'ENGN 1640', 'CSCI 1380', 'CSCI 1670','CSCI 1680', 'CSCI 1270', 'CSCI 1320', 'CSCI 1600', 'CSCI 1650', 'CSCI 1660', 'CSCI 1730', 'CSCI 1760']], 
	pathway_names[1:], "")
software = Pathway(5, [
	['CSCI 0330'], 
	['CSCI 0320'], 
	['CSCI 0220'], 
	['CSCI 1950Y', 'CSCI 1260', 'CSCI 1320', 'CSCI 1600', 'CSCI 1730' ], 
	['CSCI 1260', 'CSCI 1320', 'CSCI 1600', 'CSCI 1730', 'CSCI 1950Y', 'CSCI 1270', 'CSCI 1380', "CSCI 1650"]], 
	pathway_names, "")
data = Pathway(5, [
	stats, 
	['CSCI 0320', 'CSCI 0330'], 
	linear, 
	['CSCI 1270', 'CSCI 1420', 'CSCI 1951A'], 
	['ECON1660','CSCI 1270', 'CSCI 1420', 'CSCI 1951A', 'CSCI 1550', 'CSCI 1580']], 
	pathway_names, "")
ai_ml = Pathway(4, [
	stats,
	linear,
	['CSCI 1410', 'CSCI 1420', 'CSCI 1430', 'CSCI 1460', 'CSCI 1470', 'CSCI 1951R'],
	['CSCI 1951C', 'CSCI 1951K', 'ENGN 1610','CSCI 1410', 'CSCI 1420', 'CSCI 1430', 'CSCI 1460', 'CSCI 1470', 'CSCI 1951R', 'CSCI 1550', 'CSCI 1580', 'CSCI 1951A']], 
	pathway_names[1:], "")
theory = Pathway(5, [
	stats, 
	linear, 
	['CSCI 1010'], 
	['CSCI 1510', 'CSCI 1550', 'CSCI 1570', 'CSCI 1760'], 
	['CSCI 1510', 'CSCI 1550', 'CSCI 1570', 'CSCI 1760', 'CSCI 1590', 'CSCI 1810', 'CSCI 1820', 'CSCI 1950H', 'CSCI 1950Y', 'CSCI 1951G', 'CSCI 1951K']], 
	pathway_names, "")
security = Pathway(5, [
	['CSCI 0330'],
	['CSCI 1010'], 
	['CSCI 0220'] + stats, 
	['CSCI 1510', 'CSCI 1660', 'CSCI 1650'],
	['CSCI 1510', 'CSCI 1660', 'CSCI 1650', 'CSCI 1320', 'CSCI 1380', 'CSCI 1670', 'CSCI 1730', 'CSCI 1800', 'CSCI 1950Y', 'CSCI 1951B', 'CSCI 1951F']], 
	pathway_names, "")
visual = Pathway(4, [
	['CSCI 0320', 'CSCI 0330'], 
	linear, 
	['CSCI 1230', 'CSCI 1250', 'CSCI 1280', "CSCI 1290", "CSCI 1300", "CSCI 1370", "CSCI 1430", "CSCI 1950T", "CSCI 1951S", "CSCI 2240"], 
	['CSCI 1230', 'CSCI 1250', 'CSCI 1280', "CSCI 1290", "CSCI 1300", "CSCI 1370", "CSCI 1430", "CSCI 1950T", "CSCI 1951S", "CSCI 2240", "CSCSI 1950U", "CSCI 1950N", "ENGN 1610", "CLPS 1520"]], 
	pathway_names[1:], "")
computer_arch = Pathway(3, [
	["CSCI 0330"], 
	["ENGN 1630", "ENGN 1640", "ENGN 1650"], 
	["ENGN 1630", "ENGN 1640", "ENGN 1650", "CSCI 1600", "CSCI 1760", "ENGN 1600"]], 
	pathway_names[2:], "")
comp_bio = Pathway(5, [
	stats, 
	["CSCI 0220"], 
	["CSCI 1010"], 
	["CSCI 1810", "CSCI 1820"], 
	["CSCI 1810", "CSCI 1820", "CSCI 1420", "CSCI 1951A", "CLPS 1520"]], pathway_names, "")
design = Pathway(4, [
	stats, 
	["CSCI 0320", "CSCI 0330"],
	["CSCI 1300", "CSCI 1370", "CSCI 1951C"], 
	["CSCI 1300", "CSCI 1370", "CSCI 1951C", "CSCI 1230", "CSCI 1320", "CSCI 1600", "CSCI 1951A", "CSCI 1900", "VISA 1720"]], 
	pathway_names[1:], "")
pathways = [systems, software, data, ai_ml, theory, security, visual, computer_arch, comp_bio, design]