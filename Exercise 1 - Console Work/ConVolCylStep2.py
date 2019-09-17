import 
#input
#numbers needed to find volume of cylinder, height and radius/diameter

print("Volume of a Cylinder Formula:")

name = input("What is your name: ")   #takes users name

radius = input("Input radius(cm): ")  #input
radius = (int)(radius)     #cast to int

height = input("Input height(cm): ") #input
height = (int)(height)     #cast to int

#process
#what needs to be done to get volume from these numbers

volume = math.pi*radius*radius*height

#output
#after calculating what number it output

print("The volume is: ",volume)