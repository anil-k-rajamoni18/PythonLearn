'''
print()
------------
1.What does the print() function do in Python?
2.How do you print a string in Python?
3.Can you print multiple items with a single print() function call?
4.How do you print variables along with strings?
5.How can you control the separator between printed items?
6.How do you print 3 variables without a newline at the end?

variables
---------------
1.How do you create a variable in Python?
2.What are the rules for naming variables in Python?
3.How do you assign a value to a variable?
4.Can a variable change types in Python? Provide an example.
5.How do you swap the values of two variables in Python?
6.What happens if you use a variable that hasn't been defined?
'''

# 1: answer 
# The print() function in Python used to print data/variables on the screen
print('Hello World')

# 2: answer
name = "Virat"
print(name)

# 3: answer: yes 
a = 10
b = "india"
c = 10.5
print(a,b,c)


# 4: answer
age = 18
print(age, "years")

# 5.: answer ->  you can control the separator using the attribute sep = ''
print(a,b,c, sep = " , ")

# 6: answer
print(a, end = " ") # end = "\n" overriding with space
print(b, end = " ")
print(c, end = " ")

## VARIABLES #############

# 1. variableName = value 
person_name = "John"
print(person_name)

# 2. Variable rules
# 1. must starts with letter or underscore 
carName = "Tata Ev"
_ = "9L"

# 2. shouldn't start with number(0-9)
# 9price ="10"

# 3. can contain alpha numeric characters (letters + symbols + numbers)
no_of_students_in_10_class = 150

# 4. variables are case sensitive 
price = 10
Price = 20
PRICE = 30 

# 5. can't have same name as python keyword
# if = 10 # errror 
# for = "hello" # error 

# 3: answer
age = 27 
print(age)

# 4:answer
a = 10
print(a, type(a))

a = "hello python learners"
print(a, type(a))

# 5:answer
x = 30
y = 50
print(x,y)

# after swapping

# temp = x
# x = y
# y = temp 

x, y = y, x
print(x,y)

# 6: answer

# print(z) # it will throw NameError 