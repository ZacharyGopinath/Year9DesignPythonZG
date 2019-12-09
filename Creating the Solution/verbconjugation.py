import tkinter as tk
#Latin Verb Conjugator, asks for 2 inputs (pronoun and verb), then 
#conjugated according to the verb ending

def verb():
	output.insert(tk.END, "Verb")
	output.config(state = "disabled", height = 10, width = 20, bg = "#243c6a", fg = "#FFFFFF", 
	font = ("avenir next medium", 11))
def noun():
	output.insert(tk.END, "Noun")

def conjugate(*args):
	if pronoun == "ego" and verb[-2] == "e":
		outputm.insert(tk.END, "Ego" + " " + verb[0:-1] + "o")
	if pronoun == "tu" and verb[-2] == "e":
		outputm.insert(tk.END, "Tu" + " " + verb[0:-1] + "s")
	if pronoun == "eam" and verb[-2] == "e":
		outputm.insert(tk.END, "Eam" + " " + verb[0:-1] + "t")
	if pronoun == "eum" and verb[-2] == "e":
		outputm.insert(tk.END, "Eum" + " " + verb[0:-1] + "t")
	if pronoun == "nos" and verb[-2] == "e":
		outputm.insert(tk.END, "Nos" + " " + verb[0:-1] + "emus")
	if pronoun == "vos" and verb[-2] == "e":
		outputm.insert(tk.END, "Vos" + " " + verb[0:-1] + "etis")
	if pronoun == "eas" and verb[-2] == "e":
		outputm.insert(tk.END, "Eas" + " " + verb[0:-1] + "nt")

	#-at verbs
	if pronoun == "ego" and verb[-2] == "a":
		outputm.insert(tk.END, "Ego" + " " + verb[0:-2] + "o")
	if pronoun == "tu" and verb[-2] == "a":
		outputm.insert(tk.END, "Tu" + " " + verb[0:-2] + "s")
	if pronoun == "eam" and verb[-2] == "a":
		outputm.insert(tk.END, "Eam" + " " + verb[0:-2] + "t")
	if pronoun == "eum" and verb[-2] == "a":
		outputm.insert(tk.END, "Eum" + " " + verb[0:-2] + "t")

	#-it verbs
	if pronoun == "ego" and verb[-2] == "i":
		outputm.insert(tk.END, "Ego" + " " + verb[0:-1] + "o")
	if pronoun == "tu" and verb[-2] == "i":
		outputm.insert(tk.END, "Tu" + " " + verb[0:-1] + "s")
	if pronoun == "eam" and verb[-2] == "i":
		outputm.insert(tk.END, "Eam" + " " + verb[0:-1] + "t")
	if pronoun == "eum" and verb[-2] == "i":
		outputm.insert(tk.END, "Eum" + " " + verb[0:-1] + "t")

	#esse
	if pronoun == "ego" and verb == "esse":
		outputm.insert("Ego" + " " + "sum")
	if pronoun == "tu" and verb == "esse":
		outputm.insert("Tu" + " " + "es")
	if pronoun == "eam" and verb == "esse":
		outputm.insert("Eam" + " " + "esse")
	if pronoun == "eum" and verb == "est":
		outputm.insert("Eum" + " " + "est")
	
	
#GUI
root = tk.Tk()
root.geometry("600x300")
root.Title = "Latin Word Conjugator"

title = tk.Label(text = "Latin Word Conjugator")
title.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
title.grid(row = 0, column = 0, columnspan = 2)

pronoun = tk.Entry()
pronoun.config()
pronoun.grid(row = 1)

verb = tk.Entry()
verb.config()
verb.grid(row = 2)

button = tk.Button()
button.config(bg = "#243c6a", command = conjugate, fg = "#FFFFFF", 
	text = "Click to Conjugate")
button.grid(row = 3)

outputm = tk.Text()
outputm.config(state = "normal", font = ("avenir next medium", 11))
outputm.grid(row = 4)

root.mainloop()
print("DONE")

