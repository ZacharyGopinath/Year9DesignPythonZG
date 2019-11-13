#input
verb = input("What is the verb?:")
pronoun = input("What is the pronoun?:")

#process, output

#-et verbs
if pronoun == "ego" and verb[-2] == "e":
	print("Ego" + " " + verb[0:-1] + "o")
if pronoun == "tu" and verb[-2] == "e":
	print("Tu" + " " + verb[0:-1] + "s")
if pronoun == "eam" and verb[-2] == "e":
	print("Eam" + " " + verb[0:-1] + "t")
if pronoun == "eum" and verb[-2] == "e":
	print("Eum" + " " + verb[0:-1] + "t")
if pronoun == "nos" and verb[-2] == "e":
	print("Nos" + " " + verb[0:-1] + "emus")
if pronoun == "vos" and verb[-2] == "e":
	print("Vos" + " " + verb[0:-1] + "etis")
if pronoun == "eas" and verb[-2] == "e":
	print("Eas" + " " + verb[0:-1] + "nt")
#-at verbs
if pronoun == "ego" and verb[-2] == "a":
	print("Ego" + " " + verb[0:-1] + "o")
if pronoun == "tu" and verb[-2] == "a":
	print("Tu" + " " + verb[0:-1] + "s")
if pronoun == "eam" and verb[-2] == "a":
	print("Eam" + " " + verb[0:-1] + "t")
if pronoun == "eum" and verb[-2] == "a":
	print("Eum" + " " + verb[0:-1] + "t")


#-it verbs
if pronoun == "ego" and verb[-2] == "i":
	print("Ego" + " " + verb[0:-1] + "o")
if pronoun == "tu" and verb[-2] == "i":
	print("Tu" + " " + verb[0:-1] + "s")
if pronoun == "eam" and verb[-2] == "i":
	print("Eam" + " " + verb[0:-1] + "t")
if pronoun == "eum" and verb[-2] == "i":
	print("Eum" + " " + verb[0:-1] + "t")

#esse NOT WORKING
if pronoun == "ego" and verb == "est":
	print("Ego" + " " + "sum")
if pronoun == "tu" and verb == "est":
	print("Tu" + " " + "es")
if pronoun == "eam" and verb == "est":
	print("Eam" + " " + "est")
if pronoun == "eum" and verb == "est":
	print("Eum" + " " + "est")


