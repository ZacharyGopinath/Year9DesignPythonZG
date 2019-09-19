import math
#input
#numbers needed to find volume of cylinder, height and radius/diameter

print("Volume of a Cylinder Formula:")

print("\n\tThe volume of a Cylinder is:")
print("\n\t\t\tV = \u03C0\u00d7radius\u00b2\u00d7height")
print("\n\tThis program will take as input the radius and height")
print("\tand print the volume.")

height = 1
radius = 1

name = input("\n\t\t\tWhat is your name: ")   #takes users name

while (radius !=0 or height !=0):
	
	radius = input("\n\t\t\tInput radius(cm): ")  #input
	radius = (int)(radius)     #cast to int


	height = input("\n\t\t\tInput height(cm): ") #input
	height = (int)(height)     #cast to int

	#process
	#what needs to be done to get volume from these numbers
	if (radius >= 0 and height >= 0):

		volume = math.pi*radius*radius*height
		volume = round(volume,2)

		#output
		#after calculating what number it output

		print("\n\tHi "+name+"!")
		print("\n\tGive a cylinder with:")
		print("\n\tRadius = "+str(radius))
		print("\n\tHeight = "+str(height))
		print("\n\tThe volume is: "+str(volume))  

	else:
		print("\n\t\t\tYou have entered and invalid value!")