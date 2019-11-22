import tkinter as tk

root = tk.Tk()

title = tk.Label(text = "Latin Word Conjugator")
title.grid(row = 0, column = 0)

entry1 = tk.Entry(text = "Enter Pronoun")
entry1.grid(row = 1, column = 1)

output = tk.Text(root) 
output.config(width = 100, height = 20, state = "disabled", borderwidth = 2)
output.grid(rowspan = 1, column = 2)

check = tk.Checkbutton(text = "Hight Contrast")
check.grid(row = 3, column = 0)
root.mainloop()
print("End Program")