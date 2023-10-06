# --------DATA TYPE---------

# Data type represent the type of data present inside a variable.
# In python we are not required to specify the type explicitly. Based on value provided the type will be assingned automatically.
# Hence pythonis dynamically  typed language.




# ----PYTHON CONTAINS THE FOLLOWING INBUILD DATA TYPE----

# 1)  int
# 2)  float
# 3)  complex
# 4)  bool
# 5)  str
# 6)  bytes
# 7)  bytearray
# 8)  range
# 9)  list
# 10) tuple
# 11) set 
# 12) frozenset
# 13) dict
# 14) none





# ----NOTE :--> PYTHON CONTAIN SEVERAL INBUILD FUNCTIONS ----

# 1) type() ---> to check the type of variable.

# 2) id() ---> to get address of object

# 3) print() ---> to print the value

# IN PYTHON EVERYTHING IS OBJECT 






# ----INT DATA TYPE----

# We can use int data type to represent the whole numbers (integral literal) values.

# ex--

a = 10
type(a)  # int type


# --Note--

# In python 2 we have long data type to represent the large integral values. But in python 3 there is no long type explicitlly and we can represent 
# long values also by using the int type only.


# we can represent int values in the following ways.


# 1) Decimal form
# 2) Binary form
# 3) octal form
# 4) hexa decimal form  




# 1) Decimal form (Base - 10):

# It is the default number system in python.
# The allowed digits are : 0 to 9 
# Ex

a=10  


# 2) Binary form (Base - 2):

# The allowed digits are : 0 & 1 
# Literal value should be prefixed with 0b or 0B.
# Ex

a=0B1111
a=0b123
a=b111



# 3) octal form (Base - 8):

# The allowed digits are : 0 to 7.
# literal value should be prefixed with 0o or 0O.
# Ex

a=0o123
a=0o786


# 4) Hexa decimal form (Base - 16):

# The allowed digits are : 0 to 9 , a to f (Both lower and upper cases are allowed ) literal values should be prefixed with 0x or 0X.
# EX 

a=0xFACE
a=0xBeef
a=0xBeer


# --NOTE--

# Being a programmer we can specify literals values in decimal binary or octal and hexa decimal forms. But PVM will provide values only in decimal.

a=10
b=0o10
c=0X10
d=0B10
print(a)
print(b)
print(c)
print(d)




# -----BASE CONVERSION -----

# Python provide the following in-build-function for base conversion.

# 1) bin():         
# We can use bin() to convert from any base to binary.

bin(15)

bin(0o11)

bin(0x10)


# 2) oct():
# We can use oct() to convert from any base to octal.

oct(10)

oct(0B111)

oct(0X123)



# 3) hex():
# we can use hex() to convert from any base to hexa decimal.

hex(10)

hex(0b111111)

hex(0.12345)




# ---Float data type---

# we can use float data type to represent floting point values (decimal values)

f=1.234
type(f)


# We can also represent floating point values by using exponential form (scientific notation)

f=1.2e3
print(f)

# insted of 'e' we can use 'E'

# The main advantage of exponential form is we can represent big values in less memory.



#--NOTE--

# we can represent int values in decimals, binary, octal, and hexa decimal form.

# f=0b11.01 ---> show syntax error invalid syntax






# ----COMPLEX DATA  TYPE -----

# A complex number is of the form   
# a+bj   
# a=real part 
# b=imaginary part
# j^2 = -1

# a and b contain integers or floating point value.
# ex 

a=3+5j
b=10+5.5j
c=0.5+0.1j

print(a)
print(b)
print(c)


# In the real part if we use int values then we use specify that either by decimal, octal, binary or hexa decimal form.
# But imaginary part should be specified only by using decimal form.

a=0B111+5j
a


a=3+0B11j
# syntax error : invaild error

# Even we can perform operations on complex type values.

a=10+1.5j
b=20+2.5j
c=a+b
print(c)

type(c)


# --NOTE--

# Complex data type has some inbuild attributes to retrieve the real part and imaginary part.

c=10.5+3.6j

c.real
c.imag

# we can use complex type generally in scientific applications and electric engineering applications.





# --- BOOL DATA TYPE ---


# We can use this data type to represent boolean values.
# The only allowed values for this data type are:
# True and Flase

# Internally python represent True as 1 and False as 0.

b=True
type(b)


a=10
b=20
c=a<b
print(c)


True+True  # 2
True-False # 1


