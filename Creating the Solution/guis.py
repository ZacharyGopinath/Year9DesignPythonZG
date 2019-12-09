import tkinter as tk

def decide(*args):
	if entry == "ego":
		output.insert("Noun")
	if entry == "docet":
		output.insert("Verb")


root = tk.Tk()
root.Title = "Switch GUIs"

title = tk.Label()
title.config(bg = "#243c6a", fg = "#FFFFFF", text = "Input Word Below")
title.grid(row = 0)

entry = tk.Entry()
entry.config()
entry.grid(row = 1)

output = tk.Text()
output.config(heigh = 10, width = 10)
output.grid(row = 2)

button = tk.Button()
button.config(bg = "#243c6a", command = "decide", fg = "#FFFFFF", 
	text = "Click to Conjugate")
button.grid(row = 3)

root.mainloop()

