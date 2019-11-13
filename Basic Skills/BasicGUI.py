import tkinter as tk

print("Start Program")
root = tk.Tk() #This builds your window

btn1 = tk.Button(root)
btn1.config(text = "I am a button", width = 100, height = 3)
btn1.pack(fill = tk.BOTH)

output = tk.Text(root, width = 100, height = 20)
output.config()
output.pack(fill = tk.BOTH)


check  = tk.Checkbutton(root, text = "<-- Click Here to Make Checkmark Appear")
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)

root.mainloop()
print("END PROGRAM")
