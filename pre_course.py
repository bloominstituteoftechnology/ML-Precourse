import math
import numpy as np




#CALCULUS

####Functions

def f(x):

    return (x ** 2)


def f_2(x):

    return (x ** 3)


def f_3(x):

    return (x ** 3)  (5 * x)


####Derivatives

def d_f(x):

    return 2 * x


def d_f_2(x):

    return 3 * (x ** 2)


def d_f_3(x):

    return 3 * (x ** 2) + 5





#LINEAR ALGEBRA

####Vector Relationshp

def vector_sum(vx, vy):

    return np.array(vx) + np.array(vy)


def vector_less(vx, vy):

    return np.array(vx) - np.array(vy)


def vector_magnitude(vec):

    return np.sum(np.array(v)**2)**0.5


def vec5():

    return np.array([1, 1, 1, 1, 1])


def vec3():
    return np.array([0, 0, 0])


def vec2_1():

    return np.array([1, 0])


def vec2_2():

    return np.array([0, 1])


def matrix_multiply(vec, matrx):

    return np.array(matrx).dot(np.array(vec))
