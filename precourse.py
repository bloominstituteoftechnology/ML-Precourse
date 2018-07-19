# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py.
# Write the rest, defined in README.md, here, and execute python test.py
# to test. Passing this precourse work will greatly increase your odds of
# acceptance into the program.


import numpy as np


def f(x):
    return x ** 2


def f_2(x):
    return x ** 3


def f_3(x):
    return x ** 3 + 5 * x


def d_f(x):
    return 2 * x


def d_f_2(x):
    return 3 * x ** 2


def d_f_3(x):
    return 3 * x ** 2 + 5


vector_sum = np.add


vector_less = np.subtract


def vector_magnitude(x):
    return np.sqrt(np.sum(np.power(x, 2)))


def vec5():
    return np.ones(5, dtype=int)


def vec3():
    return np.zeros(3, dtype=int)


def vec2_1():
    return np.eye(1, 2, dtype=int).ravel()


def vec2_2():
    return np.eye(1, 2, k=1, dtype=int).ravel()


def matrix_multiply(vec, matrix):
    return np.dot(matrix, vec)
