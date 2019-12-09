import tkinter as tk
import tkinter.simpledialog as sd

#Latin Verb Conjugator, asks for 2 inputs (pronoun and verb), then 
#conjugated according to the verb ending

my_dict = {
    1: {'Header1': 'Row1_Value1', 'Header2': 'Row1_Value2', 'Header3': 'Row1_Value3', },
    2: {'Header1': 'Row2_Value1', 'Header2': 'Row2_Value2', 'Header3': 'Row2_Value3', },
    }

def getuserinput(*args):
	getuserinput = sd.askstring("Get User Input", "What is the Verb?")
	if getuserinput[-2] == "a":
		my_dict[1].replace(tk.END, getuserinput[0:-2] + "o")
		my_dict[2].replace(tk.END, getuserinput[0:-2] + "as")
		my_dict[3].replace(tk.END, getuserinput[0:-2] + "at")
	
#GUI
root = tk.Tk()
root.geometry("600x300")
root.Title = "Latin Word Conjugator"

title = tk.Label(text = "Verb Forms")
title.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
title.grid(row = 0, column = 3, columnspan = 2)

button = tk.Button()
button.config(bg = "#243c6a", command = getuserinput, fg = "#FFFFFF", 
	text = "Enter Verb")
button.grid(row = 5, column = 3)

# Create the header
for column, header in enumerate(my_dict[1]):
    tk.Label(text="header").grid(row=0, column=0+column)

# Fill in the values
for row, element in enumerate(my_dict.values()):
    for column, (header, value) in enumerate(element.items()):
        tk.Label(text="value").grid(row=1+row, column=0+column)

root.mainloop()
print("DONE")

