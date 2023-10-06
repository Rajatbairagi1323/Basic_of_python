# ---- TYPE CASTING ----

# We can convert one type value to another type. This conversion is called Typecasting or Type coersion.

# The following are various inbuild functions for type casting.

# 1) int()
# 2) float()
# 3) complex()
# 4) bool()
# 5) str()


# 1) We can use this function to convert values from others type to int.

int(123.987)


int(10+5j)


int(True)


int(False)


int("10")


int("10.5")  # ---> value error invalid literals for int() with base 10: 10.5


int("ten") # ---> value  error


int("0b1111") # ---> value error





# ---NOTE---

# We can convert from any type to int except complex type.
# If we want to convert str type to int type compulsary str should contain only integral value and should be specified in base 10.






# float()

# we can use float() function to convert other type value to float type.

float(10)


float(10+5j) # ---> type error cant convert complex to float


float(True)


float(False)


float('10')


float('10.5')


float('ten') # ----> value error


float('ob111') # ---> could not convert string to float : 'ob111'



# --NOTE--

# we can convert any type value to float type accept complex type.
# whenever we are trying to convert str type to float type integral or float point literal and should be specified only in base - 10.





# COMPLEX()

# We can use complex() function to convert other typed to complex type.

# form:1  complex(x)

# we can use this function to convert into complex number with real part X and imaginary part 0.


complex(10)  # ---> (10+0j)


complex(10.5) # ---> (10.5+0j)


complex(True) # ---> (1+0j)


complex(False) # ---> (0j)


complex('10') # ---> (10+0j)


complex('10.5') # ---> (10.5+0j) 


complex('ten') # ---> value error complex() arg is a malformed string



# form :2 complex(x,y)

# we can use this method to convert x and y into complex number such that x will be real part and y will be imaginary part.

# ex--

complex(10-2)

complex(Tue,False)





# bool()


# we can use this function to convert other type value to bool type.


bool(0)  # ---> False


bool(1)  # ---> True


bool(10)  # ---> True


bool(0.178)  # ---> True


bool(0.0)  # ---> False


bool(10-2j)  # ---> True


bool(0+1.5j)  # ---> True


bool(0+0j)  # ---> True


bool('True') # ---> True



bool('False') # ---> True



bool('') # ---> False


bool(' ') #---> True




# If x is int datatype 


# 1) 0 means False
# 2) non-zero means True





# If x is float datatype

# 1) If total number value is zero then result is false otherwise the result is True.



# If x is complex datatype

# 1) If both real and imaginary part are zero i.e 0+0j then the result is false otherwise the result is True.




# If x is srt datatype 

# 1) If x is empty string then the result is false otherfwise the result is True.




# str()

# We can use this method to convert other type values to str type.


str(10)


str(10.5)


str(10+5j)


str(True)

