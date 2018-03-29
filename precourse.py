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
import matplotlib.pyplot as pyplot

## d(f(x)) is f(x**n) = n * x**(n-1)
## function of x^2
def f(x):
    return (x**2)

## function of x^3
def f_2(x):
    return (x**3)

## function of x^3 + 5x
def f_3(x):
    return (x**3 + (5*x))

## derivative of f
def d_f(x):
    return (2*x)

## derivative of f_2
def d_f_2(x):
    return (3*(x**2))

## derivative of f_3
def d_f_3(x):
    return (3*(x**2) + 5)
 
## the sum of vectors 'x' and 'y' is another vector 'v'
## vector_sum = (x_i + y_i)
def vector_sum(x,y):
    return np.add(x,y)

## the difference of two vectors is another vector 'v'
## vector_less = (x_i - y_i)
def vector_less(x,y):
    return np.subtract(x,y)

## the magnitude of a vector, its length, is
## absolute value of v is equal to the square root of the summation between 'i' and 'n' 
## in the formula 'v' sub 'i' squared [(v_i)**2)]
def vector_magnitude(x):
    return np.linalg.norm(x)

## arrays

def vec5():
    return np.array([1,1,1,1,1])

def vec3():
    return np.array([0,0,0])

def vec2_1():
    return np.array([1,0])

def vec2_2():
    return np.array([0,1])

## matrix multiplication function that multiplies 
## a two element vector by a 2x2 matrix

def matrix_multiply(vec,matrix):
    return np.inner(vec,matrix)
