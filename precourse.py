# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###
# Qiping Sun

## Calculus
# Please define three functions with the names 'f', 'f_2', and 'f_3'.
# These functions should respectively return the following values: `x^2`, `x^3`, and `x^3 + 5x`.
import numpy as np


def f(x):
    return x ** 2


def f_2(x):
    return x ** 3


def f_3(x):
    return x ** 3 + 5 * x


# Define three additional functions `d_f`, `d_f_2`, and `d_f_3`.
# These functions should respectively return the derivative of their associated functions above:
# `d_f` returns the derivative of f, `d_f_2` returns the derivative of `f_2`, and `d_f_3` returns the derivative of `f_3`.

def d_f(x):
    return 2 * x


def d_f_2(x):
    return 3 * (x ** 2)


def d_f_3(x):
    return (3 * (x ** 2)) + 5


### Linear Algebra
# Define functions that perform basic vector arithmetic operations:

def vector_sum(x,y):
    return np.add(x,y)

def vector_less(x,y):
    return np.subtract(x,y)

def vector_magnitude(z):
    return np.linalg.norm(z)

# Using numpy's `array` object, define functions `vec5`, `vec3`, `vec2_1`, and `vec2_2` that respectively return
def vec5():
    return np.ones(5)

def vec3():
    return np.zeros(3)

def vec2_1():
    return np.array([1,0])

def vec2_2():
    return np.array([0,1])

# Finally, the last of your precourse python examples.
# Write a matrix multiplication function that multiplies a 2 element vector by a 2x2 matrix `matrix_multiply(vec,matrix)`

def matrix_multiply(vec,matrix):
    return np.matmul(vec,matrix)


