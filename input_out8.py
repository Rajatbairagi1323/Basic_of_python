	# --Input and Output Statement--

# Reading dynamic input from the keyboard

# In python2 the following 2 functions are available to read dynamic input from the keyboard.

# 1) raw_input()

# 2) input()


# raw_input():
# This function always read the data from  the keyboard in the from of string format. we have to convert the string type to our required type by
# using the corresponding type casting methods.


# Ex  
x=raw_input("Enter first number: ")
print(type)          # It will always print str type only for any input type



# input():
# input function can be used data directly in our required format. we are not required to perform type casting.

x=input("enter your number: ")
print(x)
type(x)


# "Rajat" ---> str
# 10.5 ---> float
# True ---> bool


#----Note----

# But in python3 we have only input() method and raw_input() method is not available python3 input() function behaviour exectly same as raw_input(),
# method of python 2 . i.e every input value treated as str type only.


# raw_input() function of python2 is renamed as input() function in python3.

type(input("Enter value: "))

# Enter value : 10
# <class 'str'> 

# Enter value : 10.5
# <class 'str'> 

# Enter value : True
# <class 'str'> 



# Write a program to read a employee data from a keyboard and print the data.

eno = input("Enter emp no :")
ename= input("Enter ename: ")
esal= float(input("Enter emp salary:"))
eaddr= input("Enter eaddr": ))
married= input("Enter married ? [True|False]: "))


print(eno)
print(ename)
print(esal)
print(eaddr)
print(married)


# How to read multiply value from the keyboard in a single line?

a,b = [int(x) for x in input("Enter your 2 number:").split()]
print(product is :, a*b)





# Write a program to read a float no from the keyboard with the seprator and print their sum.


a,b,c =[float(r) for r in input("Enter your 3 number: ").split(",")]
print("The sum of 3 number is: ",a+b+c)



# eval()

# eval funtion take a string and evaluate the result 


x = eval("10+20+30")

print(x)

# output : 60



x = eval(input("Enter your Expression: "))

# Enter your Expression: 10+2*3/4

# output: 11.5



# eval() can evaluate the input to list, tuple, set, etc based the provided input.


# write a program to accept list from the keyboard on the display



i=eval(input("Enter list"))

print(type(i))
print(i)





















































 
