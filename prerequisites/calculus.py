import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import diff


def f(x):
    return 3*x**2 - 4*x +5

f(3.0)

xs = np.arange(-5, 5, 0.25)
ys = f(xs)
plt.plot(xs, ys)

# h = 0.000001
# x = 2/3
# (f(x + h) - f(x))/h

# a = 2.0
# b = -3.0
# c = 10.0
# d = a*b + c
# print(d)


# inputs
h = 0.0001
a = 2.0
b = -3.0
c = 10.0

d1 = a*b + c
c += h
d2 = a*b + c

print('d1', d1)
print('d2', d2)
print('slope', (d2 - d1)/h)


def find_all_variables(equation):
    variables = []
    for value in equation:
        if (value!='*' and 
        value!='-' and
        value!='/' and
        value!='+' and
        value!=' ' and 
        (value>'9' or value<'1')):
            variables.append(value)
    return variables

def calculate_derivatives(equation):
    variables = find_all_variables(equation)
    print(variables)
    for variable in variables:
        print(f'd/d{variable}: {diff(equation, variable)}')
    

equation = "3*x**2 - 4*y + 5"
# derivative for x should be "6x"
# derivative for y should be "-4"
calculate_derivatives(equation)

equation = "a*b + c"
# derivative for a should be "b"
# derivative for c should be "1"
# derivative for b should be "a"
calculate_derivatives(equation)