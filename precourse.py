# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

import numpy as np

# calc
def f(x):
    return x**2

def f_2(x):
    return x**3

def f_3(x):
    return x**3 + 5*x

# derivatives
def d_f(x):
    return 2*x

def d_f_2(x):
    return 3*x**2

def d_f_3(x):
    return 3*x**2 + 5

# lin algebra
def vector_sum(x, y):
    return np.add(x, y)

def vector_less(x, y):
    return np.subtract(x, y)

def vector_magnitude(x):
    return np.linalg.norm(x)

def vec5():
    return np.ones(5)

def vec3():
    return np.zeros(3)

def vec2_1():
    return np.identity(2)[:,0]

def vec2_2():
    return np.identity(2)[:,1]

def matrix_multiply(a, b):
    return np.dot(a, b)