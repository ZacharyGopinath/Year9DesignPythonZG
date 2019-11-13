#this program will ask for inputs then create a chord for you
root = input("Pick a note(Natural or sharp):")
quality = input("Pick a quality (major, minor, 7, major 7:")
#a
if root == "a" and quality == "major" or root == "g#" and quality == "major":
	print("A, C#, E")
if root == "a" and quality == "minor" or root == "g#" and quality == "minor":
	print("A, C, E")
if root == "a" and quality == "7" or root == "g#" and quality == "7":
	print("A, C#, E, G")
if root == "a" and quality == "major 7" or root == "g#" and quality == "major 7":
	print("A, C#, E, G#")
#b
if root == "b" and quality == "major":
	print("B, D#, F#")
if root == "b" and quality == "minor":
	print("B, D, F#")
if root == "b" and quality == "7":
	print("B, D#, F#, G#")
if root == "b" and quality == "major 7":
	print("B, D#, F#, A")
#c
if root == "c" and quality == "major" or root == "b#" and quality == "major":
	print("C, E, G")
if root == "c" and quality == "minor" or root == "b#" and quality == "minor":
	print("C, D#, G")
if root == "c" and quality == "7" or root == "b#" and quality == "7":
	print("C, E, G, A#")
if root == "c" and quality == "major 7" or root == "b#" and quality == "major 7":
	print("C, E, G, B")
