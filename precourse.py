# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.

import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return x**2
def f_2(x):
    return x**3
def f_3(x):
    return x**3 + 5*x

def d_f(x):
     return x*2
def d_f_2(x):
     return 3*(x**2)
#this one is a little bit trickier. Not really :)
def d_f_3(x):
     return 3*(x**2)+5

# vector_sum
def vector_sum(x1,x2):
	return np.add(x1,x2)
# vector_less
def vector_less(x1,x2):
	return np.subtract(x1,x2)
# vector_magnitude
def vector_magnitude(x):
	#I'm assuming it takes an array non explicitly
	#this one is the trickiest of the lot, there has to be a better/more elegant way to solve it
	#return math.sqrt(sum(i**2 for i in x)) is the same as elevating to 1/2 so:
	return (sum(i**2 for i in x))**0.5
	#I Still have the feeling that there should be a better way
# vec5
def vec5():
	return np.array([1, 1, 1, 1, 1])
# vec3
def vec3():
	return np.array([0, 0, 0])
# vec2_1
def vec2_1():
	return np.array([1, 0])
# vec2_2
def vec2_2():
	return np.array([0, 1])
# matrix_multiply
# Finally, the last of your precourse python examples. Write a matrix multiplication function that multiplies a 2 element vector by a 2x2 matrix matrix_multiply(vec,matrix)

def matrix_multiply(vec,matrix):
	return np.dot(vec, matrix)

