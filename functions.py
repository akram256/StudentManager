students=[]
def get_students_titlecase():
    student_titlecase = []
    for student in students:
        student_titlecase = student["name"].title()
    return student_titlecase

def print_student_titlecase():
    student_titlecase=get_students_titlecase()
    print(student_titlecase) 

def add_student(name, student_id=222):
    student={"name":name, "student_id":student_id}
    students.append(student)
    
student_list=get_students_titlecase()

student_name = raw_input("Enter students name : ")
student_id = input("Enter students ID: ")

add_student(student_name, student_id)
print_student_titlecase()
