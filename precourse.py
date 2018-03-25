# Machine Learning/Data Science Precourse Work
import numpy as np
# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
"""
In the requirements there is a specification for a vector with the shape 5 rows, 1 column.
Without looking at how the test.py evaluates the functions it was tricky to know that 
it was required a flatten or a (5,) shap matrix. Comment for the ones of shape 5x1, zeros 3x1, vec2_1, and vec2_2.
"""

def f(x):
    return x**2
def f_2(x):
	return x**3
def f_3(x):
	return x**3+5*x
def d_f(x):
	return 2*x
def d_f_2(x):
	return 3*(x**2)
def d_f_3(x):
	return 3*(x**2)+5
def vector_sum(v1,v2):
	v12  = []
	if val_type(v1,v2)==True:
		for _ in range(0,len(v1)):
			v12.append(v1[_]+v2[_])
		return v12
def vector_less(v1,v2):
	v12  = []
	if val_type(v1,v2)==True:
		for _ in range(0,len(v1)):
			v12.append(v1[_]-v2[_])
		return v12
def val_type(v1,v2):
	valid=False
	v1t = type(v1)
	if v1t==type(v2):
		if v1t==list:
			v1l, v2l = len(v1),len(v2)
			if v1l == v2l:
				valid = True
	return valid
def vector_magnitude(v):
	s=0
	if type(v)==list:
		for _ in range(0,len(v)):
			s+=v[_]**2
		return s**0.5
def vec5(ones=5):
	return np.ones((ones))
def vec3(zeros=3):
	return np.zeros((zeros))
def vec2_1():
	return np.array([1,0])
def vec2_2():
	return np.array([0,1])
def matrix_multiply(vec,matrix,mode="hard"):
	vt = type(vec)
	if vt==type(matrix):
		if mode=="hard":
			if vt==list:
				vl = len(vec)
				ml = len(matrix)
				if ml>0:
					ml0 = matrix[0]
					if type(ml0) == list:
						ml0l = len(ml0)
						if ml0l == vl:
							"""
							Only multiply if the number of columns of the matrix
							equals the number of rows of the vector
							"""
							if str(vec[0]).isnumeric():
								output=[]
								for _ in range(0,ml):
									s=0
									for __ in range(0,vl):
										s+=vec[__]*matrix[_][__]
									output.append(s)
								return output
		elif mode=='easy':
			if vt==list:
				vecn = np.asarray(vec)
				mn = np.asarray(matrix)
				vm = np.dot(vecn,mn)
				return vm
