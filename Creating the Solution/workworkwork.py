import tkinter as tk
from tkinter import messagebox
import os

vAT = ["salutat", "ambulat", "vocat", "rogat", "postulat"]
vET = ["sedet", "habet", "videt", "tinet", "retinet"]
vIT = ["scribit", "surgit", "ducit", "emit", "inquit"]
vIR = ["est", "revenit", "aperit", "offert"]

n1 = ["via","familia", "lingua", "puella", "stella", "terram", "turba"]
n2 = ["coquus", "servus", "dominus", "libertus", "vinum", "portum", "argentarius" ]
n3 = ["mater", "pater", "clamor", "hospes", "dies", "mortem", "omnes"]


#Latin Verb Conjugator, asks for 2 inputs (pronoun and verb), then 
#conjugated according to the verb ending
def verbconjugate(*args):
	v1 = verb.get()[0:-2] + "eo"
	v2 = verb.get()[0:-2] + "es"
	v3 = verb.get()[0:-2] + "et"
	output1.config()
	output1.insert(tk.END, v1)
	output2.insert(tk.END, v2)
	output3.insert(tk.END, v3)

def verb(*args):
	title = tk.Label(text = "Latin Verb Conjugator")
	title.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
	title.grid(row = 0, column = 0, columnspan = 2)

	entervbelow = tk.Label(text = "Enter Verb Below")
	entervbelow.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
	entervbelow.grid(row = 1, column = 0)

	verb = tk.Entry()
	verb.config()
	verb.grid(row = 2, column = 0)

	button = tk.Button()
	button.config(bg = "#243c6a", fg = "#FFFFFF", 
	text = "Search", command = verbconjugate)
	button.grid(row = 4, column =0)

	output1 = tk.Text()
	output1.config(height = 2, width = 7)
	output1.grid(row = 5)

	output2 = tk.Text()
	output2.config(height = 2, width = 7)
	output2.grid(row = 6)

	output3 = tk.Text()
	output3.config(height = 2, width = 7)
	output3.grid(row = 7)

	output4 = tk.Text()
	output4.config(height = 2, width = 7)
	output4.grid(row = 8)

	nbutton.after(True, nbutton.destroy)
	vbutton.after(True, vbutton.destroy)
	nbuttonlable.after(vbutton == "True", nbuttonlable.destroy)
	vbuttonlable.after(vbutton == "True", vbuttonlable.destroy)
	nounverb.after(vbutton == "True", nounverb.destroy)
	vbutton.after(vbutton == True, canvas.destroy)


def noun(*args):
	title = tk.Label(text = "Latin Noun Conjugator")
	title.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
	title.grid(row = 0, column = 0, columnspan = 2)

	enternbelow = tk.Label(text = "Enter Noun Below")
	enternbelow.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
	enternbelow.grid(row = 1)

	nounentry = tk.Entry()
	nounentry.config()
	nounentry.grid(row = 2)

	button = tk.Button()
	button.config(bg = "#243c6a", fg = "#FFFFFF", 
	text = "Search", command = "Search")
	button.grid(row = 4)

	outputm = tk.Text(root)
	outputm.config(state = "normal", font = ("avenir next medium", 11))
	outputm.grid(row = 5)

	nbutton.after(True, vbutton.destroy)
	vbutton.after(True, vbutton.destroy)
	nbuttonlable.after(vbutton == "True", nbuttonlable.destroy)
	vbuttonlable.after(vbutton == "True", vbuttonlable.destroy)
	nounverb.after(vbutton == "True", nounverb.destroy)
	
def on_closing():
	print("closing")
	if messagebox.askokcancel("Quit", "Do you want to quit"):

		root.destroy()


#GUI
root = tk.Tk()
root.geometry("600x400")
root.Title = "Latin Word Conjugator"

nounverb = tk.Label(text = "Noun or Verb?")
nounverb.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a", height = 1, width = 40)
nounverb.grid(rowspan = 2, columnspan = 2)

nbuttonlable = tk.Label(text = "Noun")
nbuttonlable.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
nbuttonlable.grid(row = 6, column = 0)

nbutton = tk.Button()
nbutton.config(bg = "#243c6a", command = noun, fg = "#FFFFFF", 
	text = "Noun")
nbutton.grid(row = 7, column = 0)

vbuttonlable = tk.Label(text = "Verb")
vbuttonlable.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
vbuttonlable.grid(row = 6, column = 1)

vbutton = tk.Button()
vbutton.config(bg = "#243c6a", command = verb, fg = "#FFFFFF", 
	text = "Verb")
vbutton.grid(row = 7, column = 1)

canvas = tk.Canvas()
canvas.config()
canvas.grid(row = 8)
img = tk.PhotoImage(file = "julius.png", height = 300, width = 450)
canvas.create_image(50, 50, image = img)


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
print("DONE")

canvas = tk.Canvas()
canvas.config()
canvas.grid(row = 15, columnspan = 8, rowspan = 1)
img = tk.PhotoImage(file = "julius.png", height = 400, width = 300)
canvas.create_image(50, 50, image = img)

