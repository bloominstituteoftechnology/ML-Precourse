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

def f_2(x):
    return x**3

def f_3(x):
    return (f_2(x)+5*x)

# Derivative functions
# d_f returns the derivative of f
def d_f(x):
    return 2*x
# d_f_2 returns the derivative of f_2
def d_f_2(x):
    return 3*(x**2)

# d_f_3 returns the derivative of f_3
def d_f_3(x):
    return (d_f_2(x)+5)

# Sum of two vectors x and y
def vector_sum(x, y):
    v = []

    for i in range(len(x)):
        v.append(x[i] + y[i])

    return v

# Difference of two vectors x and y
def vector_less(x, y):
    v = []

    for i in range(len(x)):
        v.append(x[i] - y[i])

    return v

# Magnitude of a vector
def vector_magnitude(v):

    sum = 0

    for i in v:
        sum = sum + i**2

    return int(sum ** (1/2))

import numpy as np

def vec5():
    return np.array([1,1,1,1,1])

def vec3():
    return np.array([0,0,0])

def vec2_1():
    return np.array([1,0])

def vec2_2():
    return np.array([0,1])

# Matrix multiplication function that multiplies a 2 element vector by a 2x2 matrix
def matrix_multiply(vec,matrix):
    result = [0,0]

    for i in range(2):
        for j in range(2):
            result[i] = result[i]+matrix[i][j]*vec[i]

    return result

def matrix_multiply_simplified(vec,matrix):
    result = [0,0]

    result[0] = (matrix[0][0]*vec[0]+matrix[0][1]*vec[1])
    result[1] = (matrix[1][0]*vec[0]+matrix[1][1]*vec[1])

    return result

