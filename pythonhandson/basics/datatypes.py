"""
DATATYPES: defines type of data stored in variable

- In python we have
    - integers
    - floating
    - strings
    - booleans
    - complex
    - list []
    - set {}
    - dict {}
    - tuple ()
"""

name = "Chitra"
age = 25
college_name = "NJIT"
gpa = 3.5
skills = ["c", "aws", "python"]
is_student = True

#  type(variable_name) --> displays variable mapped data type

print(type(name))
print(type(age))
print(type(college_name))
print(type(gpa))

print(type(skills))
print(type(is_student))

name = 200
print(type(name))

# id(variable_name) --> display memory address

print(id(name))
print(id(gpa))
print(id(skills))