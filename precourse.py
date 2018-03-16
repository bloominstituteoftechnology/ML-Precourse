# Kurt Van Etten

# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
def f(x):
    return x**2


# define a function to calculate x^3
def f_2(x):
    return x**3

# define a function to calculate x^3 + 5x
def f_3(x):
    return x**3 + (5 * x)


# define functions to calculate the derivatives of f, f_2 and f_3
def d_f(x):
    return 2 * x

def d_f_2(x):
    return 3 * x**2

def d_f_3(x):
    return (3 * x**2) + 5


# define functions to calculate the sum, difference, and magnitude of vectors
# (Note: we will use a list to represent a vector)
def vector_sum(v1, v2):
    return [x + y for (x, y) in zip(v1, v2)]

def vector_less(v1, v2):
    return [x - y for (x, y) in zip(v1, v2)]

def vector_magnitude(v):
    import math
    return math.sqrt(sum([x*x for x in v]))


# use numpy's array object to define functions to generate some vectors
import numpy as np

def vec5():
    return np.array([1, 1, 1, 1, 1])

def vec3():
    return np.array([0, 0, 0])

def vec2_1():
    return np.array([1, 0])

def vec2_2():
    return np.array([0, 1])


# define a function to multiply a 2x2 matrix times a 2-vector
# hmmm, the vector is the first parameter, that could be confusing!
# wasn't clear if this should be in plain python or numpy

# plain python version:

def matrix_multiply(vector, matrix):
    return [sum([r * v for (r, v) in zip(row, vector)]) for row in matrix]


# numpy version:
'''
def matrix_multiply(v, m):
    np_v = np.array(v)
    np_m = np.array(m)
    return np_m.dot(np_v)
'''
