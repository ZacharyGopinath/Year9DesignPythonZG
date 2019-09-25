#Build a basic funtion that calculates volume of a cylinder
#given the height and radius
import math

#Function: A small piece of code that can be called upon and executed
#What it takes
#What it does\What its name is
#What it returns

def calcVolumeCylinder(radius, height):
	print("Calculate Volume Function")
	
	if radius >= 0 and height >= 0:
		volume = math.pi * pow(radius,2) * height
		volume = round(volume, 2)
		print(volume)
	else:
		print("BAD DATA")


print("Start Program")
calcVolumeCylinder(3, 4)
print("End Program")