# Free Example
def f(x):
    return x**2

# Imports

import numpy as nmp
import math

# LinAlgeCalc

""" calculate x**3 """

def f_2(x):
	return x**3

""" calculate x**3+5x """

def f_3(x):
	return x**3 + 5*x

""" calculate derivatives of f,f_2,f_3 """

def df(x):
	return 2*x

def df_2(x):
	return 3*(x**2)

def df_3(x):
	return 3*(x**2) + 5

# Vectors

""" calculate sum of vectors """

def vector_sum(x,y):
	#[x[0] + y[0]]
	return [nmp.add(x,y) for (x,y) in zip(x,y)]

""" calculate diff. of vectors """

def vector_less(x,y):
	#[x[0] - y[0]]
	return [nmp.subtract(x,y) for (x,y) in zip(x,y)]

""" calculate magn. of vectors """

def vector_magnitude(v):
	#(v[x]**2 + v[x]**2)**0.5
	return nmp.linalg.norm(v)

# Arrays

""" generate vectors using an array of 5 1s """

def vec5():
	#nmp.array([1,1,1,1,1])
	return nmp.ones(5)

""" generate vectors using an array of 3 0s """

def vec3():
	#nmp.array([0,0,0])
	return nmp.zeros(3)

""" generate vectors using an array of 1,0 """

def vec2_1():
	return nmp.array([1,0])

""" generate vectors using an array of 0,1 """

def vec2_2():
	return nmp.array([0,1])

# Matrixes

""" multiply a 2x2 matrix with a elem. vector of 2 """

def matrix_multiply(v,m):
	return nmp.dot(v,m)


# Reference

"""

v_1 \times m_{1,1} + v_2 \times m_{1,2}
\\ v_1 \times m_{2,1} + v_2 \times m_{2,2} 

"""
