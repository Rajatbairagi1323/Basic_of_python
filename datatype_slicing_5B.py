# ---STR TYPE ---

# str represent string data type.

# A string is a sequence of character enclosed within single quotes or double quotes.

s1='rajat'
print(s1)

s2="rajat"
print(s2)


# By using single quotes or double quotes we cannot represent multiline string literals.

s1 = "rajat
      bairagi"
      

print(s1) # get error
      

# for this requrement we should go for triple single quotes (''') or (""") triple double quotes.

s1 =  '''rajat
      bairagi'''
print(s1)

s1 =  """rajat
      bairagi"""
print(s1)


# we can  also use triple quotes to use single quotes or double quotes in our string.

# ''' This is'' character'''
# 'this i'' character'

# we can embed one string in another string. 

# '''This ''python class very helpfull'' for java students'''



# ----SLICING OF STRING----

# Slice means a piece 

# [] operator is called slice operator, which can be used to retrieve part of string.
# In python string follows zero based index.
# The index can be either +ve or -ve.
# +ve means forward direction from left to right.
# -ve means backward direction from right to left.


# -5 -4 -3 -2 -1
#  r  a  j  a  t
#  0  1  2  3  4


s='rajat'

s[0]  #----> R

s[1]  #----> A

s[-1] #----> T

S[30] #---> Index error : string index out of range.


s[1:40]

# 'ajat'

s[1:]

# 'ajat'

s[:]

# 'rajat'


len(s)

# 5


# ---Note---

# 1) In python the following data types are considered as fundamental data type.

# int
# float
# complex
# bool
# str




# 2) In python, we can represent char values also by using str type and explicitly char type is not available.

c='a'
type(c)




# Long data type is available in python 2 but not in python 3 long values also we can represent by using int type only.

# In python we can present char value also by using str type and explictly type is not available.


