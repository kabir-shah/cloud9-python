import numpy as np

x = np.array([1, 2, 3], dtype=float)
a = np.random.randn(3)
b = np.random.randn(3)
o = np.array([2, 6, 12])

for i in xrange(1500):
	y = np.multiply(x, a) + b
	e = o - y
	a -= 0.01 * -2.0 * x * (o - np.multiply(x, a) - b)
	b -= 0.01 * -2.0 * (o - np.multiply(x, a) - b)
	print(e.sum())
	print(y)
	
print(np.multiply(np.array([4, 5, 6], dtype=float), a) + b)