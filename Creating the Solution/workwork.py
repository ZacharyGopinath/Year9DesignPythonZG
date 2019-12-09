import tkinter as tk
from tkinter import messagebox

vAT = ["salutat", "ambulat", "vocat", "rogat", "postulat"]
vET = ["sedet", "habet", "videt", "tinet", "retinet"]
vIT = ["scribit", "surgit", "ducit", "emit", "inquit"]
vIR = ["est", "revenit", "aperit", "offert"]

n1 = ["via","familia", "lingua", "puella", "stella", "terram", "turba"]
n2 = ["coquus", "servus", "dominus", "libertus", "vinum", "portum", "argentarius" ]
n3 = ["mater", "pater", "clamor", "hospes", "dies", "mortem", "omnes"]

def verbconjugate(*args):
	v1 = verb.get()[0:-1] + "o"
	v2 = verb.get()[0:-1] + "s"
	v3 = verb.get()[0:-1] + "t"
	output1.config()
	output1.insert(tk.END, v1)
	output2.insert(tk.END, v2)
	output3.insert(tk.END, v3)
	print("")
	# if len(verb.get())-2 == "e" and verb not in vIR:
	# 	v1 = verb.get()[0:-2] + "o"
	# 	v2 = verb.get()[0:-2] + "s"
	# 	output1.config(text=verb)
	# 	output1.insert(v1)
	# 	output2.insert(v2)
	# 	print("")
	
		
#use for loop to replace end with verb using list, 
#where you insert list[1] in place of ending

root = tk.Tk()
root.geometry("600x300")
root.Title = "Latin Word Conjugator"

verb = tk.Entry()
verb.config()
verb.grid(row = 0, column = 2)

conjugate = tk.Button()
conjugate.config(height = 4, width = 10, command = verbconjugate, text = "Conjugate")
conjugate.grid(row = 1, column = 2)

output1 = tk.Text()
output1.config(height = 2, width = 7)
output1.grid(row = 0)

output2 = tk.Text()
output2.config(height = 2, width = 7)
output2.grid(row = 1)

output3 = tk.Text()
output3.config(height = 2, width = 7)
output3.grid(row = 2)

output4 = tk.Text()
output4.config(height = 2, width = 7)
output4.grid(row = 3)

root.mainloop()
print("DONE")
