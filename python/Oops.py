# class hello():
# 	ten = 10 # these variables can be termed static these are shared by all the objects of the class
# 	def __init__(self, a, b, c):  # init is constructor of the class, and it must have self keyword to assign the values to the members of object
# 		self.a = a
# 		self.b = b
# 		self.c = c
# 	def sum(self):     # we always use self keyword in function argument to use the members of the object, otherwise we cannot use it
# 		return self.a + self.b + self.c + self.ten
# 	def sayhello(self):
# 		print("hello")

# a = hello(1, 2, 3)
# print(a.sum())
# a.a = 10
# print(a.sum())


# a.ten = 20 # this does not modify the value of original ten variable of the class hello, rather it creates another instance of object a whose name is ten
# print(a.sum())
# # Note: this member variable is created only for a, not for all the objects of the class
# a.twelve = 101 # another example of creating another member of instance a
# print(a.twelve)

# b = hello(0, 0, 0)
# b.ten = 50
# print(b.sum())
# # note that ten member is not changed for a
# print(a.ten, b.ten)

# c = hello(0, 1, 2)
# print(c.ten) # note that c is using the ten which originally declared inside class hello as it doesn't it's personal member ten

# # to change the original value of ten we change it through the class itself
# hello.ten = 11
# print(c.ten)

# c.sayhello()

class Number():
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def add(self):
		return self.a + self.b
	
	def prod(self):
		return self.a * self.b
	
class Even(Number):
	def __init__(self, a, b):
		Number.__init__(self, a, b)   # this is important to to initilize the members of the Number class of the obj which is Even class instance
		self.c = a * 2
		self.d = b * 2
	
	def sub(self):
		return self.c - self.d
	def __str__(self):  # this is a special method like __init__, returns the string representation of the a object of the Even class
		return "it's ok"
	def __len__(self):	# this is also a special method like __init__, returns the length of the object which is upto us to return the value we want
		return 100

obj = Even(1, 2)
print(obj.add())
print(obj.prod())
print(obj.sub())

print(str(obj))
print(len(obj))  

# for multiple inheritance: class class_name(Even, Number):