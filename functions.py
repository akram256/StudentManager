students=[]
def get_students_titlecase():
    student_titlecase = []
    for student in students:
        student_titlecase.append(student["name"].title())
    return student_titlecase

def print_student_titlecase():
    student_titlecase=get_students_titlecase()
    print(student_titlecase) 

def add_student(name, student_id=222):
    student={"name":name, "student_id":student_id}
    students.append(student)

def save_file(student):
    try:
        f=open("student.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f = open("student.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")
           
# student_list=get_students_titlecase()
read_file()
print_student_titlecase()

student_name = raw_input("Enter students name: ")

student_id = input("Enter students ID: ")

add_student(student_name, student_id)
save_file(student_name)
# print_student_titlecase()
