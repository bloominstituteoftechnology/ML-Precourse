# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.

#Calculus Functions
import numpy as np

def f(x):
    return x**2

def f_2(x):
    return x**3

def f_3(x):
    return x**3 + 5*x

def d_f(x):
    return 2*X

def d_f_2(x):
    return 3*(x**2)

def d_f_3(x):
    return (3*(X**2)) + 5

#Linear Algebra Functions

# x = [0,1,2]
# y = [2,3,6]

def vector_sum(x, y):
    return [x[i]+y[i] for i in range(len(x))]

# print(vector_sum(x,y))

def vector_less(x, y):
    return [x[i]-y[i] for i in range(len(x))]

# print(vector_less([1], [1]))

def vector_magnitude(v):
    magSq = 0
    for i in v:
        magSq += i**2
    return magSq**0.5

# print(vector_magnitude([63,16]))

def vec5():
    return np.array([1,1,1,1,1])

# print(vec5())

def vec3():
    return np.array([0,0,0])

# print(vec3())

def vec2_1():
    return np.array([1,0])

# print(vec2_1())

def vec2_2():
    return np.array([0,1])

# print(vec2_2())

def matrix_multiply(vec, matrix):
    return [sum([vec[i]*matrix[j][i] for i in range(len(vec))]) for j in range(len(matrix))]

# v = [2,3]
# m = [[1,2], [3,4]]
#
# print(matrix_multiply(v,m))
