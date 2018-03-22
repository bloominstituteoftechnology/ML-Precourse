# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
import numpy as np

def f(x):
    return x**2

def f_2(x):
    return x**3

def f_3(x):
    return x**3 + 5

def d_f(x):
    return 2 * x

def d_f_2(x):
    return 3 * (x ** 2)

def d_f_3(x):
    return 3 * (x ** 2)

def vector_sum(x, y):
    xx = np.array(x)
    yy = np.array(y)
    return xx + yy

def vector_less(x, y):
    xx = np.array(x)
    yy = np.array(y)
    return xx - yy

def vector_magnitude(x):
    xx = np.array(x)
    return np.linalg.norm(xx)

def vec5(x = 5):
    return np.ones(x)

def vec3(x=3):
    return np.zeros(x)

def vec2_1():
    return np.array([1,0])


def vec2_2():
    return np.array([0,1])

def matrix_multiply(x,y):
    xx = np.array(x)
    yy = np.array(y)
    return np.dot(xx,yy)


