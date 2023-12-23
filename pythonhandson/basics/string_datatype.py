"""
STRING
- group of individual or collections of characters[alpha + numeric + special symbols]

- strings are immutable in python

- Strings have indexing

    +ve : 0 -> N-1

    -ve : -1 --> -N
- String supports slicing also.

- In Python Strings can be declared in 3 ways:

  - single quotes  'k'
  - double quotes   "dyamic programmic"
  - triple quotes (mainly used for multi-line strings)

>Text is a string data type. Any data type written as text is a string. Any data under single, double or triple quote are strings. There are different string methods and built-in functions to deal with string data types

String Methods
==================
regular methods:

    capitalize()
    count()
    endswith()
    startswith()
    expandtabs()
    find()
    rfind()
    index()
    rindex()
    title()
    replace()
    upper()
    lower()

checking methods:
----------------------
    isalnum()
    isalpha()
    isdecimal()
    isdigit()
    isnumeric()
    isidentifier()
    islower()
    isupper()

conversation methods
------------------------
    split() : str --> list
    join() : list --> str
"""

letter = 'A'
name = "Kumar"
topic_name = """
Today we are discussing String overview and 
String methods
"""

print(letter)
print(name)
print(topic_name)

str_var1 = "It's a good movie"
str_var2 = 'Today topic is "operators" '

str_var3 = """
Python is interpreted and oops language
Python is '''dynamic'''' lang
Python is scripting and functional lang
"""

print(str_var1)
print(str_var2)
print(str_var3)

# METHODS
challenge = 'thirty days of python'

# len()
print(len(challenge))

# 1.capitalize()
print(challenge.capitalize())

# 2.count()
print(challenge.count('y'))
print(challenge.count('y', 3, 10))
print(challenge.count('Y'))

# 3. startswith() & 4.endswith()
print(challenge.startswith('th'))
print(challenge.startswith('YOU'))

print(challenge.endswith('yon'))
print(challenge.endswith('thon'))

# 5. find() & 6. rfind() : returns -1 on failure
print('******* find & rfind methods ************')
team_name = 'mumbai indians'
print(team_name.find('a'))  # lowest index
print(team_name.find('i'))
print(team_name.find('M'))

print(team_name.rfind('a'))  # highest index
print(team_name.rfind('i'))
print(team_name.rfind('n'))
print(team_name.rfind('I'))

# 7. index & 8.rindex() : returns ValueError on failure.

print('******* index & rindex methods ************')
print(team_name.index('a'))  # lowest index
print(team_name.index('i'))

# print(team_name.index('M'))  # error


print(team_name.rindex('a'))  # highest index
print(team_name.rindex('i'))
print(team_name.rindex('n'))

# print(team_name.rindex('N')) # Error


# 9. title() & 10.casefold() & 11.swapcase()
print('******** title & casefold & swapcase methods ***********')

python_topic = 'today TOPIC is functions in PYTHON'
print(python_topic.title())
print(python_topic.casefold())  # smaller case

day10_topic = 'pYthon conDitionAL statemENTS topiC'
print(day10_topic.swapcase())  # upper case <--> lowercase


# 12.replace() & 13.lower() & 14.upper()
print('******** replace , uppercase , lowercase methods ***********')

chatgpt = 'chatGPT is developed using LLM model Turbo GPT 3.5 engine'
print(chatgpt.lower()) # converts entire string into lowercase
print(chatgpt.upper()) # converts entire string into uppercase

print(chatgpt.replace('3.5', '4.5'))

print('************ checking methods ************')
password = 'Kumar@1234'
name = 'kumar'

# 1.isalnum()
print('****** isalnum() **********')
print(name.isalnum())
print(password.isalnum())

print('A0017234FGT'.isalnum())
print('9982726'.isalnum())
print('computer science'.isalnum())  # space is special character

# 2. isalpha()

print('****** isalpha() **********')

print("kumar123".isalpha())
print("python".isalpha())
print('rocket science'.isalpha())

# 3. isdecimal()
print('123'.isdecimal())
print('0.6'.isdecimal())


# 4. isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)

print('*********** isdigit() ***********')

challenge = 'Thirty'
print(challenge.isdigit()) # False

challenge = '30'
print(challenge.isdigit())   # True

challenge = '\u00B2'
print(challenge.isdigit())   # True

# 5.isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)

print('*********** isnumeric() ***********')

num = '10'
print(num.isnumeric()) # True

num = '\u00BD' # ½
print(num.isnumeric()) # True

num = '10.5'
print(num.isnumeric()) # False


# 6. isidentifier() :  Checks for a valid identifier - it checks if a string is a valid variable name

print('*********** isidentifier() ***********')

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number

challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

print('student-name'.isidentifier())


# islower() & isupper()
print('******* islower & isupper *********')

print("hello".islower())
print("Hello".islower())
print("HELLO".islower())

print("Hi".isupper())
print("HI".isupper())


# split() & join()

print('************ split() method : str --> list ********')

challenge = 'python is dynamic lang'

split_output = challenge.split() # str - list , #default sep is space
print(split_output, type(split_output))

challenge = 'chatgpt,is,developed,using,LLTM,3.5,model'
print(challenge.split(','))


print('************ join() method : list --> str ********')

list_words = ['python', 'is', 'dynamic', 'language']  # str
one_line = "".join(list_words)
print(one_line, type(one_line))

print(" ".join(list_words))
print("->".join(list_words))


# EXAMPLE
'''
1. read list of integers from keyword 
2. calculate sum & average 

Input:
    10 20 30 
    sum: 60 
    average: 2
'''


# String Indexing
print('*************** Indexing ****************')

challenge = 'Java is Robust'
print(len(challenge))

# Positive Indexing
print(challenge[0])
print(challenge[3])
print(challenge[8])
# print(challenge[20])

# Negative Indexing
print(challenge[-1])
print(challenge[-4])
print(challenge[ -len(challenge)])

# SLICING [start:stop:step]
'''
- Extracting specific data.
syntax:
    [start:stop:step]
    
positive
- start : 0 (default)
- stop : LEN-1
- step : 1 

negative:
 -start : -1 (default)
- stop : -(LEN)
- step : - 1 


note: STOP is exclusive not included

- > next index = current + step 
-> current index < stop 
'''

print('*************** slicing *************')
challenge = 'CurrentVersionOfPythonIs3.12'
print(len(challenge))

print(challenge[0:4:1]) # Curr
print(challenge[2:10:2])
print(challenge[0:28:5])

challenge = "HelloWorld"
print(len(challenge))
print(challenge[0:6:3])
print(challenge[0:10:2])

print(challenge[0:5]) # [0:5:1]

print(challenge[:3]) # [0:3:1]

print(challenge[2:]) # [2: LEN-1: 1]


# Negative Indexing
challenge = "HiPython"
print(len(challenge))
print(challenge[-1: -5:-1])
print(challenge[-5:-10:-2])

var= "James Bond"
print(var[2::-1])

print(challenge[-1:-6:1])


# "Chennai Super Kings"

name = "MumbaiIndians"

print(len(name))
print(name[0])
print(name[-1])
print(name[0:4:1])
print(name[:6]) # [0:6:1]
print(name[2:]) #[2:LEN:1]
print(name[-1:-5:-2])
print(name[::2]) #[0:LEN-1:2]
print(name[-1 : -len(name)-1 : -1]) #[-1: -LEN-1: -1]
print(name[::-1])  #[-1: -LEN-1: -1] # reverse order
print(name[::]) #[0: LEN-1: 1]
