"""

RANGE BASED for loop
###################################################
    we have control on index locations
    maily used to change the data at locations
    customized output
    range(start,stop,step)
    we can apply on list , tuple ,str [indexed data types]

"""

list_data = ["Python", "Fee", "Dollars", True, 10.28989, 10, 10 + 2j, "java", "india"]
n = len(list_data)

# print(list_data[0])
# # print(list_data[n])
# print(list_data[n-1])

# example-1 : print all element
for i in range(0, len(list_data), 1):
    print(f'[{i}] -> {list_data[i]}')

print('******************************')

# example-2: print string elements
for i in range(0, len(list_data), 1):
    if type(list_data[i]) is str:
        print(list_data[i])

print('******************************')

print(list_data)

# example-3 : change only even index locations with "even" data
for i in range(0, len(list_data), 1):
    if i % 2 == 0:
        list_data[i] = "even" # updating the index data

print(list_data)
print('******************************')

# example-4
comp = ["Google", "Microsoft", True, 1729, 10e10, 5 + 2j]

for i in range(len(comp)):  # 0-5
    if (i > 2):
        print(comp[i])
    else:
        print(f"{i} is less than given condition")

print('******************************')

# example-5
comp = ["Google", "Microsoft", True, 1729, 10e10, 5 + 2j]

print(comp)
loc = int(input("Enter the loc: "))
inp_dt = input("Enter the data to input: ")

for i in range(len(comp)):
    if (i == loc):
        comp[i] = inp_dt

print(comp)

print('********************************************')

# example-6, print index no if key presents inside list, otherwise print -1 : [Linear Search ]
nums = [10,1,3,6,77,99,22,6,30,96]
key = int(input('enter key: '))
data_loc = -1
for i in range(0, len(nums),1):
    if nums[i] == key:
        data_loc = i

print(data_loc)
