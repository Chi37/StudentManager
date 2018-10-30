students = []


def get_student_name():
	student_name = input("Enter student name: ")
	student_id = input("Enter student id: ")


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
#to add students is written like add_student("Mark")


def get_user_input():
	user_input = input("Do you want to add a student?")
	if user_input == "yes":
		insert_student_info()


def save_file(student):
	try:
		f = open("students.txt","a")
		f.write(student + "\n")
		f.close()
	except:
		print("Could not save file")


def read_file():
	try:
		f = open("students.txt","r")
		for student in f.readlines():
			add_student(student)
			print("reading...")
		f.close()
	except Exception:
		print("could not read file")

    
read_file()
print_students_titlecase()


student_name = input("Enter student name: ")
student_id = input("Enter student id: ")


add_student(student_name)
save_file(student_name)


