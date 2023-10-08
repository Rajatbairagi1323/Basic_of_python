# ----LIST DATA TYPE----

# If we want to represent group of values as a single entity where insertion order  required to preserve and duplicates are allowed then we should 
# go for list data type.


# 1) Insertion order is preserved.
# 2) Heterogeneous object are allowed.
# 3) Duplicates are allowed.
# 4) Growable in nature.
# 5) Values should be enclosed within square brackets.


list = [1,10.5,'Rajat',True,10]
print(list)


list=[10,20,30,40]

list[0]

list[-1]

list[1:3]

list[0] = 100

for i in list: print(i)



# List is growable in nature .i.e. based on our requirement we can increase or decrease the size.



list=[10,20,30]

list.append('Rajat')

list  # --> [10,20,30,'Rajat']

list.remove(20)

list # ---> [10,30,'Rajat']


list2 = list*2

list2  # ---> [10,30,'Rajat',10,30,'Rajat']



# --NOTE--

# An orderd, mutable, heterogenous collection of element is nothing but list, where duplicates also allowed.




# --- Tule Data Type ---

# Tuple data type is exactly same as list data type except that it is immutable .i.e we cannot change value.
# Tuple elements can be represented within paranthesis.

t=(10,20,30,40)

type(t)

t[0]=100 #---> 'Tuple object does not support item assingment'

t.append('Rajat') #---> attribute error

t.remove(10)  # ---> attribute error


# ---NOTE---

# Tuple is the read only version of list.




# --- RANGE DATA TYPE ---

# Range data type represent a sequence of numbers.
# The elements presant in range data type are not modifiable .i.e range data type is immutable.


# Form -1: range(10)

# generate numbers from 0 to 9.

# ex-
r=range(10)
for i in r: print(i)   # print 0 to 9


# Form -2: range (10,20)

# generate numbers from 10 to 19.

r=range(10,20)
for i in r: print(i)  # print 10 to 19


# Form -3: range(10,20,2)

# 2 means increment value

r=range(10,20,2)
for i in r: print(i)  # print 10,12,14,16,18


# we can access elements present in the range data type by using index.

r=range(10,20)

r[0]  # --> 10

r[15] # index error: range object index out of range

# we cannot modify the value of range data type.

# Eg-

r[0]=100   # Type error


# We can create a list of values with range data type.

l=list(range(10))

print(l)  # ----> [0,1,2,3,4,5,6,7,8,9]





# --- SET DATA TYPE --- 

# If we want to represent a group of values without duplicates where order is not important then we should go for set data type.

# 1) Insertion order is not preserved.
# 2) Duplicates are not allowed.
# 3) Heterogeneous object are allowed.
# 4) Index concept is not available.
# 5) It is mutable collection.
# 6) Growable in nature.



s={100,0,10,200,10,'rajat'}

s


s[0] # ---> type error: set object does not support indexing.


# Set is growable in nature based on our requirement we can increase or decrease the size.

s.add(60)

s  # ---> {100,0,10,200,10,'rajat',60}


s.remove(100)

s # --> {0,10,200,10,'rajat',60}




# ---FROZENSET DATA TYPE---

# It is exactly same as set except that is immutable.
# Hence we cannot use add or remove functions.


s={10,20,30,40}

fs=frozenset(s)

type(fs)

fs  # frozenset({40,10,20,30})


for i in fs: print(i)

# 10
# 20
# 30 
# 40


fs.add(70) # --> attribute error : 'frozenset' has no attribute 'add'

fs.remove(10) # --> attribute error : 'frozenset' has no attribute 'remove'




# ---DICT DATA TYPE---


# If we want to represent a group of valued as a key - value pairs then we should go for dict data type.

# Eg :-

d={101:'Rajat',102:'mayur',103:'kapil'}

print(d)

# Duplicate keys are not allowed but values can be duplicated. If we are trying to insert an entry with duplicate key then add value will be
# replaced with new value.


d={101:'sam',102:'herry',103:'bishnu'}

d[101]='sunny'

d # {101:'sunny',102:'herry',103:'bishnu'}

# we can create empty dictionary as follows.


d={}

# We can add key value pairs as follows.

d['a']='apple'

d['b']='banana'
s
print(d)

# Note:- dict is mutable and the order want be preserved.



# Note:

# 1) In general we can use bytes and bytesarray data types to represent binary information like image, video, files etc.

# 2) In  python2 long data type is available. But in python3 it is not available and we can represent long values also by using int type only.

# 3) In python there is no char data type. Hence we can represent char values also by using str type.


