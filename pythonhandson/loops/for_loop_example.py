'''

for i in range/sequence:
    statement 1
    statement 2
    statement n
'''

# without loop

# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")

# example-1
# for i in range(100):
#     print("hello world")

# example-2
# for i in range(10):
#     print(i,end = " ")

# example-3
# for i in range(1,10,1):
#     print(f'Number: {i}')

# example-4
# for num in range(10):
#     if num%2 == 1:
#         print(num)

# example-5
# for num in range(10):
#     print(num, num**2)

# example-6
# for i in range(5):
#     print(f'Hello {i}')
#     print(f'Bye {i}')

# for loop with list,tuple,string
numbers = [100, 10, 200, 20, 30, 300, 700, 800]
# print(numbers)

# without looop
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])
# print(numbers[5])

# with loop
# for i in range(0,len(numbers),1):
#     print(numbers[i])


# example-7 - print only multiples of 3
# data = [10,3,7,6,12,18,15,20]
# for i in range(0,len(data), 1):
#     if data[i]%3 == 0:
#         print(data[i])


# print-base for loops
'''
- Mainly used for printing & filtering purpose
- Don't have access to the index locations.
- Can be used on ALL-TYPES : List,Tuple , Set , Str , Dictionary
'''

# with list
marks = [3, 0, 9, 6, 15, 25]

# for num in marks:
#     print(num)

# for num in marks:
#     if num%5 == 0:
#         print(num)

# with tuple

planets = ('Earth', 'Mars', 'Mercury', 'Pluto', 'Jupiter', 'Venus')
# for p in planets:
#     if p.startswith("M"):
#         print(p)

# for p in planets:
#     if len(p)<5:
#         print(p)


# with set

colors = {"red", "blue", "black", "red", "yellow"}

# for c in colors:
#     print(c)

# with dictionary
person = {
    'name': 'chitra',
    'course': 'devops',
    'fee': 1445242.2,
    'habits': ['chess', 'drawing']
}

# print(person)

# example-1
# for p in person:  # iterate only keys
#     print(p,person[p])

# example-2
# for p in person:  # iterate only keys
#     print(p,person.get(p))

# example-3
# for ele in person.values():
#     print(ele)

# example-4
# for ele in person.keys():
#     print(ele)

# example-5
# for k,v in person.items():
#     print(k)


# with string
# str
name = "Kumar Rajamoni"

# for ch in name:
#     print(ch)

for ch in name:
    if ch.isupper():
        print(ch)