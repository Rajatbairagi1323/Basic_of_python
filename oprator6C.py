# ---TERNARY OPERATOR---

# X = first value if conition else second value.
# If condition is True then first value will be considered else second value will be considered.

# Ex-   
a,b = 10,20
x=30 if a>b else 40
print(x)  # 30

# Read two numbers from the keyboard and print minimum value.

a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
min=a if a<b else b
print("minimum value:",min)



# output
# Enter your first number: 20
# Enter your second number: 30
# minimum value: 10


# NOTE: Nesting of ternary operator is possible.


# Program for minimum of 3 numbers

a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
c=int(input("Enter your third number: "))


min=a if a<b and a<c else b if b<c else c

print("minimum value:",min)


# Program for maximum of 3 numbers

a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
c=int(input("Enter your third number: "))


max=a if a>b and a>c else b if b>c else c

print("maximum value:",max)



# Ex-

a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
print("Both number are equal" if a==b  else "first number is greater than second number" a>b else "second number is greater than first number" )


# output 

# Enter first number: 10
# Enter second number: 10
# Both the number we qual



# Enter your first number: 10
# Enter your second number: 20
# First number is greater than second number


# Enter first number: 20
# Enter second number: 10
# First number greater than second number.



