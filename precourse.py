# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here,
# and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance
# into the program.
import math
import numpy as np


def f(x):
    return x**2


def f_2(x):
    return x**3


def f_3(x):
    return (x**3) + (5*x)


def d_f(x):
    return 2*x


def d_f_2(x):
    return 3*(x**2)


def d_f_3(x):
    return 3*(x**2) + 5


# for all values of x, return x + y
def vector_sum(x, y):
    for num in range(len(x)):
        return [x[num] + y[num]]


#  for all values of x, return x - y
def vector_less(x, y):
    for num in range(len(x)):
        return [x[num] - y[num]]


def vector_magnitude(v):
    sqvector = 0
    for vector in v:
        sqvector += vector**2
    return math.sqrt(sqvector)


def vec5():
    return np.array([1, 1, 1, 1, 1])


def vec3():
    return np.array([0, 0, 0])


def vec2_1():
    return np.array([1, 0])


def vec2_2():
    return np.array([0, 1])


def matrix_multiply(vec, matrix):
    return np.dot(vec, matrix)
