#in this example, the input was "venit"
str = "Venit"
#I then evaluate whether the ending is "it", then add "imus" to conjugate it
if str[-2:] == "i":
    print("str" + "imus")
print("Error: Not an -it verb")