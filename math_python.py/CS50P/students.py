
def students_list():

	students = ["student1", "student2", "student3","student4"]

	for student in students:
		print(student)

##students_list()
## created a method for students

def students_dict():

	students = {
		"Rafa": "Tims",
		"Timmy": "Adams",
		"Donnny": "Stans",
		"Micheal": "Jordon",
		"Jerry": "Rice"
}

	for student in students:
		print(student, students[student], sep=" + ")

students_dict()		
