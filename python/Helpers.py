for i in range(-10, 10, 2):   # range function has three parameters start, end + 1, step size
	print(i)

for i in enumerate(range(10)): # enumerate function makes a list ot tuple containing (index position, item)
	print(i)

a = [1, 2, 3, 4, 5]
b = ["eklavya", "kumar", "singh", "pratap"]
c = [3400, 528, 936]
for i in zip(a, b, c):  # zip function returns a tuple of the every next item from all the iterables passed in, it continues till the shortest length among all the iterables
	print(i)


# pass statement doesn't do anything
# break statement breaks out of the loop
# continue continues the loop

# min and max functions
a = [23, 34, 233]
print(min(a), max(a))
print(min(23, 34, 56), max(23, 23, 45))

# random library

import random

print(random.randint(1, 10)) # gives a random integer from the specified range, here 10 is inclusive
print(random.random()) # gives a random number from 0 to 1
a = [2, 3, 8, 4, 0];
print(random.choice(a)) # chooses an item from the list
random.shuffle(a) # shuffles the list a
print(a)

from collections import Counter  # counter basically returns a list which count value of each element in a list or string, the returned object looks like dictionary
a = 'aaaabbbbccccc'
b = Counter(a)
print(b)
print(list(b)) # prints all the unique values
a = [1, 2, 3, 3, 4, 4, 4, 9, 0, 0]
b = Counter(a)
print(b)


print(pow(2, 4))    # gives the power of 2 to 4
a = pow(2, 3, int(1E9+7))    # gives the power of 2 to 3 mod 1E9 + 7
print(a)

a = 1.751929482298923
print(round(a))  # rounds the number upto 0 decimal places
print(round(a, 6))  # rounds the number upto 6 decimal places