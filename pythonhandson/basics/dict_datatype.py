"""
Dictionary
    - Based on key:value
    - Keys should be immutable and unique
        :: Immutable
                - str
                - tuple
                - int , float , complex , boolean
    - Indexing is based on Keys
    ##methods
        - keys()
        - values()
        - items()
        - pop()
        - popitem()
        - update()
        - get()

    syntax:
        varName = {
            k1:v1,
            k2:v2,
            ...
            ...

            kn:vn
            }


methods
--------------------
- keys()
- values()
- get()
- update()
- items()
- pop()
- popitem()


# NOTE:
    - U can't access invalid key --> Key Error.
    - U can't pop on invalid key --> Key Error.
    - U can't pop on empty dictionary
    - When you try to update invalid key --> it will create a new entry(k,v)
"""

student = {
    'name': 'kumar',
    'college': 'UCM',
    'fee': 20.7,
    'gpa': 4.2,
    'skills': ['c', 'python', 'aws'],
    'college': 'NGIT'
}

print(student, type(student))

# demo = {
#     'name' : 'venkat',
#     10 : 'int',
#     10.5: 'float',
#     ('age'): 20,
#     1+2j : 'complex',
#     True: 'boolean'
# }
#
# print(demo, type(demo))

# key based indexing
print(student['name'])
print(student['skills'])
print(student['college'])

# update
student['name'] = 'venkat'
print(student)

# print(type( {} ))
# print(dir( {} ))

# 1. keys() : print all keys
print(student.keys())

# 2. values() : print all values
print(student.values())

# 3. items() : print list of key value pairs in tuple format
print(student.items())

# 4. get() : to get value of a specified key, throws None, if key doesn't exist
print(student.get('name'))

# indexing using [] : it will throw KeyError, if key doesn't exist
print(student['name'])

# pop() : removes the specified key from dictionary and returns corresponding value

popped_value = student.pop('college')
print(student, popped_value)

# popitem() : removes latest/last key-value pair
popped_item = student.popitem()
print(student, popped_item)

student.popitem()
print(student)

# update()
student.update({'fee': 30.7})
print(student)

# EXAMPLE

data = {
        "isbn": "123-456-222",
        "author":
            {
                "lastname": "Doe",
                "firstname": "Jane"
            },
        "editor":
            {
                "lastname": "Smith",
                "firstname": "Jane"
            },
        "title": "The Ultimate Database Study Guide",
        "category": ["Non-Fiction", "Technology"]
        }
