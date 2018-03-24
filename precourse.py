# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 00:06:39 2018

@author: Juan
"""

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
    return (x**3)+(5*x)
    
def d_f(x):
    return 2*x
    
def d_f_2(x):
    return 3*(x**2)
    
def d_f_3(x):
    return (3*(x**2))+5

def vector_sum(x,y):
    if len(x)==len(y):
       z=[0]  
       for i in range (0,len(x)-1):
           z=z+[0] 
       for i in range(0,len(x)):    
            z[i]=x[i]+y[i]
       return z
    else:
        print('error, vectors not of equal dimension')

def vector_less(x,y):
     if len(x)==len(y):
       z=[0]  
       for i in range (0,len(x)-1):
           z=z+[0] 
       for i in range(0,len(x)):    
            z[i]=x[i]-y[i]
       return z
     else:
        print('error, vectors not of equal dimension')
        
def vector_magnitude(x):
    x_2=0    
    for i in range(0,len(x)):
        x_2=x_2+x[i]**2
    return x_2**.5

def vec5():
    return np.array([1,1,1,1,1])

def vec3():
    return np.array([0,0,0])

def vec2_1():
    return np.array([1,0])

def vec2_2():
    return np.array([0,1])

def matrix_multiply(vec,matrix):
    mv=[0,0]
    mv=[(vec[0]*matrix[0][0])+(vec[1]*matrix[0][1]),(vec[0]*matrix[1][0])+(vec[1]*matrix[1][1])]   
    return mv
