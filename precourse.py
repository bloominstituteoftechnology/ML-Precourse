# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.

# Moohan Lee

import numpy as np


def f(x):
    return x ** 2


def f_2(x):
    return x ** 3


def f_3(x):
    return x ** 3 + 5 * x


h = 1e-5


def d_f(x):
    return (f(x + h) - f(x - h)) / (2 * h)
    # return return 2*x


def d_f_2(x):
    return (f_2(x + h) - f_2(x - h)) / (2 * h)
    # return return 3*(x**2)


def d_f_3(x):
    return (f_3(x + h) - f_3(x - h)) / (2 * h)
    # return return 3*(x**2) + 5


def vector_sum(x, y):
    for num in range(len(x)):
        return [x[num] + y[num]]


def vector_less(x, y):
    for i in range(len(x)):
        return [x[i] - y[i]]


def vector_magnitude(x):
    return np.linalg.norm(x)


def vec5():
    return np.ones(5)


def vec3():
    return np.zeros(3)


def vec2_1():
    return np.array([1, 0])


def vec2_2():
    return np.array([0, 1])


def matrix_multiply(vec, matrix):
    return np.dot(vec, matrix)
