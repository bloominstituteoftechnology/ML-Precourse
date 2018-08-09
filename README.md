# DEPRECATED

The Lambda School Machine Learning Precourse work enables you to demonstrate basic understanding of Python3 programming, linear algebra, very basic calculus, and conforming to unit test requirements.

# Prereqs

You can only execute the tests in a python programming environment. Run the tests in order to determine if your solutions are correct:

    python test.py

You must add the functions described below into the file `precourse.py`.


## Calculus
Please define three functions with the names 'f', 'f_2', and 'f_3'. These functions should respectively return the following values: `x^2`, `x^3`, and `x^3 + 5x`.

Define three additional functions `d_f`, `d_f_2`, and `d_f_3`. These functions should respectively return the derivative of their associated functions above: `d_f` returns the derivative of f, `d_f_2` returns the derivative of `f_2`, and `d_f_3` returns the derivative of `f_3`.

## Linear Algebra
Define functions that perform basic vector arithmetic operations:

The sum of two vectors x and y is another vector v: 

<img src="https://storage.googleapis.com/replit/images/1518650075820_953ba3c9fcb340b0be7b89abdac116bd.gif" alt="v_i = x_i + y_i">

Calculate this new vector in a function defined `vector_sum`

The difference of two vectors x and y is another vector v:

<img src="https://storage.googleapis.com/replit/images/1518650144413_70d21223b10326213ff86d36056fed67.gif" alt="v_i = x_i - y_i">

Calculate this new vector in a function defined `vector_less`

The magnitude of a vector, its length, is:

<img src="https://storage.googleapis.com/replit/images/1518650657274_8315cf4af38c510efcffd55ec9e8f408.gif" alt="magnitude of v = sqrt(/sum_i^n v_i^2)">

Calculate this magnitude, a single number, and return it in a function defined `vector_magnitude`

Using numpy's `array` object, define functions `vec5`, `vec3`, `vec2_1`, and `vec2_2` that respectively return

<img src="https://storage.googleapis.com/replit/images/1518650939169_205222078072b03d6ef953501946596f.gif" alt="vector notation of a 5d vector containing ones, a 3d vector containing 0s, a 2d vector with 1 in x and a 2d vector with 1 in y">

Finally, the last of your precourse python examples. Write a matrix multiplication function that multiplies a 2 element vector by a 2x2 matrix `matrix_multiply(vec,matrix)`

<img src="https://storage.googleapis.com/replit/images/1518651290096_7e2a83b1bfe872e977c8052d0014a75e.gif" alt="matrix notation Mv. See LaTeX in solution.">

You can see the LaTeX description of the above matrix in `precourse.tex`.

That's it! Once again, a list of the functions you must properly implement:

* `f`
* `f_2`
* `f_3`
* `d_f`
* `d_f_2`
* `d_f_3`
* `vector_sum`
* `vector_less`
* `vector_magnitude`
* `vec5`
* `vec3`
* `vec2_1`
* `vec2_2`
* `matrix_multiply`

Good luck Lambda School Machine Learning students! Remember, while Lambda School's Machine Learning program is not a math class, everything in Machine Learning hinges upon it! These fundamentals will prepare you to understand the models that we will building, copying from the greatest innovators and implementing their original ideas.
