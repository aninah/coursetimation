from concentration import Concentration
from cs_scb import computer_science_scb
from cs_scb import computer_science_ab
import string
import sqlite3

# connecting to the database file
conn = sqlite3.connect('../course_parsing/courses.db')
c = conn.cursor()

def all_classes(course_code):
	result = c.execute("SELECT * FROM courses WHERE department=?", [course_code])
	rows = c.fetchall()
	results = []
	for i in rows:
		s = (i[1] + " " + i[2]).encode(encoding='ascii')
		results.append(s)
	return sorted(set(results))

def series(course_code):
	return [course_code + letter for letter in string.ascii_uppercase]

afri_classes = ['AFRI 0090', 'AFRI 0110C', 'AFRI 0210', 'AFRI 0670', 'AFRI 0980', 'AFRI 0990', 'AFRI 1020C', 'AFRI 1020D', 'AFRI 1030', 'AFRI 1050A', 'AFRI 1050D', 'AFRI 1050E', 'AFRI 1060E', 'AFRI 1060U', 'AFRI 1100X', 'AFRI 1110', 'AFRI 1150', 'AFRI 1190', 'AFRI 1210', 'AFRI 1360', 'AFRI 1920', 'AFRI 1930', 'AFRI 1970', 'AFRI 2001', 'AFRI 2002', 'AFRI 2102', 'AFRI 2300', 'AFRI 2970', 'AFRI 2980', 'AFRI 2990', 'AFRI XLIST']
afri_xlist = afri_classes + ["ENGL 0700E", "ENGL 1711N", "POLS 1335", "POLS 1820E", "RELS 0822"]
africana_studies = Concentration(8, 
	[afri_classes,afri_classes,afri_classes,afri_classes,afri_classes,afri_classes,afri_xlist,afri_xlist ], 
	["AFRI course"]*8 + ["AFRI cross list"]*2, "- beginning with Class of 2021, an additional junior seminar in spring semester is required.", "Africana Studies")


amst_classes = ['AMST 1220', 'AMST 1600H', 'AMST 1611A', 'AMST 1612Q', 'AMST 1700F', 'AMST 1700N', 'AMST 1700X', 'AMST 1800', 'AMST 1800A', 'AMST 1900P', 'AMST 1901B', 'AMST 1901M', 'AMST 1903I', 'AMST 1903Z', 'AMST 1904H', 'AMST 1905O', 'AMST 1906A', 'AMST 1906R', 'AMST 1970', 'AMST 2010', 'AMST 2020E', 'AMST 2200O', 'AMST 2220I', 'AMST 2220J', 'AMST 2220L', 'AMST 2220P', 'AMST 2220Q', 'AMST 2220R', 'AMST 2520', 'AMST 2540', 'AMST 2635', 'AMST 2650', 'AMST 2653', 'AMST 2655', 'AMST 2660', 'AMST 2680', 'AMST 2685', 'AMST 2694', 'AMST 2920', 'AMST 2921', 'AMST 2922', 'AMST 2923', 'AMST 2950', 'AMST 2990']
amst_upper = series("APMA 1700") + series("APMA 1800") + series("APMA 1900")
american_studies = Concentration(10, 
	[series("AMST 1700"), series("AMST 1900"), amst_upper, amst_upper] + [amst_classes]*6, 
	["AMST 1700 series", "AMST 1900 series"] + ["AMST 1700, 1800, or 1900 series"]*2 + ["American Studies 1000 level course"] * 6, 
	"All seniors are required to do a capstone electronic portfolio.", "American Studies")

anthropology_classes = ['ANTH 0066D', 'ANTH 0066N', 'ANTH 0100', 'ANTH 0300', 'ANTH 0310', 'ANTH 0500', 'ANTH 0800', 'ANTH 1030', 'ANTH 1125', 'ANTH 1150', 'ANTH 1240', 'ANTH 1242', 'ANTH 1253', 'ANTH 1300', 'ANTH 1301', 'ANTH 1553', 'ANTH 1599', 'ANTH 1621', 'ANTH 1623', 'ANTH 1720', 'ANTH 1750', 'ANTH 1830', 'ANTH 1901', 'ANTH 1910B', 'ANTH 1911', 'ANTH 1940', 'ANTH 1970', 'ANTH 1990', 'ANTH 2000', 'ANTH 2010', 'ANTH 2020', 'ANTH 2045', 'ANTH 2050', 'ANTH 2055', 'ANTH 2501', 'ANTH 2515', 'ANTH 2520', 'ANTH 2590', 'ANTH 2800', 'ANTH 2970', 'ANTH 2980', 'ANTH 2990']
anth_1910 = ["ANTH 1910" + letter for letter in string.ascii_uppercase]
anthropology = Concentration(9, 
	[["ANTH 0100", "ANTH 0110", "ANTH 0200", "ANTH 0300", "ANTH 0800"], ["ANTH 0310", "ANTH 0500"], ["ANTH 1621", "ANTH 1900", "ANTH 1940", "ANTH 1950"], anth_1910] + [anthropology_classes] * 6, 
	["Sociocultural/Linguistic Anthropology Course", "Biological anthropology/Archaeology Course", "Anthropological Research", "ANTH 1910 series"] + ["ANTH course"] * 5, 
	"", "Anthropology")


apma_classes = ['APMA 1070', 'APMA 1080', 'APMA 1160', 'APMA 1170', 'APMA 1180', 'APMA 1200', 'APMA 1210', 'APMA 1330', 'APMA 1360', 'APMA 1650', 'APMA 1655', 'APMA 1660', 'APMA 1681', 'APMA 1690', 'APMA 1710', 'APMA 1740', 'APMA 1930T', 'APMA 1930U', 'APMA 1940Z', 'APMA 1970', 'APMA 2110A', 'APMA 2120A', 'APMA 2190', 'APMA 2200', 'APMA 2230', 'APMA 2240', 'APMA 2420', 'APMA 2550', 'APMA 2560', 'APMA 2570B', 'APMA 2580A', 'APMA 2610', 'APMA 2630', 'APMA 2640', 'APMA 2670', 'APMA 2811Z', 'APMA 2812A', 'APMA 2812B', 'APMA 2980', 'APMA 2990']
applied_math_ab = Concentration(12, [["MATH 0090"], ["MATH 0100"], ["MATH 0180"], ["MATH 0520", "MATH 0540"], ["APMA 0350", "APMA 0330"], ["APMA 0360", "APMA 0340"], ["CSCI 0040", "CSCI 0150","CSCI 0170", "APMA 0090", "APMA 0160"], apma_classes * 5], 
	["Prerequisite", "Prerequisite", "Intermediate Calculus", "Linear Algebra", "Applied Differential Equations I", "Applied Differential Equations II", "Programming Course"]+["Upper Level APMA"]*5,
	"", "Applied Math AB")
applied_math_scb = Concentration(18, 
	[["MATH 0090"], ["MATH 0100"], ["MATH 0180"], ["MATH 0520", "MATH 0540"], ["APMA 0350", "APMA 0330"], ["APMA 0360", "APMA 0340"], ["CSCI 0040", "CSCI 0150","CSCI 0170", "APMA 0090", "APMA 0160"], series("APMA 1930") + series("APMA 1940"),apma_classes * 10], 
	["Prerequisite", "Prerequisite", "Intermediate Calculus", "Linear Algebra", "Applied Differential Equations I", "Applied Differential Equations II", "Programming Course", "Senior Seminar Series"]+["Upper Level APMA"]*10,
	"", "Applied Math SCB")




conn.close()



