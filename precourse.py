# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

import math
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
    return 3*x**2

def d_f_3(x):
    return 3*x**2 + 5

# Note: These functions below are already implemented by numpy
# but I assume just using numpy was not the purpose of this exercise
# hence implementing them without using numpy (unless mentioned clearly in the exercise to use numpy)

# np.add(x, y)
def vector_sum(x, y):
    if (len(x) != len(y)):
        raise ValueError('adding 2 vectors of different dimensions is undefined')

    return [x[i] + y[i] for i in range(len(x))]

# np.subtract(x, y)
def vector_less(x, y):
    if (len(x) != len(y)):
        raise ValueError('subtracting 2 vectors of different dimensions is undefined')

    return [x[i] - y[i] for i in range(len(x))]

# np.linalg.norm(x)
def vector_magnitude(x):
    return math.sqrt(sum([x[i]**2 for i in range(len(x))]))

def vec5():
    return np.array([1, 1, 1, 1, 1])

def vec3():
    return np.array([0, 0, 0])

def vec2_1():
    return np.array([1, 0])

def vec2_2():
    return np.array([0, 1])

# multiplies a 2 element vector by a 2x2 matrix
# np.dot(vec, matrix) or np.matmul(vec, matrix)
def matrix_multiply(vec, matrix):
    if (len(vec) != 2 or len(matrix) != len(vec) or len(matrix[0]) != len(vec) or len(matrix[1]) != len(vec)):
        raise ValueError('please input a 2 element vector and a 2x2 matrix')

    return [sum([vec[j] * matrix[i][j] for j in range(len(vec))]) for i in range(len(matrix))]
