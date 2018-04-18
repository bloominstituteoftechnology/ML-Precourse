# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
import numpy as np

def f(x):
    return x**2

def f_2(x):
    return x**3

def f_3(x):
    return x**3 + 5*x

def df(x):
    return 2*x

def df2(x):
    return 3*x

def df3(x):
    return 3*(x**2) + 5

import numpy as np


def vector_sum(x,y):
    if len(x)>len(y):
        n=len(x)
    else:
        n=len(y)
    
    vector_sum=np.array([])
    i=0
    while i<n:
        a = x[i] + y[i]
        vector_sum=np.append(a,vector_sum)
        i=i+1
    return vector_sum
       

def vector_less(x,y):
    if len(x)>len(y):
        n=len(x)
    else:
        n=len(y)
        n=len(x)
    
    v=np.array([])
    i=0
    while i<n:
        a = x[i] - y[i]
        v=np.append(a,v)
        i=i+1
    return v
  
def vector_magnitude(v):
    sum=0
    for i in range(len(v)):
        sum= sum + (v[i]**2)  
    
    mag=sum**.5
    return mag

def vec5():
    x =[1,1,1,1,1]
    return x

def vec3():
    x = [0,0,0]
    return x

def vec2_1():
    x = [1,0]
    return x

def vec2_2():
    x = [0,1]
    return x

def matrix_multiply(v,m):
    z=np.matmul(v,m)
        
    return z
