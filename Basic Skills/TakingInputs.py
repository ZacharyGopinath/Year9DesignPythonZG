#Remember to comment code

#This program will take 2 integers and multiply them 

#Input
#The input function returns the string that the user enters
#All inputs start as strings
#To change the type, you "cast" it
#Casting is the process of changing type
name = input("Please input your name: ")
a = input("Please input first number: ")
a = int(a) #Self-referencig assignment 
b = input("Please input second number: ")
b = int(b)
#Process
product = a * b


#Output
print("Hi " + name + "!")
print("The product of "+str(a)+" and "+str(b)+" is "+str(product)+".")
