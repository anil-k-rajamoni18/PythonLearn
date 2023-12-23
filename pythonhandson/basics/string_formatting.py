studentname = 'chitra'
course = 'Java'
fee = 12300.235252725
print(studentname, course)

print('My name is', studentname)
print('I Have registered', course)

# Normally way
print('My name is', studentname, 'I have registered', course, 'and fee is', fee)

# String.format()
print('My name is {0}, I have registered {1} and fee is {2}'.format(studentname,course,fee))

# f String
print(f'My name is {studentname}, I have registered {course} and fee is {fee}')

