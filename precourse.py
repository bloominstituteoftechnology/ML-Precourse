#!/Users/Admin/.virtualenvs/precourse/bin/python
from math import sqrt
from numpy import array
"""d/d(f(x)) == exponent_from_f(x) * x^(exponent_from_f(x)-1) +  c ; where c is the constant from f(x)"""
"""vect_mag == sqrt(sum(members**2))"""
"""matrix_mult == sum(product members)"""


def f(x):
    return x**2


def f_2(x):
    return x**3


def f_3(x):
    return x**3 + x * 5


def d_f(x):
    return 2*x


def d_f_2(x):
    return 3*x**2


def d_f_3(x):
    return 3*x**2 + 5


def vector_sum(x, y):
    return [a+b for a, b in zip(x, y)]


def vector_less(x, y):
    return [a-b for a, b in zip(x, y)]


def vector_magnitude(x):
    return sqrt(sum([x[0]**2, x[1]**2]))


def vec5():
    return array([1, 1, 1, 1, 1])


def vec3():
    return array([0, 0, 0])


def vec2_1():
    return array([1, 0])


def vec2_2():
    return array([0, 1])


def matrix_multiply(y, x):
    if isinstance(x[0], list):
        x, y = y, x
    return sum([array(x)*array(i) for i in y])
