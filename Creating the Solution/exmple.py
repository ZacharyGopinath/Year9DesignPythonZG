from tkinter import *

root = Tk()
root.geometry('300x100')

class App(object):
     def __init__(self,root):
         self.root = root
         self.txt_frm = Frame(self.root, width=900, height=900, bg='khaki')
         self.txt_frm.pack(fill="both", expand=True)
         entry1 = Entry(self.txt_frm, text = "Pronoun")
         entry1.grid(column=0,row=2, padx=2, pady=2)
         entry2 = Entry(self.txt_frm, text = "Verb")
         entry2.grid(column=1,row=2, padx=2, pady=2)
         button = Button(self.txt_frm, text = "Click to Conjugate", command = conjugate)
         button.grid(column=1, row=3, padx=2, pady=2)
         output = Text(self.txt_frm)
         output.grid(column = 1, row = 4, padx = 2, pady=2)
         self.entry_var = StringVar()
         entry = Entry(self.txt_frm, textvariable=self.entry_var)
         entry.grid(column=0, row=3, columnspan=2, padx=2, pady=2)
      def conjugate(self):
         if pronoun == "ego" and verb == "docet":
          output.insert("Ego" + " " + "doceo")

app = App(root)
root.mainloop()
