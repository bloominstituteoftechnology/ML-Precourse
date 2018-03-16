# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.

# Calculus
def f(x):
    return x**2

def f_2(x):
	return f(x) * x

def f_3(x):
	return f_2(x) + 5*x

def d_f(f):		
	return 2*x

def d_f_2(f_2):	
	return 3*f(x)

def d_f_3(f_3):
  	return d_f_2(x) + 5	

# Linear Algebra
def vector_sum(a,b):
	total_vector = []
	if len(a) == len(b):
		vector_length = len(a)
	for i in range(0, vector_length):
		total_vector.append(a[i] + b[i])
	return total_vector
	
def vector_less(a,b):
	diff_vector = []
	if len(a) == len(b):
		vector_length = len(a)
	for i in range(0, vector_length):
		diff_vector.append(a[i] - b[i])
	return diff_vector	

def vector_magnitude(a):
	total = 0
	for i in range(0,len(a)):
		total += a[i]**2   # squares  of sigma xi
	return (total ** 0.5)  # square root of summation	


# import numpy
import numpy as np

def vec5():
	return np.array([1,1,1,1,1])	  

def vec3():
	return np.array([0,0,0])

def vec2_1():
	return np.array([1,0])

def vec2_2():
	return np.array([0,1])

def matrix_multiply(vector1, matrix):
	vector_mul1 = vector1[0] * matrix[0][0] + vector1[0] * matrix[1][0]
	vector_mul2 = vector1[1] * matrix[0][1] + vector1[1] * matrix[1][1]
	return np.array([vector_mul1,vector_mul2])



