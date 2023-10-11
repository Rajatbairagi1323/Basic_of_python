# --- MATHEMATICAL FUNCTION (math module)

# A module is collection of function variable and classes etc.


# Math is a module that contains several functions to perform mathematical operations.

# If we want to use any module in python, first we have to import that module.



# import math

# Once we import a module then we can call any function of that module.

import math
print(math.sqrt(16))
print(math.pi)

# 4.0
# 3.141592653589793

# we can create alias name by using that we can access function are variables of that module.


import math as m
print(m.sqrt(16))
print(m.pi)



# If we import a member explicitly then it is not required to use module name while accessing.


from math import sqrt,pi
print(sqrt(16))
print(pi)
print(math.pi) # ---> Name error: name "math" is not defined



# import function of math module:


import math

# Constants
pi = math.pi                # Pi (3.141592653589793)
e = math.e                  # Euler's number (2.718281828459045)
tau = math.tau              # Tau (2 * pi)

# Basic mathematical functions
math.ceil(x)                # Ceiling function (smallest integer not less than x)
math.floor(x)               # Floor function (largest integer not greater than x)
math.trunc(x)               # Truncate x to an integer
math.fabs(x)                # Absolute value (|x|)
math.factorial(x)           # Factorial of x
math.gcd(a, b)              # Greatest common divisor of a and b
math.pow(x, y)              # x to the power y
math.sqrt(x)                # Square root of x

# Trigonometric functions
math.sin(x)                 # Sine of x (in radians)
math.cos(x)                 # Cosine of x (in radians)
math.tan(x)                 # Tangent of x (in radians)
math.asin(x)                # Arcsine (inverse sine) of x, in radians
math.acos(x)                # Arccosine (inverse cosine) of x, in radians
math.atan(x)                # Arctangent (inverse tangent) of x, in radians
math.atan2(y, x)            # Arctangent of y/x, in radians, with signs considered

# Hyperbolic functions
math.sinh(x)                # Hyperbolic sine of x
math.cosh(x)                # Hyperbolic cosine of x
math.tanh(x)                # Hyperbolic tangent of x
math.asinh(x)               # Inverse hyperbolic sine of x
math.acosh(x)               # Inverse hyperbolic cosine of x
math.atanh(x)               # Inverse hyperbolic tangent of x

# Logarithmic functions
math.log(x)                 # Natural logarithm of x
math.log10(x)               # Base-10 logarithm of x
math.log2(x)                # Base-2 logarithm of x
math.exp(x)                 # Exponential function e^x

# Miscellaneous functions
math.degrees(x)             # Convert radians to degrees
math.radians(x)             # Convert degrees to radians

# Constants for special values
math.inf                    # Positive infinity
-math.inf                   # Negative infinity
math.nan                    # Not-a-Number

# Constants for precision
math.tau                    # Tau (2 * pi)
math.inf                    # Positive infinity
-math.inf                   # Negative infinity
math.nan                    # Not-a-Number

# Other functions
math.comb(n, k)             # Number of ways to choose k items from n items without repetition

# Random functions (requires the random module)
math.randbytes(n)           # Generate n random bytes

# Angular conversion functions
math.degrees(x)             # Convert radians to degrees
math.radians(x)             # Convert degrees to radians

# Special functions (requires the scipy module)
math.erf(x)                 # Error function
math.erfc(x)                # Complementary error function
math.gamma(x)               # Gamma function
math.lgamma(x)              # Natural logarithm of the absolute value of the gamma function





# import variable of math module:
# pi3.14
# e --> 2.71
# inf --> infinity
# man --> not a number



# Write a python program to find area of circle.

#  pi*r**2

from math import pi
r=16
print("Area of circle is: ",pi*r**2)

# output--> Area of circle is: 804.247719318987






