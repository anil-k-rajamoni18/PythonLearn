'''
OPERATORS : symbol , which does operation

- Python language supports several types of operators
- Operator is symbol which applies on operands
    ex: a + b ==> a, b operands , + --> operator.
'''

# Assignment Operators.

print('******** Assignment & Compound Assignment ********')
name = 'kumar'  # assignment operator
price = 60

# increase price by 12
price = price + 12
print(price)

# decrease price by 5
price = price - 5
print(price)

# increase price by 10 using compound assignment
price += 10 # price = price + 10
print(price)

# decrease price by 3  using compound assignment
price -= 3
print(price)

# multiply price by 2  using compound assignment
price *= 2  # price = price * 2
print(price)

# divide price by 5
price /= 5
print(price)

# Arithmetic Operators +, - , * , / , **, //
print('*************** Arithmetic Operators **************')
print(f'Addition : {10 + 20}')
print(f'Addition: {(-10 + 6)}')
print(f'Difference: {10 - 40}')
print(f'Multiplication: {10 * 3}')
print(f'Multiplication: {10 * 0}')
print(f'Division: {10 / 3}')
# print(f'Division: {10/0}') # ZeroDivisionError
print(f'Floor Division: {10 // 3}')  # integer part
print(f'Floor Division: {5 // 2}')
# print(f'Floor Division: {10//0}') # ZeroDivisionError
print(f'Expo: {2 ** 3}')

print(f'Modulus: {10 % 3}')
print(f'Modulus: {4 % 2}')
print(f'Modulus: {5 % 5}')
# print(f'Modulus: {7 % 0}') # ZeroDivisionError
print(f'Modulus: {50 % 100}')

'''
# NOTE : 
1. Numerator<Demo ---> Answer is Numerator
2. Numerator == Demo --> 0
3. Numerator> Demo (get remainder doing division method)
4. Demo == 0 or 0.0 --> Raise Zero Division Error
'''

# Calculating area of a circle
radius = 10  # radius of a circle
area_of_circle = 3.14 * radius ** 2  # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(f'Weight {weight} N')  # Adding unit to the weight

# Calculate the density of a liquid
mass = 75  # in Kg
volume = 0.075  # in cubic meter
density = (mass / volume)  # 1000 Kg/m^3

print(f'density {density}')

print('*************** Comparison Operators **************')

print(10 > 3)
print(10 >= 3)
print(5 < 2)
print(5 <= 2)
print(5 <= 5)
print(10 == 3)
print(10 == 10)
print(10 != 4)
print(10 != 10)
print('a' == 'A')  # 97 == 65
print('K' > 'a')  # 75 > 97
print('Hi' > 'Hello')  # 72 == 72, 105 > 101
print('Bye' > 'bye')
print('Bye' == 'bye')
print('Hello' == 'HellO')
print('Hello' > 'HeLlo')

# MemberShip Operator
'''
    in: Returns True if the queried sequence contains a certain item(x in y)
    not in: Returns True if the queried list doesn't have a certain item(x not in y)
'''

print('************* MemberShip Operator ***************')
colors = {'red', 'blue', 'yellow', 'orange'}

print('red' in colors)
print('skyblue' in colors)
print('RED' in colors)
print('yellow' not in colors)
print('black' not in colors)

print('A in Asabeneh', 'A' in 'Asabeneh')  # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh')  # False - there is no uppercase B
print('coding' in 'coding for all')  # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')  # True

# dictionary with in operators
person = {'name': 'venkat', 'course': 'devops', 'duration': 4}
print('venkat' in person)
print('course' in person)
print('devops' in person.values())

# Identity Operator
print('************ Identity Operator **************')
'''
is: Returns true if both variables are the same object(x is y)
is not: Returns true if both variables are not the same object(x is not y)
'''
a = 10  # primitive [int, float, boolean,complex, None]
b = 10
print(a is b)
print("int", id(a), id(b))

x = 10.5
y = 10.5
z = 10.5
print(x is y)
print(y is z)
print("float", id(x), id(y), id(z))

b1 = True
b2 = True
print(b1 is b2)
print("boolean", id(b1), id(b2))

c1 = 1 + 2j
c2 = 1 + 2j
print(c1 is c2)
print("complex ", id(c1), id(c2))

n1 = None
n2 = None
print(n1 is n2)
print("None", id(n1), id(n2))

s1 = "hello"
s2 = "hello"
print(s1 is s2)
print("string", id(s1), id(s2))

lst1 = [10, 20, 30]  # collection/sequence
lst2 = [10, 20, 30]
print(lst1 is lst2)  # address is comparing
print(lst1 is not lst2)
print(lst1 == lst2)  # comparing content
print("collections", id(lst1), id(lst2))

# LOGICAL OPERATORS
print('********* logical operators *************')

username = "fury"
passwd = 1234
print(username == ['fury'] and passwd == 1234)  # both
print(username == "fur" or passwd == 1234)  # atleast
print(not (username == "fury" and passwd == 1234))
print(username == "fury" and passwd == 1234)

# login
database = {"username": "kumar", "passwd": "kumar123"}

username = input("Enter the username: ")
passwd = input("Enter the password: ")

if username == database['username']:
    if passwd == database['passwd']:
        print('Login Success :) ')
    else:
        print(f'password {passwd} is not valid')
else:
    print(f'invalid username : {username}')


if username == database['username'] and passwd == database['passwd']:
    print('login success')
else:
    print('invalid credentials.')

