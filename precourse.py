# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
import numpy as np
def f(x):
	return x**2
def f_2(x):
	return x**3
def f_3(x):
	return x**3+5*x
def d_f(x):
	return 2*x
def d_f_2(x):
	return 3*x**2
def d_f_3(x):
	return 3*x**2+5

def vector_sum(x,y):
	return np.sum([x, y], axis=0)
def vector_less(x,y):
	return np.subtract(x, y)
def vector_magnitude(x):
	return np.linalg.norm(x)
def vec5():
	return np.array([1,1,1,1,1])
def vec3():
	return np.array([0,0,0])
def vec2_1():
	return np.array([1, 0])

def vec2_2():
	return np.array([0, 1])
def matrix_multiply(x,y):
	return np.matmul(np.array(x),np.array(y))