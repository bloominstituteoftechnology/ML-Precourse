# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
import math
import numpy as np

def derivative(func, x):
    epsilon = math.e**-18
    return round((func(x+epsilon)-func(x))/epsilon, 3)

def f(x):
    return x**2

def f_2(x):
    return x**3

def f_3(x):
    return x**3 + 5*x

def d_f(x):
    return derivative(f, x)

def d_f_2(x):
    return derivative(f_2, x)

def d_f_3(x):
    return derivative(f_3, x)

print(d_f_2(5))
def vector_sum(vectA, vectB):
    vectorAdd = []
    if(len(vectA) == len(vectB)):
        for x,y in zip(vectA, vectB):
            vectorAdd.append(x+y)
    return vectorAdd

def vector_less(vectA, vectB):
    vectorSub = []
    if(len(vectA) == len(vectB)):
        for x,y in zip(vectA, vectB):
            vectorSub.append(x-y)

    return vectorSub

def vector_magnitude(vectA):
    squaredAddition = 0
    for x in vectA:
        squaredAddition = squaredAddition + x**2

    return math.sqrt(squaredAddition)

def vec3():
    return np.zeros(3)

def vec5():
    return np.ones(5)

def vec2_1():
    return np.identity(2)[0]

def vec2_2():
    return np.identity(2)[1]

def matrix_multiply(matrixA, matrixB):
    try:
        matrixAColNos = np.shape(matrixA)[0]
    except IndexError as e:
        matrixAColNos = 1
    try:
        matrixBrowNos = np.shape(matrixB)[1]
    except Exception as e:
        matrixBrowNos = 1

    if (matrixAColNos == matrixBrowNos):
        return np.dot(matrixA, matrixB)
    else:
        raise Exception('The dot multiplication is not possible in this case')

