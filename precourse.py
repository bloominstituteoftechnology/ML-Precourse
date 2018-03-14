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

import numpy as np

## Calculus

# Remaining 2 of 3 functions, defined.
def f_2(x):
    return x**3

def f_3(x):
    return x**3 + 5*x

# Derivatives of said functions
def d_f(x):
    return 2*x

def d_f_2(x):
    return 3*x**2

def d_f_3(x):
    return 3*x**2 + 5

## Linear Algebra

# Vectors

def vector_sum(x,y):
    return np.add(x,y)

def vector_less(x,y):
    return np.subtract(x,y)

def vector_magnitude(x):
    return np.linalg.norm(x)

def vec5():
    return np.ones(5)

def vec3():
    return np.zeros(3)

def vec2_1():
    return np.array([1,0])

def vec2_2():
    return np.array([0,1])

# Matrix

def matrix_multiply(v,m):
        return np.dot(v,m)
