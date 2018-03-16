# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Henry (Jake) Huneycutt

import numpy as np


def f(x):
    return x**2


def f_2(x):
    return x**3


def f_3(x):
    return (x**3) + (5*x)


def d_f(x):
    return 2*(x**(2-1))


def d_f_2(x):
    return 3*(x**(3-1))


# apologies for the insane long-form version
# wanted to force myself to relearn the math that I haven't done in over a decade

def d_f_3(x):
    return 3*(x**3-1) + 1*5*(x**(1-1))


def vector_sum(x,y):
    return np.add(x,y)


def vector_less(x,y):
    return np.subtract(x,y)


def vector_magnitude(x):
    return np.linalg.norm(x)


def vec5():
    return np.ones(5)


def vec3():
    return np.zeros(3)


def vec2_1():
    return np.array([1,0])


def vec2_2():
    return np.array([0,1])


def matrix_multiply(vec, matrix):
    return np.array(vec).dot(matrix)




