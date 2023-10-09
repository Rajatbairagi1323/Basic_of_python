# ----OPERATORS----

# Operator is symbol that perform certain operation.
# python provides the following set of operations.

# 1) Arithmetic operators
# 2) Reational operators or comparision operators 
# 3) logical operators 
# 4) Bitwise operators
# 5) Assingment operators
# 6) special operators



# 1) Arithmetic operators:

# + --> addition 
# - ---> subtraction
# * ---> multiplication
# / ---> division
# % ---> modulo
# // ---> floor division
# ** ---> exponent or power operator


a=10
b=2

print('a+b=',a+b)  # -->12
print('a-b=',a-b)  # -->8
print('a*b=',a*b)  # -->20
print('a/b=',a/b)  # -->5.0
print('a%b=',a%b)  # -->0
print('a//b=',a//b)# -->5
print('a**b=',a**b)# -->100






a=10.5
b=2

print('a+b=',a+b)  # -->12.5
print('a-b=',a-b)  # -->8.5
print('a*b=',a*b)  # -->21.5
print('a/b=',a/b)  # -->5.25
print('a%b=',a%b)  # -->0.5
print('a//b=',a//b)# -->5.0
print('a**b=',a**b)# -->110.25





# --Note--

# / operator always perform floatng point arithmetic. Hence it will always return floating value.

# But floor division (//) can perform both floating point and integral arithmetic. If argument are int type then result is int type.
# If atleast one argument is float type then result is float type.




# ----NOTE----

# we can use + , * operator for str type also.
# If we want to use + operator for str type then compulsary both argument should be srt type only otherwise we will get error.


# "rajat" +10  ----> Type error must be srt not int 


"rajat"+"10"

# "rajat10"


# If we use * operator for str type then compulsary one argument should be int and other argument should be str type.


2*"rajat"

# rajatrajat


# 2.5*"rajat" ---> type error cant multiply  sequence by non-int of type 'float'.


# "rajat"*"rajat" ---> Type error cant multiply sequence non-int of type "str". 


#  + ---> string concatination operator.

#  * ---> string multiplication operator.



# ----NOTE----

# for any number x ---> x/0 and x%0 always raises "zero division error"

10/0
10.0/0








# Relational operator:

# >,>=,<,<=

a=10
b=20

print("a>b is", a>b)  # a>b is --> False
print("a>=b is", a>=b)# a>=b is --> False
print("a<b is", a<b)  # a<b is --> True
print("a<=b is", a<=b)  # a<=b is --> True


# we can apply relation operator srt type also.



a="rajat"
b="rajat"


print("a>b is", a>b)  # a>b is --> False
print("a>=b is", a>=b)# a>=b is --> True
print("a<b is", a<b)  # a<b is --> False
print("a<=b is", a<=b)  # a<=b is --> True




print(True>True) # ----> False
print(True>=True) # ----> True
print(10>True) # ----> True
print(False>True) # ---> False


print(10>"rajat") # --> type error not support between of int and srt.


a=10
b=20

if(a>b):
    print("a  is greater than b")
else:
    print("a  is not greater than b")

# output --> a is not greater than b.


# ---NOTE---

# Chaining of relational operator is possible. In the chaining if all comparision return True then only result is True. If atleast one comparision 
# return False then the result is False.

# Ex--

10<20 # --> True
10<20<30 # --> True
10<20<30<40 # ---> True
10<20<30<40>50 # ---> False








   




