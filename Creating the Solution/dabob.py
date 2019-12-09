import tkinter as tk
#Latin Verb Conjugator, asks for 2 inputs (pronoun and verb), then 
#conjugated according to the verb ending

def verb(*args):
	title = tk.Label(text = "Minion fo today")
	title.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
	title.grid(row = 0, column = 0, columnspan = 2)

	img = ImageTK.PhotoImage(Image.open("minion.png"))

	entervbelow = tk.Label(text = "Minion")
	entervbelow.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
	entervbelow.grid(row = 1)

	verbentry = tk.Entry()
	verbentry.config()
	verbentry.grid(row = 2)

	button = tk.Button()
	button.config(bg = "#243c6a", fg = "#FFFFFF", 
	text = "No bob")
	button.grid(row = 4)

	outputm = tk.Text(root)
	outputm.config(state = "normal", font = ("avenir next medium", 11))
	outputm.grid(row = 5)

	outputm.insert(tk.END, img)

	nbutton.after(True, vbutton.destroy)
	vbutton.after(True, vbutton.destroy)
	nbuttonlable.after(vbutton == "True", nbuttonlable.destroy)
	vbuttonlable.after(vbutton == "True", vbuttonlable.destroy)
	nounverb.after(vbutton == "True", nounverb.destroy)
	
def noun(*args):
	title = tk.Label(text = "Da Bob")
	title.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
	title.grid(row = 0, column = 0, columnspan = 2)

	enternbelow = tk.Label(text = "Da bob for today")
	enternbelow.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
	enternbelow.grid(row = 1)

	nounentry = tk.Entry()
	nounentry.config()
	nounentry.grid(row = 2)

	button = tk.Button()
	button.config(bg = "#243c6a", fg = "#FFFFFF", 
	text = "No minion")
	button.grid(row = 4)

	outputm = tk.Text(root)
	outputm.config(state = "normal", font = ("avenir next medium", 11))
	outputm.grid(row = 5)

	nbutton.after(True, vbutton.destroy)
	vbutton.after(True, vbutton.destroy)
	nbuttonlable.after(vbutton == "True", nbuttonlable.destroy)
	vbuttonlable.after(vbutton == "True", vbuttonlable.destroy)
	nounverb.after(vbutton == "True", nounverb.destroy)
	
#GUI
root = tk.Tk()
root.geometry("600x300")
root.Title = "Minion or Da bob"

nounverb = tk.Label(text = "Minion or da bob?")
nounverb.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a", height = 1, width = 40)
nounverb.grid(rowspan = 2, columnspan = 2)

nbuttonlable = tk.Label(text = "Bob")
nbuttonlable.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
nbuttonlable.grid(row = 6, column = 0)

nbutton = tk.Button()
nbutton.config(bg = "#243c6a", command = noun, fg = "#FFFFFF", 
	text = "Bob")
nbutton.grid(row = 7, column = 0)

vbuttonlable = tk.Label(text = "Minion")
vbuttonlable.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
vbuttonlable.grid(row = 6, column = 1)

vbutton = tk.Button()
vbutton.config(bg = "#243c6a", command = verb, fg = "#FFFFFF", 
	text = "Minion")
vbutton.grid(row = 7, column = 1)
root.mainloop()
print("DONE")

