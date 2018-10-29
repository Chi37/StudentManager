students = []


def get_students_titlecase():
	students_titlecase = []
	for student in students:
		students_titlecase = student["name"].title()
	return students_titlecase


def print_students_titlecase():
	students_titlecase = get_students_titlecase()
	print(students_titlecase)


def add_student(name, student_id=0):
	student = {"name": name, "student_id": student_id}
	students.append(student)


student_list = get_students_titlecase()
#to add students is wrritten like add_student("Mark")

def insert_student_info():
	student_name = input("Enter student name: ")
	student_id = input("Enter student id: ")
	add_student(student_name, student_id)
	print_students_titlecase()


def get_user_input():
	user_input = input("Do you want to add a student?")
	if user_input == "yes":
		insert_student_info()
	else:
		print("thanks")

get_user_input()

