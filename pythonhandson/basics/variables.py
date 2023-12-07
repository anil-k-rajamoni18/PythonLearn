"""
VARIABLES IN PYTHON
-------------------------------------------
- Variable is name assigned to memory location
- Variable posses variability property


Python Variable Name Rules

1. A variable name must start with a letter or the underscore character
2.A variable name cannot start with a number[0-9]
3.A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4.Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)
5.A variable cannot have same name as Reserved word or KEYWORD.

"""

# 1. A variable name must start with a letter or the underscore character

name = 'kumar'
lang = 'python'
rating = 3.5

print(name)
print(lang)
print(rating)

name = 'Venkat'
rating = 4.5
print(name)
print(rating)

_college = "NJIT"
print(_college)

_ = 200
__ = 300

print(_)
print(__)

# 2. A variable name cannot start with a number[0-9]
# 9cricket_score = 239
# print(9cricket_score)


# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
student_10th_marks = 960
print(student_10th_marks)

# 4. Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)
age = 10
Age = 30
AGE = 20
print(age)
print(Age)
print(AGE)

# 5.A variable cannot have same name as Reserved word or KEYWORD.

# import keyword
# print(keyword.kwlist, len(keyword.kwlist))

'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
'break', 'class', 'continue', 'def', 'del', 'elif', 
'else', 'except', 'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
'raise', 'return', 'try', 'while', 'with', 'yield']

'''

# lambda = "chitra"
# print(lambda)

True_ = 10
print(True_)


large_num = 922337203685477580800000000000000000000000000000222223003030300000000000000000000000000229929200202320383
print(large_num)

# first-name = "kumar"
# print(first-name)


#  STYLE CASES
#  camleCase

a = 100
b = 3.844e8

myAccountBalance = 100
distanceToMoon = 3.844e8

print(myAccountBalance, distanceToMoon)

# snake_case
student_name = "chitra"
student_marks = 87
number_of_students_in_college = 400

print(student_marks, student_marks, number_of_students_in_college)