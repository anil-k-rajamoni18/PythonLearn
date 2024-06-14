# TYPE CASTING : converting one datatype to another data type
# methods
"""

- Converting one data type to another data type. - We use int(), float(), str(), list(), set()
- When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error.
- If we concatenate a number with a string, the number should be first converted to a string.

    - int() :
    - float()
    - str()
    - bool()
    - complex()
"""

# int() :  string["0-9"],float,boolean --> int

# Example-1

str_num = "10"
var1 = int(str_num)  # string to integer

print(str_num, type(str_num))
print(var1, type(var1))

# Example-2
float_num = 3.14
var2 = int(float_num)  # float to integer

print(float_num, type(float_num))
print(var2, type(var2))

# Example-3
bool_num = True
var3 = int(bool_num)  # bool to integer

print(bool_num, type(bool_num))
print(var3, type(var3))

# Errors while converting when data is incompatible
roll_no = "150017A2023"
# print(int(roll_no))


# float() :  string,int,boolean --> float

# Example-1
iphone_13_price = "63500.25"
var5 = float(iphone_13_price) # str -> float

print(iphone_13_price, type(iphone_13_price))
print(var5, type(var5))

#  Example-2
area_of_triangle = 25
var6 = int(area_of_triangle) # int - float

print(area_of_triangle, type(area_of_triangle))
print(var6, type(var6))

# Example-3
is_cricket_player = False
var7 = float(is_cricket_player)

print(is_cricket_player, type(is_cricket_player))
print(var7, type(var7))

# Errors while converting when data is incompatible
ist_time = '7.42am'
# print(float_num(ist_time))


# str() : int, float, bool, complex,None --> string
student_age = 25
var8 = str(student_age)

student_fee = 34000.21122
var9 = str(student_fee)

is_student = True
var10 = str(is_student)

complex_var = 1+2j
var11 = str(complex_var)

print(var8, type(var8))
print(var9, type(var9))
print(var10, type(var10))
print(var11, type(var11))

#  want to store student names , of 500 students  -- 500 variables

st1_name = 'chitra'
st2_name = 'kumar'
st3_name = 'venkat'

print(st3_name)

student_names_lst = ['chitra', 'kumar', 'venkat', 'lasya', 'anusha', True, 10, 3.14, 10+2j, None]

print(student_names_lst[2])

