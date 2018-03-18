# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
import numpy as np
import sympy as sp
def f(x):
    return x**2

def f_2(x):
    return x**3

def f_3(x):
    return x**3 + 5*x


def d_f(x):
    return sp.diff(x**2, x)

def d_f_2(x):
    return sp.diff(x**3, x)

def d_f_3(x):
    return sp.diff(x**4, x)

def vector_sum(x,y):

    return np.array(x) + np.array(y)

def vector_less(x,y):
    return np.array(x) - np.array(y)

def vector_magnitude(x):
    return np.linalg.norm(x)

def vec5():
    return np.ones((1,5),dtype=int)

def vec3():
    return np.zeros((1,3),dtype=int)

def vec2_1():
    return np.array((1,0),dtype=int)

def vec2_2():
    return np.array((0,1),dtype=int)

def matrix_multiply(x, y):
    return np.dot(x,y)
