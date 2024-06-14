'''
            LIST
- It's a collection & ordered & indexed data type
- It's stores multiple items in one variable
- Indexing
        positive  0 ---> N-1 [left - right]
        negative -1 ---> -N [right - left]
- It's Mutable ---> Changes are allowed
- declared with []
- stores homogeneous & hetrogenous data types


syntax:

varName = [data1,data2,....data_n]
'''

lstNumbers = [0, 1, 2, 3, 4, 5]  # all are the same data types - a list of numbers

fruits = ['Banana', 'Orange', 'Mango', 'Avocado', "grape"]  # all the same data types - a list of strings (fruits)

countries = ['Finland', 'Estonia', 'Sweden', 'Norway']  # all the same data types - a list of strings (countries)

mixedList = ['Banana', 10, False, 9.81, 1 + 2j]  # different data types in the list - string, integer, boolean and float

# print(len(fruits), len(countries), len(mixedList))
# print(lstNumbers , type(lstNumbers))

# INDEXING

# print(fruits[1], fruits[2])
# print(countries[3], countries[-1])
# print(mixedList[3], mixedList[-2])

# METHODS

"""
- insertion
     append(obj) 
     insert(index,obj)
     extend([obj1,obj2..])
- deletion
    pop(index=-1)
    remove(value)
- popular 
    reverse()
    copy()
    clear()
    sort(reverse=False)
    count()
    index()
"""
# print(dir( [] )) # print list data type methods

# 1.append(obj) : adds new element/obj to the end of the list

student_names = ['kumar']
print(student_names)

student_names.append('chitra')
# student_names.append('venkat', 'teja')
print(student_names)

# 2.insert(index,object): insert the object data at specified index location

student_names.insert(0, "lasya")
print(student_names)

student_names.insert(-1, "joyce")
print(student_names)

#  NOTE:
# insert(() , if index is invalid , +ve : add data at last, -ve: add data at first

student_names.insert(100, "john")
print(student_names)

student_names.insert(-100, "manoj")
print(student_names)

teams = ["india", "aus", "bang"]
print(teams, type(teams), len(teams))

# 3.extends([obj1, obj2, .. objn]) : add multiple data elements to the end of the list
teams.extend(["pak", "eng"])
print(teams)

# remove() & pop()
programming_langs = ['c', 'cpp', 'java', 'Mojo']

# programming_langs.append('python')
# programming_langs.insert(1,'ruby')
# programming_langs.extend(['.Net', 'Scala'])


# 4.pop(index = -1) : remove and return element at index  [ index based deletion]

print(programming_langs)

last_index_data = programming_langs.pop()  # pops last index

print(last_index_data, programming_langs)

removed_data = programming_langs.pop(2)
print(removed_data, programming_langs)

# 5.remove(value) : removes the specified element
student_names = ["kumar", "lasya", "alice", "kumar", "venkat", "chitra", "venkat"]
print(student_names)

removed_data2 = student_names.remove("kumar")
print(removed_data2, student_names)

# student_names.remove("manoj")
# print(student_names)

# 6.reverse()

# print(student_names)
# student_names.reverse()
# print(student_names)

# 7.sort(reverse = False) # ascending
# sort(reverse = True) # descending

print(student_names)
student_names.sort(reverse=True)
print(student_names)

# 8.index() : find the index of a value
print(student_names.index("venkat"))
print(student_names.index("chitra"))
# print(student_names.index("bob"))

# 9.count() : count the occurrence of a value
print(student_names.count("venkat"))
print(student_names.count("bob"))

# 10.clear() : remove all elements from list
print(student_names)
student_names.clear()
print(student_names)

# 11.copy(): creates & returns a shallow copy of the list
employee_lst = ['Ram', 'Krishna', 'Ashwani', 'Naveen']
dup_lst = employee_lst.copy()
print(employee_lst, dup_lst)
print(id(employee_lst), id(dup_lst))  # printing memory address

# changing 2nd index employee name
employee_lst[2] = 'Shruti'
print(employee_lst, dup_lst)


"""
# summary 
        insertion
    ================
        append(obj)
        insert(ind,obj)
        extend([obj1,obj2...objn])
        
            deletion
    =======================
        pop(index=-1) # if index is invalid, raises IndexError
        remove(value) # if value not exists , raises ValueError
        
            popular 
    ============================
        reverse()
        count()
        index()
        sort(reverse=False) #default is asc
        clear()
        copy()
    
    
        OBSERVATION
    =============================
    - insert() , even index is +ve/-ve invalid , we can insert the data
    - pop() default will remove last indexed element
    - we can't pop empty list
    - remove() will throw Error if element is not there
    - sort(reverse=True) : desc order.
    - copy() method , it create new variable with different memory addr.
    
        
"""