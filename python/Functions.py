# function declaration:
# def function_name(parameters):


# in python if you pass a mutable variable, it is passed by reference, i.e. it's changes reflect even after function terminates
# in case of immutable variable, the changes are lost after function ends

def change_immutable(a):
	a += 2

x = 3
change_immutable(x)
print(x)             # it prints 3 itself

def change_mutable(a):
	a.append(23)

x = [1, 2, 3]
change_mutable(x)
print(x)            # it prints the modified list


def multiple_arguments(*args):
	print(args[0], args[1], args[2])

multiple_arguments(20, "eklavya", 23.6)

def multiple_keyword_arguments(**kwargs):
	print(kwargs['name'], kwargs['age'], kwargs['dob'])

multiple_keyword_arguments(name = 'eklavya', age = 20, dob = 2003)

def func(x):
	return x * x

a = [1, 2, 3, 4]
a = list(map(func, a))  # map function applies a function to every element of the iterable
print(a)

x = 10
def check():
	x = 20
	print(x)
	def scope():
		global x  # prints 30, because global goes all the way back to global scope to fetch the variable
		print(x)
		x += 1
	scope()

check()
print(x)


if __name__ == '__main__':
	print("this file is being run directly")  # this lines executes if functions.py is run directly
else:
	print("this file is being run by being imported by another file and not being run directly") # this is run if functions.py is not being run directly but run by being imported by another file



# variable properties of a function
	
# assigning a function to a variable
def func(a, b):
	print(a + b)

func1 = func   # every properties of func is copied to func1
func1(1, 2)
del func       
func1(1, 2)   	# even after deleting func we can see func1 still runs

# passing a function as parameter and returning a function
def maths(func1):
	def add():
		func1(3, 4)
	add()
	return add

add = maths(func1)  
add()

# function decorators
def decorate(func):
	def arithmetic(a, b):
		func(a, b)
		print(a - b)
		print(a * b)
		print(a / b)
	
	return arithmetic

@decorate   # if this is on (not commented out) then arithmetic function will be executed otherwise, just func function will be executed
def func(a, b):
	print(a + b)

func(10, 15)


# how does generator (yield) works
# yield is like a iterator, when the function is called it returns the value as soon as yield is encountered, when the function is iteratred further then the function starts executing just the yield from where it has left
# but if function is called again explicitly then function is executed again

def rangge(n):
	for i in range(n):
		yield i * i

obj = rangge(10)  # creating the object of the generator
print(next(obj))  # since object is iterable we can iterate using next() function
print(next(obj)) 
print(next(obj))

for i in rangge(5):  # iterating the generator using for loop
	print(i)

# creating list of the iterable
a = list(rangge(5))
for i in a:
	print(i)

a = list(obj)
for i in a:
	print(i)