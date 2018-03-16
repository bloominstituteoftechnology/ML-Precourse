"""
Created for LambdaSchool Machine Learning
Precourse Assignment
By: Jason Sigfred Seril
"""
import numpy as np

"""
Calculus
"""
def f(x):
    return x ** 2

def f_2(x):
    return x ** 3

def f_3(x):
    return x ** 3 + 5 * x

def d_f(x):
    return 2 * x

def d_f_2(x):
    return 3 * x ** 2

def d_f_3(x):
    return 3 * x ** 2 + 5

"""
Linear Algebra
"""
def vector_sum(x, y):
    return np.add(x, y)

def vector_less(x, y):
    return np.subtract(x, y)

def vector_magnitude(v):
    return np.linalg.norm(v)

def vec5():
    return np.ones(5)

def vec3():
    return np.zeros(3)

def vec2_1():
    return np.array([1,0])

def vec2_2():
    return np.array([0,1])

def matrix_multiply(vec, matrix):
    return np.dot(vec, matrix)
    
    



