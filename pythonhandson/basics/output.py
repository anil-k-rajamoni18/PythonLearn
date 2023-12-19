"""
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

attributes
    - value
    - sep = ' '
    - end = '\n' # new line
    - file = sys.stdout [monitor]
    - flush = False

"""

print('Iam learning python')  # string - group of character(alpha+numbers+symbols)
print(10)  # integers
print(10.2)  # floats
print(False)  # boolean [True, False]
print(10 + 2j)  # complex  real + imag consant (x+iy) (a+ib)
print([10, 20, 30, 40])  # list
print(('india', 'aus', 'usa'))  # tuple (val1, val2, val3)
print({'orange', True, 'red', 'yellow', 'red'})  # set {val1,val2, val3}
print({'name': 'kumar', 'lang': 'python', 'rating': 4.5})  # dict {k:v}

name = 'chitra'
college_name = 'NJIT'
gpa = 3.6

print(name)
print(college_name)
print(gpa)

# print multiple variable in a single print() method
print(name, college_name, gpa)  # sep = ' ' is the default separator when having multiple values

# overriding separator value sep = ','
print(name, college_name, gpa, sep='--->')

# end = '\n' --> new line , \t --> tab space
world_cup_winner = 'Aus'
world_cup_runner = 'India'
print(world_cup_winner)
print() # end = '\n'
print()
print()
print(world_cup_runner)

#  file = sys.stdout --> mointor
print("Hello World Learning print methon in details", file=open('file_op.txt', mode='a'))
print("India lost the 2023 ICC world cup", file=open('file_op.txt', mode='a'))


