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

def d_f(x):
    return 2*x

def f_2(x):
    return x**3

def d_f_2(x):
    return 3*(x**2)

def f_3(x):
    return x**3 + 5*x

def d_f_3(x):
    return 3*(x**2) + 5

def vector_sum(x,y):
    output = []
    # check for conformability
    if (len(x) != len(y)):
        return("Vectors are not conformable...exiting")
    for i in range(0,len(x)):
        output.append(x[i] + y[i])
    return(output)
        
def vector_less(x,y):
    output = []
    # check for conformability
    if (len(x) != len(y)):
        return("Vectors are not conformable...exiting")
    for i in range(0,len(x)):
        output.append(x[i] - y[i])
    return(output)

def vector_magnitude(x):
    summand = 0
    for i in range(0,len(x)):
        summand += x[i]**2
    return((summand)**.5)

import numpy as np

def vec5():
    return(np.array([1,1,1,1,1]))

def vec3():
    return(np.array([0,0,0]))

def vec2_1():
    return(np.array([1,0]))

def vec2_2():
    return(np.array([0,1]))

def matrix_multiply(vec,matrix):
    vm0 = vec[0]*matrix[0][0] + vec[0]*matrix[1][0]
    vm1 = vec[1]*matrix[0][1] + vec[1]*matrix[1][1]
    return(np.array([vm0,vm1]))