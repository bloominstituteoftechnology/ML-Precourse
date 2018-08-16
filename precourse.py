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

def d_f(x):
    return 2*x

def d_f_2(x):
    return 3*(x**2)

def d_f_3(x):
    return 3*(x**2) + 5

def vector_sum(vec1,vec2):
    return [sum(x) for x in zip(vec1,vec2)]

def vector_less(vec1,vec2):
    return [a_i - b_i for a_i,b_i in zip(vec1,vec2)]

def vector_magnitude(v):
    sum_components = 0
    for x in v:
        sum_components += x**2
    return sum_components**.5

def vec5():
    return [1,1,1,1,1]

def vec3():
    return [0,0,0]

def vec2_1():
    return [1,0]

def vec2_2():
    return [0,1]

def matrix_multiply(vec,matrix):
    result = []
    for i in range (len(matrix[0])):
        total = 0
        for j in range (len(vec)):
            total += vec[j] * matrix[j][i]
        result.append(total)
    return result
