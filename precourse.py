import numpy as np
import math

def f(x):
    return x ** 2

def f_2(x):
    return x ** 3

def f_3(x):
    return x ** 3 + 5 * x

h = 1e-5

def d_f(x):
    return (f(x + h) - f(x - h)) / (2 * h)
# return 2 * x

def d_f_2(x):
    return (f_2(x + h) - f_2(x - h)) / (2 * h)
# return 3 * (x ** 2)

def d_f_3(x):
    return (f_3(x + h) - f_3(x - h)) / (2 * h)
# return 3 * (x ** 2) + 5


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
