import json
import sqlite3


# open json file, insert into db
with open('courses.json') as json_file:  
    courses = json.load(json_file)
    c = set()
    for course in courses:
        x = course["code"].split()
        if x[0] == "CSCI":
            c.add(course["title"])

    print(len(c))
    print(c)

# # connecting to the database file
# conn = sqlite3.connect('courses.db')
# c = conn.cursor()

# # creating a new SQLite table 
# c.execute('DROP TABLE IF EXISTS courses');
# c.execute('CREATE TABLE courses(key INTEGER PRIMARY KEY, department TEXT, course_num INTEGER, instr TEXT)')

# # open json file, insert into db
# with open('courses.json') as json_file:  
#     courses = json.load(json_file)
#     for course in courses:
#     	# split course code
#     	x = course["code"].split()
#     	if len(x) != 2:
#     		print("ERROR: ", x)
#     		continue
#     	department = x[0]
#     	course_num = x[1]
#     	key = course["key"]
#     	instr = course["instr"]

#     	# insertion
#     	params = (key, department, course_num, instr)
#     	c.execute("INSERT INTO courses (key, department, course_num, instr) VALUES (?, ?, ?, ?)", params)


# # committing changes and closing the connection to the db file
# conn.commit()
# conn.close()