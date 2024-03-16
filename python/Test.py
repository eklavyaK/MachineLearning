import numpy as np

a = np.array([1, 2, 3, 4])
def sigmoid(z):
	g = 1 / (1 + np.exp(-z))
	return g

print(a)
a = sigmoid(a)