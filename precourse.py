# Machine Learning/Data Science Precourse Work
import numpy as np
# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
def f(x):
    return x**2

def f_2(x):
	return x**3

def f_3(x):
	return f_2(x) + 5*x

def d_f(x):
	return 2*x

def d_f_2(x):
	return 3*(x**2)

def d_f_3(x):
	return d_f_2(x) + 5

def vector_sum(x, y):
	return np.add(x, y)

def vector_less(x, y):
	return np.subtract(x,y)

def vector_magnitude(x):
	return np.sqrt(np.array(x).dot(np.array(x)))

def vec5():
	return np.array([1,1,1,1,1])

def vec3():
	return np.array([0,0,0])

def vec2_1():
	return np.array([1,0])

def vec2_2():
	return np.array([0,1])

def matrix_multiply(vec, matrix):
	return np.array(vec).dot(matrix)