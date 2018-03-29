##ShaunFlynn

import numpy as np
import matplotlib.pyplot as pyplot

## d(f(x)) is f(x**n) = n * x**(n-1)
## function of x^2
def f():
    return (x**2)

## function of x^3
def f_2():
    return (x**3)

## function of x^3 + 5x
def f_3():
    return (x**3 + 5x)

## derivative of f
def d_f:
    return (2x)

## derivative of f_2
def d_f_2:
    return (3x**2)

## derivative of f_3
def d_f_3:
    return (3x**2 + 5)
 
## the sum of vectors 'x' and 'y' is another vector 'v'
## vector_sum = (x_i + y_i)
def vector_sum:
    return np.add(x,y)

## the difference of two vectors is another vector 'v'
## vector_less = (x_i - y_i)
def vector_less:
    return np.subtract(x,y)

## the magnitude of a vector, its length, is
## absolute value of v is equal to the square root of the summation between 'i' and 'n' 
## in the formula 'v' sub 'i' squared [(v_i)**2)]
def vector_magnitude(x):
    return np.linalg.norm(x)

## arrays

def vec5:
    return np.array([1,1,1,1,1])

def vec3:
    return np.array([0,0,0])

def vec2_1:
    return np.array([1,0])

def vec2_2:
    return np.array([0,1])

## matrix multiplication function that multiplies 
## a two element vector by a 2x2 matrix

def matrix_multiply(vec,matrix):
    return np.inner(vec,matrix)

## Matrix [m_0_0,m_0_1,m_0_2]
##        [m_1_0,m_1_1,m_1_2]
## Vector [v_0,v_1,v_2]
## M*v =  [(v_0 * m_0_0) + (v_1 * m_0_1) + (v_2 * m_0_2)]
##        [(v_0 * m_1_0) + (v_1 * m_1_1) + (v_2 * m_1_2)]


