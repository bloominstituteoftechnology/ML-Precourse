# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

from numpy.polynomial import Polynomial
import numpy as np
import math

c = [1, 0, 0]
f = Polynomial(c)

d = [1, 0, 0, 0]
f_2 =  Polynomial(d)

e = [1, 0, 5, 0]
f_3 =  Polynomial(e)

def f(x):
    return x ** 2

def f_2(x):
    return x ** 3

def f_3(x):
    return x ** 3 + 5 * x

def d_f(x):
    d_f = f.deriv()
    #d_f = 2*x
    return d_f(x)

def d_f_2(x):
    d_f_2 = f_2.deriv()
    #d_f_2 = 3 * x ** 2
    return d_f_2(x)

def d_f_3(x):
    d_f_3 = f_3.deriv()
    #d_f_2 = 3*x**2 + 5
    return d_f_3(x)


def vector_sum(x,y):
    return np.add(x,y)

def vector_less(x,y):
    return np.subtract(x,y)

def vector_magnitude(x):
    return math.sqrt(sum(np.square(x)))


def vec5():
    return np.array([1, 1, 1, 1, 1])

def vec3():
    return np.array([0, 0, 0])

def vec2_1():
    return np.array([1, 0])

def vec2_2():
    return np.array([0, 1])
    
def matrix_multiply(vec, matrix):
    return np.dot(vec, matrix)
