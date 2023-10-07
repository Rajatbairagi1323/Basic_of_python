# ---FUNDAMENTAL DATA TYPE VS IMMUTABILITY---

# All fundamental data type are immutable .i.e once we creates an object. we cannot perform any changes in their object. If we are trying to change
# then with those changes are new object will be created. This non changeable behaviour is called immutability.



# In python a new object is required then PVM wont create object immediately. First it will check is any object available with the required 
# Content or not. If available then existing object will be reused. If it is not available then only a new object will be created. The advantage
# of this approach is memory utilization and performance will be improved.



# But the problem in this approach is several reference pointing to the same object by using one reference if we are allowed to change the content
# in the existing object then the remaining reference will be effected. To prevent this immutability concept  is required. According to this once
# concept is required. According to this once created an object we are not allowed to change content. If we are trying to change with those change
# new object will be created.


# ex-

# a=10
# b=10
# a is b 
# True
# id(a) --> id is same
# id(b) --> id is same



a=10

b=10

id(a)

id(b)

a is b

# Both id(a) and id(b) are same




a=10+5j

b=10+5j

id(a)

id(b)

a is b

# Both id(a) and id(b) are different



a=True

b=False

a is b # --> True

id(a)

id(b)

# Both id(a) and id(b) are same




a='Rajat'

b='Rajat'

a is b #--> True

id(a)

id(b)

# Both id(a) and id(b) are same








# ---- BYTES DATA TYPE----

# bytes data type represent a group of bytes number just like an array.


x=[10,20,30,40,50]

b=bytes(x)

type(b)

print(b[0])  # 10

print(b[-1]) # 40

for i in b: print(i)


# 10
# 20
# 30 
# 40 
# 50



# Conclusion 1: The only allowed value for byte data type are 0 to 256. By mistake if we are trying to provide any other values then we will get 
# value error.


# Conclusion 2: Once we creates bytes data type value we cannot change the value otherwise we will get type error.


x=[10,20,30,40]

b=bytes(x)

b[0]=100


# Type error: 'bytes' object does not support item assingment.








# --BYTEARRAY DATA TYPE-- 

# bytearray is exactily same as bytes data type except that its elements can be modified.


x=[10,20,30,40]

b=bytearray(x)

for i in b: print(i)

# 10
# 20 
# 30 
# 40

b[0]=100


for i in b: print(i)

# 100
# 20 
# 30 
# 40


x=[10,256]

b=bytearray(x)

# value error: byte must be in range (0,256)


