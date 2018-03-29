# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
from scipy.misc import derivative
import numpy as np

def f(x):
    return x**2

def f_2(x):
    return x**3

def f_3(x):
    return (x**3) + (5*x)

def d_f(x):
    return derivative(f,x)

def d_f_2(x):
    return round(derivative (f_2,x,dx=1e-3))
    

def d_f_3(x):
    return round(derivative(f_3,x,dx=1e-3))
    

def vector_sum(x,y):
    x = np.array(x) 
    y = np.array(y)
    return x+y

def vector_less(x,y):
    x = np.array(x) 
    y = np.array(y)
    return x-y

def vector_magnitude(x):
    return np.linalg.norm(x)

def vec5():
    return np.array([1,1,1,1,1],dtype=int)
    
def vec3():
    return np.array([0,0,0],dtype=int)
    
def vec2_1():
    return np.array([1,0],dtype=int)

def vec2_2():
    return np.array([0,1],dtype=int)

def matrix_multiply(vec,matrix):
    return np.dot(vec, matrix)




    



