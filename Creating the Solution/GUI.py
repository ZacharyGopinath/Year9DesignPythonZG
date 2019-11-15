import tkinter as tk

root = tk.Tk()

title = tk.Label(text = "Latin Word Conjugator")
title.grid(row = 0, column = 0)

entry1 = tk.Entry(text = "Enter Pronoun")
entry1.grid(row = 1, column = 1)

output = tk.Text(root) 
output.config(width = 200, height = 40, state = "disabled", borderwidth = 2)
output.grid(rowspan = 1, sticky =S)

check = tk.Checkbutton(text = "Hight Contrast")
check.grid(row = 3, sticky =W)
grid.mainloop()
print("End Program")