print("hello world"[8]) # prints the character at position 8 which is 'r'
print("hello world"[1 : 5]) # prints the substrings starting at index 1 and ending at 5 - 1
print("hello world"[0 :]) # prints whole string
print("hello world"[0 : -1]) # -1 is treated as last index so it'll print upto last second index

# String methods
a = "eklavya"
print(a + a) # string concatnation
print(a * 10) # string concatanation 10 times
# a[0] = 'b' # throws error because strings in python are immutable
b = a.upper() # these are upper and lower case conversions in python, remember that original string is still unchanged (immutable)
print(b)  
print(b.lower())

# Since strings in python are immutable we can convert the string to list and modify the list in case if we want to change a character at any position

a = list(a)
print(a)
a = ''.join(a) # to join everything present in the list
print(a)

# string sorting
a = sorted(a) # sorted function first converts the string to list then sorts it and returns a sorted list of characters, sorting is done based on the ascii value of the characters
a = ''.join(a)
print(a)

# string formatting

# .format() method
a = "my name is {} and my age is {}".format("eklavya", 23) # directly fills the elements in the provided order
print(a)
a = "my name is {1} and my age is {0}".format(23, "eklavya") # fills the elements in order of indices
print(a)
print("my name is {name} and my age is {age}".format(name = "eklavya", age = 23)) # fills the elements according to the values of the parameters
# f-strings
name = "eklavya"
age = 23
a = f"my name is {name} and my age is {age}"
print(a)



a = 'aaabbbbccccccc'
print(a.count('c')) # counts the number of occurrances of 'c'
print(a.find('b')) # returns the first index where 'b' is present
print(a.find('4')) # returns -1
print(a.endswith('cc'))  # returns true of 'cc' is suffix of a
print(a.startswith('aa')) # returns true of 'aa' is prefix of a
print('bbbb' in a)   # returns true of a contains 'bbbb' as a substring
print('bbbbbcd' in a)  