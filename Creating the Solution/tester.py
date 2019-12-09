import tkinter as tk

def verb():
	output.insert(tk.END, "Verb")
	output.config(state = "disabled", height = 10, width = 20, bg = "#243c6a", fg = "#FFFFFF", 
	font = ("avenir next medium", 11))
def noun():
	output.insert(tk.END, "Noun")
	output.config(height = 0, width = 0, bg = "#FFFFFF", fg = "#FFFFFF")
	nounoutput = tk.Text()
	nounoutput.config()
	nounoutput.grid(row = 3)

root = tk.Tk()
root.Title = "Switch GUIs"

title = tk.Label()
title.config(bg = "#243c6a", fg = "#FFFFFF", text = "Is the word a noun or verb?")
title.grid(row = 0, columnspan = 2)

nbutton = tk.Button()
nbutton.config(bg = "#243c6a", command = noun, fg = "#FFFFFF", 
	text = "Noun")
nbutton.grid(row = 1, column = 0)

vbutton = tk.Button()
vbutton.config(bg = "#243c6a", command = verb, fg = "#FFFFFF", 
	text = "Verb")
vbutton.grid(row = 1, column = 1)

output = tk.Text()
output.config(state = "normal", height = 10, width = 20, bg = "#243c6a", fg = "#FFFFFF", 
	font = ("avenir next medium", 11))
output.grid(row = 2)

root.mainloop()