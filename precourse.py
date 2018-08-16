# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.

# precourse.py - Adam Anderson - completed 04/16/18

import numpy as np
import math
from random import randint

# hardcoded methods for f, f_2, f_3, d_f, d_f_2, d_f_3

# x = 2
# exp1 = 2
# exp2 = 3
# exp3 = 3
# f3_mult = 5

# def f(x):
#     return x**exp1
# print("f = ", f(x))

# def f_2(x):
#     return x**exp2
# print("f_2 = ", f_2(x))

# def f_3(x):
#     return x**exp3 + f3_mult*x
# print("f_3 = ", f_3(x))

# def d_f(x):
#     return exp1*x**(exp1-1)
# print("d_f = ", d_f(x))

# def d_f_2(x):
#     return exp2*x**(exp2-1)
# print("d_f_2 = ", d_f_2(x))

# def d_f_3(x):
#     return exp3*x**(exp3-1) + f3_mult*x
# print("d_f_3 = ", d_f_3(x))

# plain methods for functions and derivatives

def f(x):
    return x**2

# print(f(x))

def f_2(x):
    return x**3

# print(f_2(x))

def f_3(x):
    return x**3 + 5*x

# print(f_3(x))

def d_f(x):
    return 2*x**(2-1)

# print(d_f(x))

def d_f_2(x):
    return 3*x**(3-1)

# print(d_f_2(x))

# test should test for 5*n, but tests for 5 instead

def d_f_3(x):
    return 3*x**(3-1) + 5

# print(d_f_3(x))

# vector operations, tested with random vectors:

# def rand_vector():
#     return np.random.randint(0, 9, (1, 3))

# x = rand_vector()
# y = rand_vector()
# print("x = ", x)
# print("y = ", y)

def vector_sum(x,y):
    return np.array(x) + np.array(y)

# print("v_sum = ", vector_sum(x,y))

def vector_less(x,y):
    return np.array(x) - np.array(y)

# print("v_less = ", vector_less(x,y))

# my method for magnitude, with value of [4,3], should return 7, no?
# test expects 5 instead

# def vector_magnitude(x):
#     return math.sqrt(np.array(x).sum()**2)
# print("v_mag = ", vector_magnitude(x))

# others' method for magnitude, which seems inconsistent:

def vector_magnitude(x):
    return np.linalg.norm(x)

# print("v_mag2 = ", vector_magnitude2(x))

# matrix + vector operations

def vec5():
    return np.array([1,1,1,1,1])

# print("vec5 = ", vec5())

def vec3():
    return np.array([0,0,0])

# print("vec3 = ", vec3())

def vec2_1():
    return np.array([1,0])

# print("vec2_1 = ", vec2_1())

def vec2_2():
    return np.array([0,1])

# print("vec2_2 = ", vec2_2())

# static vector
# def vec():
#     return np.array([4,3])
# vec = vec()
# print("vec = \n", vec)

# static matrix

# def matrix():
#     return np.matrix('3 0; 0 2')

# matrix = matrix()

# print("matrix = \n", matrix)

# first method

def matrix_multiply(vec, matrix):
    vec = np.array(vec)
    matrix = np.array(matrix)
    return np.inner(vec, matrix)

# print("first method = \n", matrix_multiply(a,b))

# second method:
# def matrix_multiply2(vec, matrix):
#     vec = np.array(vec)
#     matrix = np.array(matrix)
#     return np.dot(vec, matrix)
# print("second method = \n", matrix_multiply2(vec,matrix))
