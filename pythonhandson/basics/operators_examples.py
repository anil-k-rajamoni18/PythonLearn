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
price += 10
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
print('Hi' > 'Hello') # 72 == 72, 105 > 101
print('Bye' > 'bye')
print('Bye' == 'bye')
print('Hello' == 'HellO')
print('Hello' > 'HeLlo')




