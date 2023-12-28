studentname = 'chitra'
course = 'Java'
fee = 12300.235252725

print(studentname, course, fee)

print('My name is', studentname)
print('I Have registered', course)

# Normally way
print('My name is', studentname, 'I have registered', course, 'and fee is', fee)

# String.format()
print('My name is {0}, i have registered {1}, and fee is {2:.3f}'.format(studentname,course,fee))

# f String [3.6+]
print(f'My name is {studentname}, I have registered {course}, and fee is {fee}')
print(f'My name is {studentname}, I have registered {course}, and fee is {fee:.3f}')

