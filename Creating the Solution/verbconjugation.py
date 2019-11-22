import tkinter as tk
#Latin Verb Conjugator, asks for 2 inputs (pronoun and verb), then 
#conjugated according to the verb ending


def conjugate(*args):
	#-et verbs
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
	if pronoun == "ego" and verb == "est":
		outputm.insert(tk.END, "Ego" + " " + "sum")
	if pronoun == "tu" and verb == "est":
		outputm.insert(tk.END, "Tu" + " " + "es")
	if pronoun == "eam" and verb == "est":
		outputm.insert(tk.END, "Eam" + " " + "est")
	if pronoun == "eum" and verb == "est":
		outputm.insert(tk.END, "Eum" + " " + "est")

#GUI
root = tk.Tk()
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

button = tk.Button(text = "Click to Conjugate", borderwidth = 2)
button.config(bg = "#243c6a", command = conjugate, fg = "#FFFFFF")
button.grid(row = 3)

outputm = tk.Text()
outputm.config(state = "normal", font = ("avenir next medium", 10))
outputm.grid(row = 4)

root.mainloop()
outputm.insert("Done")

