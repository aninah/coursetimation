function parse_classes(class_str) {
	let classes = class_str.split();
	// ,,, finish this method lmfao

}

class Concentration {
	Concentration(num_classes, requirement_list) {
		this.num_classes = num_classes;
		this.requirements = requirement_list;
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
		return satisfied.
	}
}

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