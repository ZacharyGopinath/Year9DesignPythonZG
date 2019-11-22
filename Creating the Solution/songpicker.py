#this program will take an input and print a song  title
import random
print("This program will help you decide which piece to listen to")

catinput = input("Category(Baroque, Classical, Romantic):")
catinput = catinput.lower()
if catinput == "baroque":
	catinput = ["Bach Praeludium 1", "Vivaldi Concerto for 2 Violins", "Bach Johanne's Passion", "Bach Mattew's Passion"]
	print(random.choice(catinput))

if catinput == "classical":
	catinput == ["Mozart Sonata 16", "Beethoven Sonata Pathetique", "Elgar Cello Concerto"]
	print(random.choice(catinput))

0	

1	

2