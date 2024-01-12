# sequential statements
numbers = [10, 20, 30]
print('hello world python')
print(f'0th index is : {numbers[0]}')
num1 = 7
num2 = 0
print(f'Multiplication is {num1 * num2}')
# print(f'Division {num1 / num2}') # Error : division by zero
print('python Current Version is 3.13'.upper())
print(f'Addition is {numbers[0] + numbers[-1]}')
print('last line')

# conditional statements

################ if statement #########################
# example -1
a = 10
b = 20

if (a > b):
    print('hello')
    print('hello world')
    print('hello python')

# example -2
msg = "Hi"
if msg == "Hello":
    print("Greeted")

print("next lines")
print(10 + 20)

############## if else ######################
#  example -1
x = 10
y = 6

if (x > y and x > 40):  # True
    print('hello world')
    print('2023')
    print('python learning')
else:  # False
    print('hello world java')

# example-2
age = int(input('Enter an age: ')) # reading integer value from keyword

if age >= 18:
    print('Major')
else:
    print('Minor')

# example-3
if "a" > "A":
    print("Hello")
else:
    print("Bye")

# example-4
num = 10

if num % 2 == 0:
    print("EVEN")
    print("BLOCK")
else:
    print("ODD")
    print("BLOCK")

# example-5 - Even Odd
n = int(input("enter the n value:"))

if n % 2 == 0:
    print(f"{n} is even number")
else:
    print(f"{n} is odd number")

# example-6
if not True:
    print("Hello")
else:
    print("Bye")

# example-7
if type("10") is int:
    print("True")
    print("True Block")
else:
    print("False")
    print("False block")

# example-8
if 'apple' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')

else:
    print("Not Present")

print('After conditional')
