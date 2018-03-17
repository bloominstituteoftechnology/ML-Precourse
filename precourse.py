import numpy as np
import math


f = np.poly1d([1, 0, 0])
f_2 = np.poly1d([1, 0, 0, 0])
f_3 = np.poly1d([1, 0, 5, 0])


def f(x):
    return f

def f_2(x):
    return f_2

def f_3(x):
    return f_3

def d_f(x):
    return f.deriv(1)

def d_f_2(x):
    return f_2.deriv(1)

def d_f_3(x):
    return f_3.deriv(1)


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