# Machine Learning/Data Science Precourse Work
# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md,
# here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
import numpy as np

def f(x):
    return x**2

def f_2(x):
    return x**3

def f_3(x):
    return x**3 + 5*x

def d_f():
    return ("f")

def d_f_2():
    return ("f_2")

def d_f_3():
    return ("f_3")

def vector_sum( x, y):
    return np.add(x,y)

def vector_less( x, y):
    return np.subtract(x,y)

def vector_magnitude(x):
    return np.linalg.norm(x)
    
def vec5():
    return np.ones(5)
    
def vec3():
    return np.zeros(3)
 
def vec2_1():
    return np.array([1,0])
     
def vec2_2():
    return np.array([0,1])

def matrix_multiply(vec,matrix):
    return np.dot(vec,matrix)
