import numpy as np

def f(x):
    return x**2
def f_2(x):
    return x**3
def f_3(x):
    return x**3 + (5*x);
def d_f(x):
    return 2*x
def d_f_2(x):
    return 3*x**2
def d_f_3(x):
    return 3*x**2 + 5
def vector_sum(x,y):
     v = np.add(x,y)
     return v
def vector_less(x,y):
     v = np.subtract(x,y)
     return v
def vector_magnitude(x):
    return np.linalg.norm(x)
def vec5(myList = [1,1,1,1,1]):
    return np.array(myList)
def vec3(myList = [0,0,0]):
    return np.array(myList)
def vec2_1(myList = [1,0]):
    return np.array(myList)
def vec2_2(myList = [0,1]):
    return np.array(myList)
def matrix_multiply(a,b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a,b)
