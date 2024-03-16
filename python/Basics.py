# a = "strings can be in either double quotes or single quotes"

# # taking input in python
# # input() function takes everything as string
# a = input() # this takes a line as input, we need to split it on the basis of spaces using split function
# a = a.split(' ')
# print(a)

# # to take a list of integers a liput
# a = list(map(int, input().split()))
# print(a)
# # or
# a = [int(x) for x in input().split()]
# print(a)

# # if we do not provide '.' in a number then it'll be considered as integer or it'll considered as a floating point number
# # by default result of a division comes in decimal
# a = 5 / 2 # we can reassign variables with different data types
# print(a)
# print(type(a))  # type function is used to get the type  of the variable
# a = 5
# print(type(a))

# # dictionaries in python
# # the key inside the a dictionary should always be a immutable and unique, a list cannot be used as key
# # dictionaries in python is sorted
# # keys in a dictionary can be of different data types
# # variables can be used as keys
# age = 20
# a = {'name' : "eklavya", age : "is a number" }
# print(a)
# print(a['name'], a[20])
# print(a.items()) # .items() gives the list of items
# print(a.keys()) # .keys() gives the list of keys()
# print(a.values()) # .values() gives the list of values

# # tuples in python
# # tuples are like list in python, the only difference between tuple and list is that tuples are immutable (the value at a index cannot be changed)
# a = ("eklavya", 20, "IITR")
# print(a[0], a[1], a[2])

# sets in python
#declaration:
a = set()
a.add(1)  # add method is used to insert a element to the set
a.add(2)
a.add(2)
print(a)
a.remove(2)  # to remove an element from set
print(a)
print(len(a)) # to find the length of the set
print(1 in a) # to check the existence of the element in the set
# another declaration method
a = {1, 2, 3, 4}
b = a   # doesn't copy a to b, rather a and b are made same
b.add(5)
print(a, b)  # changing a changes b as well
b = a.copy()  # now both a and b are different sets
b.add(6)
print(a, b)
a.clear()  # method to empty the set
print(a)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))   # finding the union of two sets
print(a.intersection(b))  # finding intersection of two sets
print(a.difference(b))  # subtracting b from a
print(a.isdisjoint(b))  # if intersection is null then it returns true
print(a.issubset(b))  # if a is contained in b then it returns true
print(a.issuperset(b)) # if b is contained in a then it returns true

# boolean has capital first character of True and False
# in python 'and' is used instead of && and 'or' is used instead of ||

# in python elese if is written as 'elif'
if (3 == 2):
	print(3)
elif 4 == 4:
	print(4)
else:
	print(6)


# format of for loop in python
	# for iterable_item in iterable:
# here condition is not checked after for
for i in range(10):
	print(i, end = " ")  # end can be used to print whatever we want at the end of the line, by default it's '\n'
print()

# iterating a dictionary in python
a = {"hello" : 20 , "ok" : 70, "god" : 40}
for key, value  in a.items(): 
	print(key, value)

for key in a:
	print(key)

for value in a.values():
	print(value)

# while loop format:
	# while condition:
x = 0;
while (x < 5):
	print(x)
	x += 1