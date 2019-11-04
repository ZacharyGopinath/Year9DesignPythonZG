#in this example, the input was "venit"
float == "veni"
#I then evaluate whether the ending is "it", then add "imus" to conjugate it
if float[-2:] == 'i':
	print(float+'mus')
