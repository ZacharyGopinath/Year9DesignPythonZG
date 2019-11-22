import tkinter as tk

root = tk.Tk()
root.Title = "Latin Word Conjugator"

title = tk.Label(text = "Latin Word Conjugator")
title.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
title.grid(row = 0, column = 0, columnspan = 2)

entry1 = tk.Entry()
entry1.config()
entry1.grid(column = 2)

output1 = tk.Text()
output1.config(width = 50, height = 2, state = "disabled", borderwidth = 2,
	relief = "groove")
output1.grid(row = 3, columnspan = 1, column = 0)

output2 = tk.Text()
output2.config(width = 50, height = 2, state = "disabled", borderwidth = 2,
	relief = "groove")
output2.grid(row = 4, column = 0)

output3 = tk.Text()
output3.config(width = 50, height = 10, state = "disabled", borderwidth = 2,
	relief = "groove")
output3.grid(row = 5, column = 0)



output4 = tk.Text()
output4.config(width = 50, height = 2, state = "disabled", borderwidth = 2, 
	relief = "groove")
output4.grid(row = 3, column = 1)

output5 = tk.Text()
output5.config(width = 50, height = 10, state = "disabled", borderwidth = 2, 
	relief = "groove")
output5.grid(row = 4, column = 1)

check = tk.Checkbutton(text = "High Contrast")
check.config(font = ("avenir next medium", 10), anchor = tk.W)
check.grid(row = 7, column = 0, sticky = "W")

root.mainloop()
print("Program Ended")