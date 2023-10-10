# ---SPECIAL OPERATOR---

# Python operator defines the following 2 special operators.

# 1) Identity operators
# 2) Membership operators


# 1) Identity Operator ---> we can use identity operator for address comparision 2 identity operators are available

# 1) is
# 2) is not


# r1 is r2 return True if both r1 and r2 are pointing to the same object.
# r1 is not r2 result True if both r1 and r2 are not pointing the same object.

a=10
b=10
print(a is b) # True

x=True
y=True
print(x is y) # True


a="rajat"
b="rajat"
print(id(a))
print(id(b))
print(a is b)





list1=["one","two","three"]
list2=["one","two","three"]
print(id(list1))
print(id(list1))
print(list1 is list2)  # False
print(list1 is not list2) # True
print(list1 == list2) # True


# NOTE:-

# we can use is operator for address comparision where as == operator for content comparision



# 2) Membership operator:

# we can use membership operator to check whether the given object present in given collection.(It may be string, list, set, tuple, or dict)

# in --> Return True if the given object present in the specified collection.

# not in ---> return True if the given object not present in the specified collection.



# Ex-

x="hello learning python is very easy"
print("h" in x) # True
print("d" in x) # False
print("d" not in x) # True
print("python" in x) # True




# OPERATOR PRECEDENCE:

# If multiple operator present than which operator will be evaluted first is decided by operator precedence.


# Ex-

print(3+10*2) # 23
print((3+10)*2) # 26


# The following list describe operators precedence in python.


# ()--> parenthsis 
# **--> exponential operator
# ~,- --> Bitwise complement operator unary minus operator 
# *,/,%,// --> multiplication, division, modulo, floor division
# +,- --> addition, substraction 
# <<, >> --> left and right shift
# & --> bitwise AND
# ^ --> bitwise x-OR
# \ --> bitwise OR
# >,>=,<,<=,==,!= --> Relational or comparision operators.
# =, +=, -=, *=, ......---> aasingment operators
# is, is not --> identity operator
# in, not in --> membership operators
# not --> logical not 
# and --> logical and 
# or --> logical or 


a=30
b=20
c=10
d=5
print((a+b)*c/d) # 100.0
print(a+(b*c)/d) # 70.0

# 3/2*4+3+(10/5)**3-2
# 3/2*4+3+2.0**3-2
# 3/2*4+3+8.0-2
# 6.0+3+8.0-2
# 15.0


