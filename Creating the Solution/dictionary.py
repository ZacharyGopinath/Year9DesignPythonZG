from tkinter import *

root = Tk()
root.title = "Dictionary"

my_dict = {
    1: {' ': ' ', ' ': 'Row1_Value2', 'Header3': 'Row1_Value3', },
    2: {'Header1': 'Row2_Value1', 'Header2': 'Row2_Value2', 'Header3': 'Row2_Value3', },

    }

def GO(*args):
	if int(imput)[-2] == "a":
		my_dict[0].insert(str(imput-2) + "o")

# Create the header
for column, header in enumerate(my_dict[1]):
    Label(text=header).grid(row=0, column=0+column)

# Fill in the values
for row, element in enumerate(my_dict.values()):
    for column, (header, value) in enumerate(element.items()):
        Label(text=value).grid(row=1+row, column=0+column)

imput = input()
imput.config(state = "normal", height = 4, width = 10, borderwidth = 2)
imput.grid(row = 3)

btn = Button()
btn.config(height = 5, width = 5, bg = "#243c6a", fg = "#FFFFFF", command = GO, borderwidth = 3)
btn.grid(row = 4, columnspan = 3)


root.mainloop()