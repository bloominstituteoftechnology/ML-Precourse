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
    return (x**3) + (5*x)

def d_f(x):
    return 2*x

def d_f_2(x):
    return 3*(x**2)

def d_f_3(x):
    return 3*(x**2) + (5*x)

def vector_sum(x, y):
    # for all values of x, return x + y
    for num in range(len(x)):
        return [x[num] + y[num]]

def vector_less(x, y):
    #  for all values of x, return x - y
    for num in range(len(x)):
        return [x[num] - y[num]]
