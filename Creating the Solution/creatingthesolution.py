import tkinter as tk

root = tk.Tk()

title = tk.Label(root, text = "Latin Word Conjugator")
title.config(fg = "#FFFFFF", bg = "#243c6a")
title.pack(fill = tk.BOTH)

entry1 = tk.Entry(root, text = "Enter Pronoun")
entry1.config()
entry1.pack(side = "top")

output = tk.Text(root)
output.config(width = 50, height = 10, state = "disabled", borderwidth = 2,
	relief = "groove")
output.pack()

check = tk.Checkbutton(root, text = "High Contrast")
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)

root.mainloop()
print("End Program")