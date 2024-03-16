a = ["ok", 1, 3, 3]    # a list can contain elements of different data types

# sorting a list
# the list above cannot be sorted because comparision between string and int is not possible
a = [1, 2, 3, 4, 10, 8, 7]
a.sort()
print("sorted", a)

# custom sorting

a.sort(key = lambda x : -x) # for reverse sorting

k = [("what", 3), ("is", 23), ("your", 90), ("name", 80)]
k.sort(key = lambda x : (x[0], -x[1])) # this sorts on the basis of the first element then second element in decreasing order
print(k)

# custom lists of list sorting
# when two lists are compared the following rules are applied : first each element of the list is compared successively and at the point of the first different the comparision operator is applied, if in case shorter list is prefix of the longer list then it is considered as lesser
k = [[1, 1, 3], [2, 0], [0, 3, 2, 5], [-1, 100], [23], [8, 0], [1, 0, 3]]
k.sort(key = lambda x : [x[0]])
print("sorted", k)
# we can also write lambda elsewhere
func = lambda x : -x
a = [2, 4, 3, 5]
a.sort(key = func)
print(a)

# checking the length of a list
print(len(a))

# list concatnation
b = [3, 4, 5]
c = b + a
print(c)

# appending to list
a.append(100)
print(a)

# removing last element
a.pop()
print(a)

# reversing a list
a.reverse()
print(a)

# copying a list
a = [1, 2] 
b = a     # it doesn't copy a to b rather a and b are same, changes in one is reflected in another
b.append(3)
print(a, b)
b = a.copy() # this creates another independent copy of a
b.append(4)
print(a, b)


# extending a list
a = [1, 2, 3]
b = [4, 5, 6]
a.append(b) # it makes b list as element of the list
print(a) 
a.extend(b) # it concatanates a to b
print(a)
a = a + b
print(a) # this is the same as above


# counting
print(a.count(4)) # prints the number of occurances of 4 in list a


# removing
a.remove(4) # removes the first occurance of 4 in list a
print(a)