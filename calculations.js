function parse_classes(class_str) {
	let classes = class_str.split();
	// ,,, finish this method lmfao

}

class Concentration {
	Concentration(num_classes, requirement_list, special_cases, additional_notes) {
		this.num_classes = num_classes;
		this.requirements = requirement_list;
		this.special_cases = special_cases;
		this.additional_notes = additional_notes;
	}

	how_many_satisfy(classes_taken) {
		let satisfied = new Array(this.num_classes).fill(0);
		// for each requirement
		for (var i = 0; i < this.requirements.length; i++) {
			let reqs = this.requirements[i];
			// there's a list of possible classes fulfilling it
			for (var j = 0; j < reqs.length; j++) {
				// if you have one of those classes...
				let ind = classes_taken.indexOf(reqs[j]);
				if (ind != -1) {
					satisfied[i] = reqs[j];
					classes_taken.splice(ind, 1);
					continue;
				}
			}
		}


		return satisfied;
	}

	how_many_left(classes_taken) {
		let left = 0;
		let satisfied = how_many_satisfy(classes_taken);
		for (var i = 0; i < satisfied.length; i++) {
			if (satisfied[i] == 0) {
				left++;
			}
		}
		return left;
	}

	get_additional_notes() {
		return this.additional_notes;
	}
}

let prereqs = ["MATH 100", "MATH 170", "MATH 190"];
let intro1 = ["CSCI 0150", "CSCI 0170", "CSCI 0190"];
let intro2 = ["CSCI 0160", "CSCI 0180"];
let foundations = ["CSCI 0220", "CSCI 1010"];
let math = ["CSCI 540", "MATH 0520", "MATH 540", "MATH 0180", "MATH 0200", "MATH 0350", "APMA 1650", "APMA 1655", "CSCI 1450"];
let systems = ["CSCI 0330", "CSCI 0320"];
let all = ['CSCI 0020', 'CSCI 0030', 'CSCI 0081', 'CSCI 0082', 'CSCI 0100', 'CSCI 0111', 'CSCI 0130', 'CSCI 0150', 'CSCI 0160', 'CSCI 0170', 'CSCI 0180', 'CSCI 0190', 'CSCI 0220', 'CSCI 0320', 'CSCI 0330', 'CSCI 0530', 'CSCI 1010', 'CSCI 1230', 'CSCI 1234', 'CSCI 1250', 'CSCI 1260', 'CSCI 1270', 'CSCI 1280', 'CSCI 1300', 'CSCI 1320', 'CSCI 1370', 'CSCI 1380', 'CSCI 1410', 'CSCI 1420', 'CSCI 1430', 'CSCI 1450', 'CSCI 1460', 'CSCI 1470', 'CSCI 1550', 'CSCI 1570', 'CSCI 1575', 'CSCI 1600', 'CSCI 1650', 'CSCI 1670', 'CSCI 1680', 'CSCI 1690', 'CSCI 1730', 'CSCI 1800', 'CSCI 1805', 'CSCI 1810', 'CSCI 1820', 'CSCI 1870', 'CSCI 1900', 'CSCI 1950N', 'CSCI 1950Y', 'CSCI 1951A', 'CSCI 1951C', 'CSCI 1951I', 'CSCI 1951K', 'CSCI 1951R', 'CSCI 1970', 'CSCI 1971', 'CSCI 1972', 'CSCI 2240', 'CSCI 2270', 'CSCI 2470', 'CSCI 2500B', 'CSCI 2890', 'CSCI 2950V', 'CSCI 2951F', 'CSCI 2951I', 'CSCI 2951K', 'CSCI 2951U', 'CSCI 2952F', 'CSCI 2952G', 'CSCI 2980', 'CSCI 2990'];
let upper_level = ['CSCI 0220', 'CSCI 0320', 'CSCI 0330', 'CSCI 0530', 'CSCI 1010', 'CSCI 1230', 'CSCI 1234', 'CSCI 1250', 'CSCI 1260', 'CSCI 1270', 'CSCI 1280', 'CSCI 1300', 'CSCI 1320', 'CSCI 1370', 'CSCI 1380', 'CSCI 1410', 'CSCI 1420', 'CSCI 1430', 'CSCI 1450', 'CSCI 1460', 'CSCI 1470', 'CSCI 1550', 'CSCI 1570', 'CSCI 1575', 'CSCI 1600', 'CSCI 1650', 'CSCI 1670', 'CSCI 1680', 'CSCI 1690', 'CSCI 1730', 'CSCI 1800', 'CSCI 1805', 'CSCI 1810', 'CSCI 1820', 'CSCI 1870', 'CSCI 1900', 'CSCI 1950N', 'CSCI 1950Y', 'CSCI 1951A', 'CSCI 1951C', 'CSCI 1951I', 'CSCI 1951K', 'CSCI 1951R', 'CSCI 1970', 'CSCI 1971', 'CSCI 1972', 'CSCI 2240', 'CSCI 2270', 'CSCI 2470', 'CSCI 2500B', 'CSCI 2890', 'CSCI 2950V', 'CSCI 2951F', 'CSCI 2951I', 'CSCI 2951K', 'CSCI 2951U', 'CSCI 2952F', 'CSCI 2952G', 'CSCI 2980', 'CSCI 2990'];
let thousand_level = ['CSCI 1010', 'CSCI 1230', 'CSCI 1234', 'CSCI 1250', 'CSCI 1260', 'CSCI 1270', 'CSCI 1280', 'CSCI 1300', 'CSCI 1320', 'CSCI 1370', 'CSCI 1380', 'CSCI 1410', 'CSCI 1420', 'CSCI 1430', 'CSCI 1450', 'CSCI 1460', 'CSCI 1470', 'CSCI 1550', 'CSCI 1570', 'CSCI 1575', 'CSCI 1600', 'CSCI 1650', 'CSCI 1670', 'CSCI 1680', 'CSCI 1690', 'CSCI 1730', 'CSCI 1800', 'CSCI 1805', 'CSCI 1810', 'CSCI 1820', 'CSCI 1870', 'CSCI 1900', 'CSCI 1950N', 'CSCI 1950Y', 'CSCI 1951A', 'CSCI 1951C', 'CSCI 1951I', 'CSCI 1951K', 'CSCI 1951R', 'CSCI 1970', 'CSCI 1971', 'CSCI 1972', 'CSCI 2240', 'CSCI 2270', 'CSCI 2470', 'CSCI 2500B', 'CSCI 2890', 'CSCI 2950V', 'CSCI 2951F', 'CSCI 2951I', 'CSCI 2951K', 'CSCI 2951U', 'CSCI 2952F', 'CSCI 2952G', 'CSCI 2980', 'CSCI 2990'];

let req_list = [
	prereqs, 
	intro1, 
	intro2, 
	foundations, 
	math, 
	systems, 
	foundations.concat(math, systems),
	foundations.concat(math, systems),
	upper_level,
	thousand_level,
	thousand_level,
	thousand_level,
	thousand_level,
	thousand_level,
	thousand_level,
	thousand_level,
	 ];

let student_a = ["CSCI 0220", "CSCI 0320", "CSCI 0330", "MATH 0180", "APMA 1650", "CSCI 0150", "CSCI 0520", "CSCI 1730", 'CSCI 2240']

let computer_science = new Concentration(16, req_list);
console.log(computer_science.how_many_satisfy(student_a);
	


// idea: always know the number of courses required, right? 
// maybe some kind of list of lists? dict of lists?
// class 1: cs15/17/19
// class 2: cs16/18/cs+ (priority on first two)
// class 3: intermediate foundation : cs22, cs1010
// class 4: intermediate math: math52, math 180, math

// rules for cs:
// 1. prereq calc
// 2. cs15/cs17/cs19
// 3. cs16/cs18/ if 2 == cs19, csx
// 4. intermediates:
// 		foundations: cs22, cs1010
// 		math: math52/math54, apma1650/cs1450/apma1655, math180/math200/math350
// 		systems: cs32, cs33
//	- 5 from 7
//  - 1 from each minimum
// 5. pathways:
		// 1. 1 core, 1 core or related, all intermediates
		// 2. 1 core, 1 core or related, all intermediates
// 6. 1 1000+ non core non related
// 7. 2 1000+
// 8. 1 CS220+