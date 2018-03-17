# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
from numpy import array, sqrt
from functools import reduce

def f(x):
  return x ** 2


def f_2(x):
  return x ** 3


def f_3(x):
  return f_2(x) + (5 * x)


def d_f(x):
  return 2 * x


def d_f_2(x):
  return 3 * (x ** 2)


def d_f_3(x):
  return d_f_2(x) + 5

'''
  Converts numbers into a vector and makes vectors
  lengths match by padding shortest with 0. In the case
  where a vector is a number, vector will be filled with
  the given number so that the length matches that of the
  other vector.

  fix_vectors([1,1,1], 2)
    -> [[1,1,1], [2,2,2]]

  fix_vectors([1], [2,2,2])
    -> [[1,0,0], [2,2,2]]

  fix_vectors(1, 2)
    -> [[1], [2]]
'''
def fix_vectors(*vectors):
  longest = 1
  foundVector = False
  fixedVectors = []

  for vector in vectors:
    if type(vector) == type([]) or type(vector) == type(0):
      foundVector = True
    if type(vector) == type([]) and len(vector) > longest:
      longest = len(vector)

  if foundVector != True:
    raise ArithmeticError('You must provide at least one vector')

  for vector in vectors:
    if type(vector) == type(0):
      vector = [vector] * longest

    diff = len(vector) - longest
    if diff < 0:
      vector = vector + [0] * abs(diff)

    fixedVectors.append(vector)

  return fixedVectors


def vector_sum(*vectors):
  return [sum(vs) for vs in zip(*fix_vectors(*vectors))]


def vector_less(*vectors):
  return [reduce((lambda x, y: x - y), vs) for vs in zip(*fix_vectors(*vectors))]


def vector_multiply(*vectors):
  return [reduce((lambda x, y: x * y), vs) for vs in zip(*fix_vectors(*vectors))]


def vector_divide(*vectors):
  return [reduce((lambda x, y: x / y), vs) for vs in zip(*fix_vectors(*vectors))]


def vector_adjust_center(*vectors):
  vectors = fix_vectors(*vectors)
  total = vector_sum(*vectors) # add all the vectors
  average = list(map((lambda x: x / len(vectors)), total)) # divide by number of vectors
  return list(map((lambda vector: vector_less(vector, average)), vectors)) # subtract average from each vector


def vector_magnitude(vector):
  return sqrt(reduce((lambda x, y: x + y**2), *fix_vectors(vector), 0))


def vec5():
  return array([1] * 5)


def vec3():
  return array([0] * 3)


def vec2_1():
  return array([1, 0])


def vec2_2():
  return array([0, 1])


def matrix_multiply(vector, matrix):
  return vector_sum(*[vector_multiply(vector, row) for row in matrix])
