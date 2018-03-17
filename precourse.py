#Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
import numpy as np
import math

def f(x):
    return x ** 2

def f_2(x):
    return x ** 3

def f_3(x):
    return x ** 3 + 5 * x

def d_f(x):
    return 2 * x ** (2 - 1)

def d_f_2(x):
    return 3 * x ** (3 - 1)

def d_f_3(x):
    return 3 * x ** (3 - 1) + 5

def vector_sum(x, y):
    return [x[0] + y[0]]

def vector_less(x, y):
    return [x[0] - y[0]]

def vector_magnitude(vector):
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2)

def vec5():
    return np.array([1, 1, 1, 1, 1])

def vec3():
    return np.array([0, 0, 0])

def vec2_1():
    return np.array([1, 0])

def vec2_2():
    return np.array([0, 1])

def matrix_multiply(vec, matrix):
    return np.array(vec).dot(matrix)
