# ----- Command line Argument -----

# argv is not array it is a list. It is available sys module.

# The argument which are passig at the time of execution we called command line argument.

# rj_classes> test.py 10 20 30
#          command line arguments

# within the python program this command line argument are available in argv. which is present in sys module.



#                     test.py 10 20 30

# Note: 

# argv[0] represent name of program. But not first command line argument argv[1] represent first command line argument.

# program: To check type of argv from sys


import argv
print(type(argv))


# write a program to display command line argument 


from sys import argv

print("The number command line Argument =: ",len(argv))

print("The list of command line argument: ",argv)

print("command line argument one by omne: ")

for x in argv :
	print(x)
	
	


from sys import argv 
sum = 0 
argvs = argv[1:]
for x in argvs:
    n = int(x)
    sum = sum +n
print("The sum: ", sum)




# Note 

# usually space is seprator between command line argument. If our command  line line argument itself contain space then we should enclose 
# within double quotes (but not in single quotes) 




from sys import argv

print(argv[1])


# D:\python_classes> py test.py sunny leone

# output --> sunny

# D:\python_classes> py test.py 'sunny leone'


# output --> sunny

# D:\python_classes> py test.py "sunny leone" 

# output --> sunny leone



# Note -2

# within the python program command line arguments are available in string form. Based on our requirement, we can convert into corresponding 
# type by using type casting methods.

from sys import argv
print(argv[1]+argv[2])
print(int(argv[1])+int(argv[2]))


# D:\python_classes> py test.py 10 20

# 1020

# output: 30



# note3 :

# if we are trying to access command line arguments with out of range index then we will get error.


from sys import argv
print(argv[100])

# D:\python_classes> py test.py 10 20

# index error: list index out of range 



# note :


# In python there is ardparse module to parse command line argument and display some help message whenever end user enters wrong input.

# input()

# raw_inputI()

# command line argument.

	
