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

def f_2(x):
	return x**3

def f_3(x):
	return (x**3 + 5*x)

def d_f(x):
	return 2*x

def d_f_2(x):
	return 3*x**2

def d_f_3(x):
	return (3*x**2 + 5)

def vector_sum(x,y):
	return [x[0]+y[0]]

def vector_less(x,y):
	return [(x[0]-y[0])]

def vector_magnitude(x):
	import math
	return math.sqrt(x[0]**2 + x[1]**2)

def vec5():
	import numpy as np
	return np.array([1,1,1,1,1])

def vec3():
	import numpy as np
	return np.array([0,0,0])

def vec2_1():
	import numpy as np
	return np.array([1,0])

def vec2_2():
	import numpy as np
	return np.array([0,1])

def matrix_multiply(vec,matrix):
	import numpy as np
	return np.dot(vec,matrix)

