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
  return x**3

def f_3(x):
  return (x**3 + 5*x)

def d_f(x):
  return 2*x

def d_f_2(x):
  return 3*x**2

def d_f_3(x):
  return 3*x**2 + 5


# Linear Algebra

def vector_sum(x,y):
  x = np.array(x)
  y = np.array(y)
  return x + y

def vector_less(x,y):
  x = np.array(x)
  y = np.array(y)
  return x - y

def vector_magnitude(x):
  import math
  x = np.array(x)
  return math.sqrt(x[0]**2 + x[1]**2)
  
def vec5():
  return np.array([1,1,1,1,1])

def vec3():
  return np.array([0,0,0])

def vec2_1():
  return np.array([1,0])

def vec2_2():
  return np.array([0,1])

def matrix_multiply(vec,matrix):
  v0 = vec[0] * matrix[0][0] + vec[1] * matrix[0][1]
  v1 = vec[0] * matrix[1][0] + vec[1] * matrix[1][1]
  return [v0, v1]
  
  
  


  






