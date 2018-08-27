import numpy as np

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
  return x**3 + 5*x

def d_f():
  return x

def d_f_2():
  return 2*x**2

def d_f_3():
  return 2*x**2 + 5

def vector_sum(p1, p2):
  if len(p1) != len(p2):
    raise ValueError('Inputs does not have the same shape.')
  result = []
  for i in range(0, len(p1)):
    result.append(p1[i] + p2[i])
  return result

def vector_less(p1, p2):
  if len(p1) != len(p2):
    raise ValueError('Inputs does not have the same shape.')
  result = []
  for i in range(0, len(p1)):
    result.append(p1[i] - p2[i])
  return result

def vector_magnitude(p1):
  (x, y) = p1
  return (x**2+y**2)**(1/2)

def vec5():
  return np.array([1, 1, 1, 1, 1])

def vec3():
  return np.array([0, 0, 0])

def vec2_1():
  return np.array([1, 0])

def vec2_2():
  return np.array([0, 1])

def matrix_multiply(vec, matrix):
  result = []
  for i in range(0, len(matrix)):
    if (len(vec) != len(matrix[i])):
      raise ValueError('Vector - Matrix shape is invalid.')
    ops = []
    for j in range(0, len(vec)):
      ops.append(vec[j]*matrix[i][j])
    result.append(sum(ops))

  return result
