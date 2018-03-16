# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
import math, numpy

def f(x):
  return x**2

def f_2(x):
  return x**3

def f_3(x):
  return x**3 + 5*x

def d_f(x):
  return 2*x

def d_f_2(x):
  return 3*x**2

def d_f_3(x):
  return 3*x**2 + 5

def vector_sum(v1, v2):
  output = []
  for i in range(len(v1)):
    output.append(v1[i]+v2[i])
  return output

def vector_less(v1, v2):
  output = []
  for i in range(len(v1)):
    output.append(v1[i]-v2[i])
  return output

def vector_magnitude(v):
  output = 0
  for i in range(len(v)):
    output += v[i]**2
  return math.sqrt(output)

def vec5():
  return numpy.ones((5), dtype=int)

def vec3():
  return numpy.zeros((3), dtype=int)
def vec2_1():
  return numpy.array([1,0])
def vec2_2():
  return numpy.array([0,1])

def matrix_multiply(vec, matrix):
  output = numpy.array(numpy.zeros(len(vec)))
  for i in range(len(vec)):
    for j in range(len(matrix)):
      output[i] += matrix[i][j] * vec[i]
  return output


