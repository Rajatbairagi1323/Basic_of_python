
#    ------- SUMMARY OF DATATYPE IN PYTHON 3 -------


#  DATA TYPE                  DESCRIPTION                           IS IMMUTABLE                                        EXAMPLE

#  int           we can use to represent the whole/integral          immutable                          a=10
#                numbers.                                                                               type(a) ----> int


# float          we can use to represent the decimal/                immutable                          b=10.5
#                floating point numbers                                                                 type(b) ----> float


# complex       we can use to represent the complex                  immutable                          c=10+5j
#               number                                                                                  type(c) ----> complex ,c.real=10,c.imag=5.0

# Bool          we can use to represent the logical                  immutable                          d=True
#               values are True and False                                                               type(d) ---> bool
                                                                                                    


# str          To represent sequence of character                    immutable                          e='rajat'
#                                                                                                       type(e) ---> str


# bytes        To represent a sequence of charachter                 immutable                          list=[1,2,3]  
#                                                                                                       f=bytes(list)
#                                                                                                       type(f) ---> bytes


# bytearray   To represent a sequence of byte values                 mutable                            list=[10,20,30,40,50]            
#             from 0-255                                                                                g=bytearray(list)                        
#                                                                                                       type(g) ----> bytearray


# range       To represent a range of values                         immutable                          r=range(10)
#                                                                                                       r1=range(0,10)
#                                                                                                       r2=range(0,10,2)


# list       To represent an order collection of                     mutable                            l=[10,11,12,13,14,15] 
#            object                                                                                     type(l) ----> list 


# tuple      TO represent an order collection of                     immutable                          t=(1,2,3,4)
#            object                                                                                     type(t) ----> tuple


# set        To represent an unorder collection of                   mutable                            s={1,2,3,4,5}
#            unique object                                                                              type(s) ----> set


# frozenset  TO represent an unorderd collection of                 immutable                           s=(11,2,3,'rajat','shyam')                  
#            unique objects                                                                             fs=frozenset(s)
#                                                                                                       type(fs) ----> frozenset


# dict       TO represent a group of  key value pairs               mutable                             d={101:'sam',102:'rohit',103:'virat'}
#                                                                                                       type(d) ----> dict




# None data type:-

# None means nothing or no value associated.
# If the value is not available then to handle such type of cases None introduced. 
# It is something like null value in java.


# Ex-   

def m1():
    a=10
    
print(m1())  # ---> None







# -----  ESCAPE CHARACTER:-  -----

# In string literal we can use escape character to associate a special meaning.


s='rajat\nbairagi'
print(s)

# rajat
# bairagi

s='rajat\tbairagi'
print(s)

# rajat  bairagi

# s="This is "symbol" ---> invalid syntax

s="This is \"symbol"
print(s)

# This is "symbol



# The following are various important escape character in python.


# 1) \n ===> New line
# 2) \t ===> Horizontal tab
# 3) \r ===> Carriage return
# 4) \b ===> Back space
# 5) \f ===> fprm feed
# 6) \v ===> vertical tab
# 7) \' ====> single quote
# 8) \" ===> double quote
# 9) \\ ===> back slash symbol

# ................





# ---CONSTANTS:---

# Constant concept is not applicable in python.
# But it is convention to use only uppercase characters if we don't want to change value.

# MAX_VALUE=10

# It is just convention but we can change the value.

