# declare 5 different realtime  variable names, print it's value & type & address

student1_age = 26
student_name = "venkatesh"
student_fee = 980282.22
student_grade = 'F'
gpa = 3.9

student2_age = 27

is_student = True
skills = ['c', 'c++', 'python']

print(student1_age, type(student1_age), id(student1_age))
print(student_name, type(student_name), id(student_name))
print(student_fee, type(student_fee), id(student_fee))
print(is_student, type(is_student), id(is_student))
print(skills, type(skills), id(skills))

print(ord('A')) # it will display ascii number mapped to character
print(chr(78)) # it will display character mapped to number
