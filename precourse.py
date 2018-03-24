# Matthew Tomas
# github: DreamsOfBunnies

# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.

import numpy as np

# Calculus Tests:

# x^2
def f(x):
    return x**2

# x^3
def f_2(x):
    return x**3

# x^3 + 5x
def f_3(x):
    return x**3 + 5*x

# dy/dx (x^2)
def d_f(func, x):
    return 2*x

# dy/dx (x^3)
def d_f_2(x):
    return 3*x**2

# dy/dx (x^3 + 5x)
def d_f_3(x):
    return 3*x**2 + 5

# Linear Algebra Tests:

# vector addition: x sub i + y sub i
def vector_sum(x, y):
    return np.add(x, y)

# vector subtraction: x sub i - y sub i
def vector_less(x,y):
    return np.subtract(x, y)

# vector magnitude calculation: sqrt of the sum of (v sub i) sq from i to n
def vector_magnitude(v):
    return np.linalg.norm(v)

# create a vector filled with 5 '1's 
def vec5():
    return np.array([1, 1, 1, 1, 1])
    # could also np.ones(5, dtype=int) to fill vector with just 1's

# create a vector filled with 3 '0's
def vec3():
    return np.array([0,0,0])
    # could also use np.zeros(3, dtype=int) to fill vector with just 0's

# create a vector of 2 rows 1 wide where row 1 is 1 and row 2 is 0
def vec2_1():
    return np.array([1,0])

# create a vector of 2 rows 1 wide where row 1 is 0 and row 2 is 1
def vec2_2():
    return np.array([0,1])

# multiply a 2 element vector by a 2x2 matrix, LaTeX below
def matrix_multiply(vec, matrix):
    return np.dot(vec, matrix)

# Mv =

# \begin{pmatrix}
# m_{1,1} \  m_{1,2}
# \\ m_{2,1} \  m_{2,2}
# \end{pmatrix}

# \begin{pmatrix}
# v_1
# \\ v_2
# \end{pmatrix}

# =

# \begin{pmatrix}
# v_1 \times m_{1,1} + v_2 \times m_{1,2}
# \\ v_1 \times m_{2,1} + v_2 \times m_{2,2}
# \end{pmatrix}

# https://latex.codecogs.com/gif.latex?%5Clarge%20Mv%20%3D%20%5Cbegin%7Bpmatrix%7D%20m_%7B1%2C1%7D%20%5C%20m_%7B1%2C2%7D%20%5C%5C%20m_%7B2%2C1%7D%20%5C%20m_%7B2%2C2%7D%20%5Cend%7Bpmatrix%7D%20%5Cbegin%7Bpmatrix%7D%20v_1%20%5C%5C%20v_2%20%5Cend%7Bpmatrix%7D%20%3D%20%5Cbegin%7Bpmatrix%7D%20v_1%20%5Ctimes%20m_%7B1%2C1%7D%20&plus;%20v_2%20%5Ctimes%20m_%7B1%2C2%7D%20%5C%5C%20v_1%20%5Ctimes%20m_%7B2%2C1%7D%20&plus;%20v_2%20%5Ctimes%20m_%7B2%2C2%7D%20%5Cend%7Bpmatrix%7D
