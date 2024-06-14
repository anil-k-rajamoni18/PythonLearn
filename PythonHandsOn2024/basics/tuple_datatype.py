"""
TUPLE:
--------------------------
- It's also collections and sequence & ordered data types
- stores multiple items in a single variable.
- declared with (ele1,ele2 ,ele3...)
- INDEXING
    - +VE : 0 - N-1
    - -VE : -1 - -N
- Immutable(insertion,deletion,updation) : changes not allowed at indexing levels

METHODS
--------------

"""

planets = ('Earth', "Venus", 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury')  # planets

print(planets, len(planets), type(planets))

# access 3rd planet name
print(planets[2])

# change 4th index name to Pluto
# planets[4] = 'Pluto'  # Error

# METHODS

# print(dir( () )) # display all methods & attribute of a data type

# 1. count()
print(planets.count('Earth'))
print(planets.count('Pluto'))

# 2. index()
print(planets.index('Mars'))
# print(planets.index('venus')) # throws ValueError, if value doesn't exists


# Tricky questions
a = 10, 20.5, 'Chitra'  # assigning more than one element with comma, separated will act a tuple type
print(a, type(a))

# tuple unpacking
a, b, c = (10, 20, 30)
print(a, b, c)
