# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

import numpy as np 

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
def f(x):
    return x**2

def f_2(x):
	return x**3

def f_3(x):
	return x**3 + 5*x

def d_f(x):
	return 2*x

def d_f_2(x):
	return 3 * x**2

def d_f_3(x):
	return (3 * x**2) + 5

def vector_sum(x, y):
	v = []
	for xi, yi in zip(x, y):
		v.append(xi + yi)
	return v

def vector_less(x, y):
	v = []
	for xi, yi in zip(x, y):
		v.append(xi-yi)
	return v

def vector_magnitude(v):
	result = 0
	for vi in v:
		result += vi**2
	return result**0.5

def vec5():
	return np.ones((5))

def vec3():
	return np.zeros((3))

def vec2_1():
	return np.array([1, 0])

def vec2_2():
	return np.array([0, 1])

def matrix_multiply(vec, matrix):
	return np.dot(matrix, vec)