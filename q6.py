def student_data(student_id, student_name , student_class):
    print(f'\nStudent ID: {student_id}')
    if student_name == '':
            True
    else:
        print(f"Student Name = {student_name}")

    if student_class == '':
        True
    else:
        print(f"Student Class = {student_class}")


a  = input("Enter Your Student ID :-  ")
enter_student_name = input("Type Y to enter name else type N :-  ")
if enter_student_name == 'Y' :
    b  = input("Enter Your student name :-  ")
else:
    b = ''
enter_student_class = input("Type Y to enter name else type N:-  ")
if enter_student_class == 'Y' :
    c  = input("Enter Your student class :-  ")
else:
    c = ''

student_data(student_id= a ,student_name= b , student_class= c )
