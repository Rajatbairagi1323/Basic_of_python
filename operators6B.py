# ---- Equality Operator ----

# == , !=

# we can apply these operator for any type even for incompatible types also.


# 10 == 20 ---> False
# 10 != 20 ---> True
# 10 == True ---> False
# False == False ---> True
# 'rajat' == 'rajat' ---> True
#  10 == "rajat" ---> False


# ---- NOTE ----

# Chaining concept is applicable for equality operator. If atleast one comparision return False then the result is False then the result is False.
# otherwise the result is True.

10==20==30==40 # ---> False

10==10==10==10 # ---> True




# --- LOGICAL OPERATOR ---

# and, or, not

# we can apply for all types.


# For boolean types behaviour:

# and ==> if both argument are True then only result is True.

# or ==> if atleast one argument is True then the result is True.

# not ==> complement

True and True # --> False
True and False # --> True
not False # --> True




# For non - boolen type behaviour:

# 0 means False
# non zero means True
# empty string is always return as False



# If x is evaluates to False return x otherwise return y.

# Ex-  10 and 20

# Ex-  0 and 20  ---> If first argument is zero then the result is zero otherwise result is y.


# x or y

# If x evaluates to True then result is x otherwise result is Y.

10 or 20
0 or 20


# not x:
# If x is evaluates to False then result is True otherwise Flase

not 10 # ---> False
not 0 # ----> True



"rajat" and "rajatbairagi" # --> rajatbairagi

"" and "rajat" # ---> ""

"durga" and "" # ---> ""

"" or "rajat" # ---> "rajat"

"rajat" or ""  #  ---> "rajat"

not"" # ---> True

not"rajat" # ---> False






#  --- BITWISE OPERATOR ---

# We can apply these operator bitwise these operators are applicable only for int and boolean type by mistake if we are trying to apply for any
# other type then we will get error.

#   & , \ , ^ , ~ , << , >>

print(4&5) # --> valid

print(10.5&5.6) # --> Type error: unsupported operand type(s) for & : float and "float".

print(True & True) # --> valid



#  & --> If both bits are 1 then result is 1 otherwise result is 0.

# \ --> If atleast are different then only result is 1 otherwise result is 0.

# ^ --> If bits are different then only result is 1 otherwise result is 0.

# ~ --> bitwise complement operator 


#  1 = 0 & 0 = 1

# << --> bitwise left shift 

# >> --> bitwise right shift


print(4&5)  # --> 4
print(4|5)  # --> 5
print(4^5)  # --> 1



#  operator             Description

#    &                  If both bits are 1 then only result is 1 otherwise result is 0.

#   \                   If atleast one bit is 1 then result is 1 otherwise result is 0.

#   ^                   If bits are different then only result is 1 otherwise result is 0.

#   ~                   bitwise complement operator i.e. 1 means 0 and 0 means 1.

#  >>                   Bitwise left shift operator.

#  >>                   Bitwise right shift operator.





# Bitwise complete operator (~):

# we have to apply complement for total bits.

print(~5) # --> -6


# ---NOTE---

# The most significant bit acts sign bit,
# 0 value represent +ve number where as 1 represent -ve value.

# positive numbers will be represent directly in the memory where as -ve numbers will be represent indirectly in 2's complement form.



# shift operator:

# << left shift operator
# After shifting the empty cells we have to fill with zero.

print(10<<2) # --> 40


# 0. 0. 0 0 1 0 1 0

# 0  0 1 0 1 0 0 0


# >> right shift operator 
# After shifting the empty cells we have to file with sing bit (0 for +ve and 1 for -ve)

print(10>>2) # --> 2

# 0 0 0 0 1 0 1. 0.

# 0 0 0 0 0 0 1 0

# we can apply bitwise operator for boolean type also.

print(True & False) # --> Flase
print(True | False) # --> True
print(True ^ False) # --> True
print(~ True)       # --> -2
print(True << 2)    # --> 4
print(True>>2)      # --> 0



# Assignment operators:

# we can use assignment operator to assign value to the variable.

# Ex-  X = 10

# we can combine assingment operator with some other operator to from compound assingment operator.


#  x+ = 10  ,  x = x+10


# The following in the list of all possible compound assignment operator in python.

# +=

# -=

# *=

# /=

# %=

# //=

# **=

# &=

# \= 

# ^=

# >>=

# <<=


# Ex-   

x=10
x+=20
print(x)   # --> 30


x=10
x&=5
print(x)  # --> 0

