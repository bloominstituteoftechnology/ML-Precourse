# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###
import numpy as np
import math

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
def f(x):
    return x**2

# Compute derivative of x^2.
def df(x):
    return 2*x

# Compute x^3.
def f_2(x):
    return x**3

# Compute derivative of x^3.
def df_2(x):
    return 3*(x**2)

# Compute x^3+5x.
def f_3(x):
    return (x**3 + 5*x)

# Compute derivative of x^3+5.
def df_3(x):
    return (3*(x**2) + 5)

# Compute sum of two vectors.
def vector_sum(x,y):
    return np.add(x,y)

# Compute difference of two vectors.
def vector_less(x,y):
    return np.subtract(x,y)

# Compute magnitude of a vector.
def vector_magnitude(x):
    return math.sqrt(sum(i**2 for i in x))

def vec5():
    return np.array([1,1,1,1,1])

def vec3():
    return np.array([0,0,0])

def vec2_1():
    return np.array([1,0])

def vec2_2():
    return np.array([0,1])

def matrix_multiply(x,y):
    return np.matmul(x,y)
