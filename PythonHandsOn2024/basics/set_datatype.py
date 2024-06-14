"""
    SET
------------------------------------
 -It's Un-Ordered & Un-Indexed.
- Doesn't store the duplicates.
- declared with {}
- No Indexing because of No Ordering.
- Mutable
- prebuilt method: set()

    methods:
-------------------

'add', 'clear', 'copy', 'difference', 'difference_update',
'discard', 'intersection', 'intersection_update', 'isdisjoint',
'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
'symmetric_difference_update', 'union', 'update'

"""
# {} will act dictionary not set

print(type([]))
print(type(()))
print(type({}))
print(type(set()))
print(dir(set()))

# set of colors
colors = {'red', 'green', 'green', 'red'}
print(colors, type(colors), len(colors))

# add(object)
colors.add('brown')
colors.add('green')
print(colors, len(colors))

# pop() : removes random element if set is not empty
removed_ele = colors.pop()
print(removed_ele, colors)

# remove() : removes element from set, if element doesn't exists raise KeyError

# colors.remove("yellow")
# print(colors)

# discard(): removes element from set, if exits, otherwise doesn't throw any exception/Error
colors.discard("yellow")
print(colors)


# intersection() : prints common elements
set_a = {'iphone13', 'samsung', 'realme', 'redmi'}
set_b = {'samsung', 'redmi', 'motorla'}

print(set_a.intersection(set_b))

# union() : print all elements from both the sets, no duplicates
print(set_a.union(set_b))

# difference: print elements of the first set [doesn't include common elements]
print(set_a.difference(set_b))
print(set_b.difference(set_a))

# copy() : returns shallow copy a set
dup_set = colors.copy()
print(id(dup_set), id(colors))

# clear() : clears all elements from the set
set_a.clear()
print(set_a)


#  common use cases
numbers = [10,20,10,30,40,20] # list
print(numbers)

# list to set
numbers_set = set(numbers)
print(numbers_set, type(numbers_set))



