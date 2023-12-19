"""
DATATYPES: defines type of data stored in variable

- In python we have
primitive data types
    - integers
    - floating
    - strings
    - booleans
    - complex
    - None

 Sequence/collection
    - list []
    - tuple ()
    - set {}
    - dict {}

"""

# name = "Chitra"
# age = 25
# college_name = "NJIT"
# gpa = 3.5
# skills = ["c", "aws", "python"]
# is_student = True
#
# #  type(variable_name/value) --> displays variable values  data type
#
# print(type(name))
# print(type(age))
# print(type(college_name))
# print(type(gpa))
#
# print(type(skills))
# print(type(is_student))
#
# name = 200
# print(type(name))
#
# # id(variable_name) --> display memory address
#
# print(id(name))
# print(id(gpa))
# print(id(skills))
#
# print(True, type(True))


####################### Integers [0-9] positive and negative ###################################

# int_var1 = -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#
# print(int_var1, type(int_var1))
#
# int_var2 = 1029
# print(int_var2, type(int_var2))
#
# # Binary representation # BASE 2
# bin_var1 = 0b101 #5
# bin_var2 = 0b100 #4
#
# print(bin_var1, bin_var2)
# print(bin_var1 + bin_var2)
#
# # Octal representation # BASE 8
# oct_var1 = 0o10
# print(oct_var1)
#
# # Hexa Decimal  # BASE 16 [0-9] [A-F]
# hex_var1 = 0xA
# hex_var2 = 0xB
# print(hex_var1, hex_var2) # 10, 11
# print(hex_var1 + hex_var2)

############### FLOAT #########################################
# float_var1 = 3.14
# print(float_var1, type(float_var1))
#
# float_var2 = 1.0
# print(float_var2, type(float_var2))
#
# print(type(float(1)))
#
# float_var3 = 3.4 * (10**5)
# print(float_var3, type(float_var3))
#
# float_var4 = 3.4e5 # 10^5
# print(float_var4, type(float_var4))
#
# float_var5 = 1.5e-10  # 1.5 *(10**-10)
# print(float_var5, type(float_var5))


############## Strings ###################
"""
Collections of characters(alpha + numbers + symbols)
3 notations
    single quote 
    double quote 
    triple quote  : multi line strings
"""

str_var1 = 'A'
print(str_var1, type(str_var1))

str_var2 = "My name is Kumar"
print(str_var2, type(str_var2))

str_var3 ="It's a good movie"
print(str_var3, type(str_var3))

str_var4 = """Its "good" book"""
print(str_var4, type(str_var4))

str_var5 = 'It\'s a good show'
print(str_var5, type(str_var5))

str_var6 = "Today class is \"datatypes\""
print(str_var6, type(str_var6))


multi_str = """
Python is HighLevel Lang and
Python is intereprted language
"""
print(multi_str, type(multi_str))

multi_str1 = '''
line1 
line2
line3
'''
print(multi_str1, type(multi_str1))

############# complex numbers ##############################
# - real+imagj
# - real number is optional
# - imag number is mandatory


comp_var1 = 1 + 2j
print(comp_var1, type(comp_var1))

comp_var2 = 5j # 0 + 5j
print(comp_var2, type(comp_var2))

print(comp_var1 + comp_var2)

## BOOLEANS  ##############
# True - 1
# False  - 0
#  T , F must be uppercase

is_student = True
is_employee = False

print(is_employee, type(is_employee))
print(is_student, type(is_student))

bool_var1 = True
bool_var2 = False
print(bool_var1 * bool_var2)
