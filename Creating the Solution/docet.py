import tkinter as tk
#Latin Verb Conjugator, asks for 2 inputs (pronoun and verb), then 
#conjugated according to the verb ending


def conjugate(*args):
	if pronoun == "ego" and verb == "docet":
		output.insert("Ego" + " " + "doceo")
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
button.config(state = "normal", bg = "#243c6a", command = conjugate, fg = "#FFFFFF", 
	text = "Click to Conjugate")
button.grid(row = 3)

output = tk.Text(root)
output.config(state = "normal", font = ("avenir next medium", 11))
output.grid(row = 4)

root.mainloop()
print("DONE")

