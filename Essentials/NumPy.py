import numpy as np

# np.array is a mutable container
a = np.array([1, 2, 3, 4])  # this array is a column vector
a[0] = 10 # mutable
print(a)
# appending an element
a.resize(a.size + 1)
a[-1] = 100
print(a)

# initilizing an np.array
a = np.zeros(4)
print(a)
a = np.zeros((4, 5), dtype = int)
print(a)
print(a.shape)  # shape method provides the dimensions of the matrix
print(a.dtype)  # dtype method provides the date type of the elements of the matrix

a = np.arange(10)  # provides integers ranging from 0 to 9
print(a)
a = np.random.rand(5)  # prints 5 random numbers between 0 and 1
print(a)
a = np.arange(2, 50, 3)  # here 2 is the starting point and 3 is the step size and 20 is the range limit
print(a) 

# vector slicing
print(a[5])  # prints number at index 5
print(a[:3]) # gets a new by slicing from index 0 to 3 - 1
print(a[3:]) # starts from 3 goes till end
print(a[2:5]) # starts from index 2 and goes till 4
print(a[0:-1]) # starts from index 0 and goes till second last
print(a[1:10:3]) # starts from index 1 and goes till index 8 by keep step size of 3

# simple operations on np array
print(np.sum(a))
print(np.mean(a))
print(10 * a)
print(a**2)
print(a + a)
print(a * a)
print(np.dot(a, a))  # dot function is used to calculate the dot product of two matrices


# for matrix multiplication we use operator @
b = np.array([[1, 2]])
c = np.array([[1], [2]])
print(b, c)
print(b @ c)


# reshape is popular way to create np matrices
b = np.array([1, 2, 3, 4, 5, 6]).reshape(3, 2)
print(b)

# in case of 2D matrices, each entry in list represent a row
a = np.array([[1, 32, 3, 4, 5], [1, 2, 3, 4, 5]]) 