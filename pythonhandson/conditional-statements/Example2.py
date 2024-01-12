'''
elif
- Handling the multiple conditions
- The elif keyword in python a way of saying "if the previous conditions were not true, then try this condition".
- at most only one output [ first true condition] , will not check other conditions after getting one true condition
'''

# Example-1
a = 6
b = 5

if a > 10:
    print('if block')
elif 5 <= b <= 10:
    print('elif block 1')
elif a > b:
    print('elif block 2')
else:
    print('else block')

# Example -2
name = input("Enter the Name: ")

if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Joe':
    print('Hello Joe')
elif name == "Joe":
    print('Hello Arnold')
else:
    print("I don't know who you are!")

print("Normal flow")


# Example-3

#grade example

studentMarks = [10,9,8,7,6]
sumOfMarks = sum(studentMarks)
noOfStudents = len(studentMarks)
avg = sumOfMarks/noOfStudents

print("the average is ",avg)
print(avg,sumOfMarks)

if avg > 9:
    print("A")
elif avg>8:
    print("B")
elif avg>7:
    print("C")
elif avg>6:
    print("D")
else:
    print("Fail")

'''
multiple if statements
- #In multiple if's , each and every condition is checked =>  even if the previous if is true or false
- will get more one output on multiple true conditions
'''

# example-1

data = 10

if data > 10:
    print("HI")
if type(data) is int:
    print("Hey")
if type("10") is str:
    print("Hello")
else:
    print("Bye Bye")

print("Continue from if else")


# Example -2

name = input("Enter the Name: ")

if name == 'Fred':
    print('Hello Fred')
if name == 'Xander':
    print('Hello Xander')
if name == 'Joe':
    print('Hello Joe')
if name == "Joe":
    print('Hello Arnold')
else:
    print("I don't know who you are!")

# Example-3
studentMarks = [10,9,8,7,6]
sumOfMarks = sum(studentMarks)
noOfStudents = len(studentMarks)
avg = sumOfMarks/noOfStudents

print("the average is ",avg)
print(avg,sumOfMarks)

if avg > 9:
    print("A")
if avg>8:
    print("B")
if avg>7:
    print("C")
if avg>6:
    print("D")
else:
    print("Fail")