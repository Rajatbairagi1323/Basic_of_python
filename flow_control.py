# if-elif-else flow control:

# example  for if condition 
name=input("Enter name: ")
if name=="Rajat":
    print("Hello Rajat good morning.")
print("How are you ?")      #  input is not (Rajat) how are you is print because it is in not in if condition.



# example of if and else condition.     # else is a optional
name=input("Enter name: ")              #  if (use)
if name=="Rajat":                       #  if-else (use)
    print("Hello Rajat good morning.")  #  if-elif (use)
else:                                   #  if-elif-else (use)
    print("Hello guest good morning")   #  switch is not available in python.
print("How are you ?")



# program for selecting car brand.....
car=input("Enter your car brand: ")
if car=="Honda":
    print("Honda city,Honda Amaze,Honda Civic--> Is available")
elif car=="Maruti":
    print("Maruti 800, Baleno, Ciaz --> Is available")
elif car=="Hyundai":
    print("i-20, Verna, i-10--> Is available")
elif car=="XUV":
    print("XUV300, XUV500, XUV800--Is available")
else:
    print("No available")
print("Thanks for showing your intrest!")


# program to find biggest of two given number by taking input.
num_1=int(input("Enter 1st number: "))
num_2=int(input("Enter 2nd number: "))
if num_1>num_2:
          print(num_1,"is a greater number")
else:
    print(num_2,"is a greater number")


#program to find biggest of three given number by taking input.
num_1=eval(input("Enter 1st number: "))   # In place of int use eval because you use int value not pass any other value like float and string.
num_2=eval(input("Enter 2nd number: "))   # you Enter string it compare only first letter  for example "rajat" --> r
num_3=eval(input("Enter 3nd number: "))
if num_1>num_2 and num_1>num_3:
          print(num_1,"is a greater number")
elif num_2>num_1 and num_2>num_3:
    print(num_2,"is a greater number")
else:
    print(num_3,"is a greater number")
