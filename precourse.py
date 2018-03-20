# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###
##
# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
import numpy as m
import math
def f(x):
    return x**2

def f_2(x):
        return x**3

def f_3(x):
        return x**2 + (5 * x)

def d_f(x):
        return (f(x + h) - f(x - h)) / (2 * h)

def d_f_2(x):
        return (f_2(x + h) - f_2(x - h)) / (2*h)

def d_f_3(x):
        return (f_3(x + h) - f_3(x-h)) / (2 * h)

def vector_sum(x,y):
    for i in range(len(x)):
        return [x[i] + y[i]]

def vector_less(x,y):
    for i in range(len(x)):
        return [x[i] - y[i]]

def vector_magnitude(x):
        return m.linalg.norm(x)

def vec5():
        return m.ones(5)

def vec3():
        return m.zeros(3)

def vec2_1():
        return m.array([1,0])

def vec2_2():
        return m.array([0,1])

def matrix_multiply(vec, matrix):
        return m.dot(vec, matrix)
