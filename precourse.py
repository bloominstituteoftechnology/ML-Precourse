# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
import numpy as np
import math



def f(x):
    return x**2

def f_2(x):
    return x**3

def f_3(x):
    return (x**3 + 5*x)

def d_f(x):
    return 2*x

def d_f_2(x):
    return 3*x

def d_f_3(x):
    return (3*x + 5)

def vector_sum(x,y):
    return np.add(x,y)

def vector_less(x,y):
    return np.subtract(x,y)

def vector_magnitude(x):

    y=0

    for( number in x):

        y += number**2

    return math.sqrt(y)

def vec5():

    x = np.array(np.ones(5,1))

    return x

def vec3():

    x = np.array(np.zeros(3,1))

    return x

def vec2_1():

    x = np.array([[1],[0]])

    return x

def vec2_2():

    x = np.array([[0],[1]])

    return x

def matrix_multiply():

    x = np.array([[0],[1]])

    return x
