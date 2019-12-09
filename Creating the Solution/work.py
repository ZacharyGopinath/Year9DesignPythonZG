import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#lists of words to try
'''
vAT = ["salutat", "ambulat", "vocat", "rogat", "postulat"]
vET = ["sedet", "habet", "videt", "tinet", "retinet"]
vIT = ["scribit", "surgit", "ducit", "emit", "inquit"]
vIR = ["est", "revenit", "aperit", "offert"]

n1 = ["via","familia", "lingua", "puella", "stella", "terram", "turba"]
n2 = ["coquus", "servus", "dominus", "libertus", "vinum", "portum", "argentarius" ]
n3 = ["mater", "pater", "clamor", "hospes", "dies", "mortem", "omnes"]
'''	
#function for verb GUI
def cverb(*args):
	title = tk.Label(text = "Latin Verb Conjugator")
	title.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a", width = 27)
	title.grid(row = 0, column = 1, columnspan = 2)

	entervbelow = tk.Label(text = "Enter Verb Below")
	entervbelow.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a", width = 15)
	entervbelow.grid(row = 1, column = 1)

	verb = tk.Entry()
	verb.config()
	verb.grid(row = 2, column = 1)
	#function for the actual conjugation
	def verbconjugateat(*args):
		#example -at verbs include ambulat, pugnat, etc. 
		#present
		v1 = verb.get()[0:-2] + "o"
		v2 = verb.get()[0:-1] + "s"
		v3 = verb.get()[0:-1] + "t"
		v4 = verb.get()[0:-1] + "mus"
		v5 = verb.get()[0:-1] + "tis"
		v6 = verb.get()[0:-1] + "nt"
		#perfect
		v11 = verb.get()[0:-1] + "vi"
		v21 = verb.get()[0:-1] + "visti"
		v31 = verb.get()[0:-1] + "vit"
		v41 = verb.get()[0:-1] + "vimus"
		v51 = verb.get()[0:-1] + "vistis"
		v61 = verb.get()[0:-1] + "verunt"
		#imperfect
		v12 = verb.get()[0:-1] + "bam"
		v22 = verb.get()[0:-1] + "bas"
		v32 = verb.get()[0:-1] + "bat"
		v42 = verb.get()[0:-1] + "abamas"
		v52 = verb.get()[0:-1] + "batis"
		v62 = verb.get()[0:-1] + "bant"
		#future
		v13 = verb.get()[0:-1] + "bo"
		v23 = verb.get()[0:-1] + "bis"
		v33 = verb.get()[0:-1] + "bit"
		v43 = verb.get()[0:-1] + "bimus"
		v53 = verb.get()[0:-1] + "betis"
		v63 = verb.get()[0:-1] + "bunt"

		#print verbs into GUI
		output1.insert(tk.END, "1.  " + v1 + "    " + "2.  " + v11 + " " + "3. " + v12 + "    " + "4.  " + v13)
		output2.insert(tk.END, "1.  " + v2 + "    " + "2.  " + v21 + " " + "3. " + v22 + "    " + "4.  " + v23)
		output3.insert(tk.END, "1.  " + v3 + "    " + "2.  " + v31 + " " + "3. " + v32 + "    " + "4.  " + v33)
		output4.insert(tk.END, "1.  " + v4 + "    " + "2.  " + v41 + " " + "3. " + v42 + "   " + "4.  " + v43)
		output5.insert(tk.END, "1.  " + v5 + "    " + "2.  " + v51 + " " + "3. " + v52 + "   " + "4.  " + v53)
		output6.insert(tk.END, "1.  " + v6 + "    " + "2.  " + v61 + " " + "3. " + v62 + "   " + "4.  " + v63)
		sentence.insert(tk.END, "Sample Sentence: Ego" + " " + v11 + ".")
	def verbconjugateit(*args):
		#example -at verbs include ambulat, pugnat, etc. 
		#present
		v1 = verb.get()[0:-2] + "o"
		v2 = verb.get()[0:-2] + "s"
		v3 = verb.get()[0:-2] + "t"
		v4 = verb.get()[0:-2] + "mus"
		v5 = verb.get()[0:-2] + "tis"
		v6 = verb.get()[0:-2] + "nt"
		#perfect
		v11 = verb.get()[0:-2] + "i"
		v21 = verb.get()[0:-2] + "isti"
		v31 = verb.get()[0:-2] + "it"
		v41 = verb.get()[0:-2] + "imus"
		v51 = verb.get()[0:-2] + "istis"
		v61 = verb.get()[0:-2] + "erunt"
		#imperfect
		v12 = verb.get()[0:-2] + "ebam"
		v22 = verb.get()[0:-2] + "ebas"
		v32 = verb.get()[0:-2] + "ebat"
		v42 = verb.get()[0:-2] + "eabamas"
		v52 = verb.get()[0:-2] + "ebatis"
		v62 = verb.get()[0:-2] + "ebant"
		#future
		v13 = verb.get()[0:-1] + "bo"
		v23 = verb.get()[0:-1] + "bis"
		v33 = verb.get()[0:-1] + "bit"
		v43 = verb.get()[0:-1] + "bamus"
		v53 = verb.get()[0:-1] + "batis"
		v63 = verb.get()[0:-1] + "bant"

		#print verbs into GUI
		output1.insert(tk.END, "1.  " + v1 + "    " + "2.  " + v11 + " " + "3. " + v12 + "    " + "4.  " + v13)
		output2.insert(tk.END, "1.  " + v2 + "    " + "2.  " + v21 + " " + "3. " + v22 + "    " + "4.  " + v23)
		output3.insert(tk.END, "1.  " + v3 + "    " + "2.  " + v31 + " " + "3. " + v32 + "    " + "4.  " + v33)
		output4.insert(tk.END, "1.  " + v4 + "    " + "2.  " + v41 + " " + "3. " + v42 + "   " + "4.  " + v43)
		output5.insert(tk.END, "1.  " + v5 + "    " + "2.  " + v51 + " " + "3. " + v52 + "   " + "4.  " + v53)
		output6.insert(tk.END, "1.  " + v6 + "    " + "2.  " + v61 + " " + "3. " + v62 + "   " + "4.  " + v63)
		sentence.insert(tk.END, "Sample Sentence: Ego" + " " + v11 + ".")
	def verbconjugateet(*args):
		#example -at verbs include ambulat, pugnat, etc. 
		#present
		v1 = verb.get()[0:-1] + "o"
		v2 = verb.get()[0:-1] + "s"
		v3 = verb.get()[0:-1] + "t"
		v4 = verb.get()[0:-1] + "mus"
		v5 = verb.get()[0:-1] + "tis"
		v6 = verb.get()[0:-1] + "nt"
		#perfect
		v11 = verb.get()[0:-2] + "ui"
		v21 = verb.get()[0:-2] + "uisti"
		v31 = verb.get()[0:-2] + "uit"
		v41 = verb.get()[0:-2] + "uimus"
		v51 = verb.get()[0:-2] + "uistis"
		v61 = verb.get()[0:-2] + "urunt"
		#imperfect
		v12 = verb.get()[0:-1] + "bam"
		v22 = verb.get()[0:-1] + "bas"
		v32 = verb.get()[0:-1] + "bat"
		v42 = verb.get()[0:-2] + "abamas"
		v52 = verb.get()[0:-1] + "batis"
		v62 = verb.get()[0:-1] + "bant"
		#future
		v13 = verb.get()[0:-1] + "bo"
		v23 = verb.get()[0:-1] + "bis"
		v33 = verb.get()[0:-1] + "bit"
		v43 = verb.get()[0:-1] + "bimus"
		v53 = verb.get()[0:-1] + "betis"
		v63 = verb.get()[0:-1] + "bunt"
		#print verbs into GUI
		output1.insert(tk.END, "1.  " + v1 + "    " + "2.  " + v11 + " " + "3. " + v12 + "    " + "4.  " + v13)
		output2.insert(tk.END, "1.  " + v2 + "    " + "2.  " + v21 + " " + "3. " + v22 + "    " + "4.  " + v23)
		output3.insert(tk.END, "1.  " + v3 + "    " + "2.  " + v31 + " " + "3. " + v32 + "    " + "4.  " + v33)
		output4.insert(tk.END, "1.  " + v4 + "    " + "2.  " + v41 + " " + "3. " + v42 + "   " + "4.  " + v43)
		output5.insert(tk.END, "1.  " + v5 + "    " + "2.  " + v51 + " " + "3. " + v52 + "   " + "4.  " + v53)
		output6.insert(tk.END, "1.  " + v6 + "    " + "2.  " + v61 + " " + "3. " + v62 + "   " + "4.  " + v63)
		sentence.insert(tk.END, "Sample Sentence: Ego" + " " + v11 + ".")

	def verbconjugateir(*args):
		#example -at verbs include ambulat, pugnat, etc. 
		if verb.get() == "est" or "es" or "sum" or "esse":
			#present
			v1 = "sum"
			v2 = "es"
			v3 = "est"
			v4 = "sumus"
			v5 = "estis"
			v6 = "sunt"
			#perfect
			v11 = "fui"
			v21 = "fuisti"
			v31 = "fuit"
			v41 = "fuimus"
			v51 = "fuistis"
			v61 = "fuerunt"
			#imperfect
			v12 = "eram"
			v22 = "eras"
			v32 = "erat"
			v42 = "eramus"
			v52 = "eratis"
			v62 = "erant"
			#future
			v13 = "ero"
			v23 = "eris"
			v33 = "erit"
			v43 = "erimus"
			v53 = "eritis"
			v63 = "erunt"
		#print verbs into GUI
		output1.insert(tk.END, "1.  " + v1 + "    " + "2.  " + v11 + " " + "3. " + v12 + "    " + "4.  " + v13)
		output2.insert(tk.END, "1.  " + v2 + "    " + "2.  " + v21 + " " + "3. " + v22 + "    " + "4.  " + v23)
		output3.insert(tk.END, "1.  " + v3 + "    " + "2.  " + v31 + " " + "3. " + v32 + "    " + "4.  " + v33)
		output4.insert(tk.END, "1.  " + v4 + "    " + "2.  " + v41 + " " + "3. " + v42 + "   " + "4.  " + v43)
		output5.insert(tk.END, "1.  " + v5 + "    " + "2.  " + v51 + " " + "3. " + v52 + "   " + "4.  " + v53)
		output6.insert(tk.END, "1.  " + v6 + "    " + "2.  " + v61 + " " + "3. " + v62 + "   " + "4.  " + v63)
		sentence.insert(tk.END, "Sample Sentence: Ego" + " " + v11 + ".")

	def darkmode(*args):
		label1.config(fg = "#FFFFFF", bg = "#36424d")
		label2.config(fg = "#FFFFFF", bg = "#36424d")
		label3.config(fg = "#FFFFFF", bg = "#36424d")
		label4.config(fg = "#FFFFFF", bg = "#36424d")
		label5.config(fg = "#FFFFFF", bg = "#36424d")
		label6.config(fg = "#FFFFFF", bg = "#36424d")
		output1.config(fg = "#FFFFFF", bg = "#36424d")
		output2.config(fg = "#FFFFFF", bg = "#36424d")
		output3.config(fg = "#FFFFFF", bg = "#36424d")
		output4.config(fg = "#FFFFFF", bg = "#36424d")
		output5.config(fg = "#FFFFFF", bg = "#36424d")
		output6.config(fg = "#FFFFFF", bg = "#36424d")
		entervbelow.config(fg = "#FFFFFF", bg = "#36424d")
		verb.config(fg = "#FFFFFF", bg = "#36424d")
		instructions.config(fg = "#FFFFFF", bg = "#36424d")
		sentence.config(fg = "#FFFFFF", bg = "#36424d")
		buttonat.config(fg = "#36424d", bg = "#FFFFFF")
		buttonet.config(fg = "#36424d", bg = "#FFFFFF")
		buttonit.config(fg = "#36424d", bg = "#FFFFFF")
		darkm.config(fg = "#FFFFFF", bg = "#36424d")
		buttonir.config(fg = "#36424d", bg = "#FFFFFF")
		
		root.config(background = "grey")
	
	#GUI that will appear after choosing verb GUI
	label1 = tk.Label(text = "1 Person   ")
	label2 = tk.Label(text = "2 Person   ")
	label3 = tk.Label(text = "3 Person   ")
	label4 = tk.Label(text = "1 Person P.")
	label5 = tk.Label(text = "2 Person P.")
	label6 = tk.Label(text = "3 Person P.")
	label1.config(fg = "#243c6a", bg = "#FFFFFF", font = ("avenir next medium", 12), width = 15)
	label2.config(fg = "#243c6a", bg = "#FFFFFF", font = ("avenir next medium", 12), width = 15)
	label3.config(fg = "#243c6a", bg = "#FFFFFF", font = ("avenir next medium", 12), width = 15)
	label4.config(fg = "#243c6a", bg = "#FFFFFF", font = ("avenir next medium", 12), width = 15)
	label5.config(fg = "#243c6a", bg = "#FFFFFF", font = ("avenir next medium", 12), width = 15)
	label6.config(fg = "#243c6a", bg = "#FFFFFF", font = ("avenir next medium", 12), width = 15)
	label1.grid(row = 7)
	label2.grid(row = 8)
	label3.grid(row = 9)
	label4.grid(row = 10)
	label5.grid(row = 11)
	label6.grid(row = 12)

	presenttitle = tk.Label(text = "1.Present      2.Perfect      3.Imperfect      4.Future")
	presenttitle.config(bg = "#243c6a", fg = "#FFFFFF", height = 1, width = 40)
	presenttitle.grid(row = 13, column = 1, columnspan = 3)
	
	#output boxes where conjugated forms appear
	output1 = tk.Text()
	output2 = tk.Text()
	output3 = tk.Text()
	output4 = tk.Text()
	output5 = tk.Text()
	output6 = tk.Text()
	output1.config(font = ("avenir next medium", 12),height = 1, width = 50)
	output2.config(font = ("avenir next medium", 12),height = 1, width = 50)
	output3.config(font = ("avenir next medium", 12),height = 1, width = 50)
	output4.config(font = ("avenir next medium", 12),height = 1, width = 50)
	output5.config(font = ("avenir next medium", 12),height = 1, width = 50)
	output6.config(font = ("avenir next medium", 12),height = 1, width = 50)
	output1.grid(row = 7, column = 1)
	output2.grid(row = 8, column = 1)
	output3.grid(row = 9, column = 1)
	output4.grid(row = 10, column = 1)
	output5.grid(row = 11, column = 1)
	output6.grid(row = 12, column = 1)

	buttonat = tk.Button()
	buttonat.config(height = 2, width = 7, command = verbconjugateat, 
		text = "-at Verb", foreground = "blue", background = "grey")
	buttonat.grid(row = 14, column = 0)

	buttonet = tk.Button()
	buttonet.config(height = 2, width = 7, command = verbconjugateet, 
		text = "-et Verb", foreground = "blue", background = "grey")
	buttonet.grid(row = 14, column = 1)

	buttonit = tk.Button()
	buttonit.config(height = 2, width = 7, command = verbconjugateit, 
		text = "-it Verb", foreground = "blue", background = "grey")
	buttonit.grid(row = 14, column = 2)

	buttonir = tk.Button()
	buttonir.config(height = 2, width = 10, command = verbconjugateir,
		text = "Irregular Verb", foreground = "blue", background = "grey")
	buttonir.grid(row = 15, column = 1)

	conjugate = tk.Button()
	if buttonat == True:
		conjugate.config(height = 2, width = 7, command = verbconjugateat, 
		text = "Conjugate", foreground = "blue", background = "grey")
	if buttonet == True:
		conjugate.config(height = 2, width = 7, command = verbconjugateet, 
		text = "Conjugate", foreground = "blue", background = "grey")
	if buttonit == True:
		conjugate.config(height = 2, width = 7, command = verbconjugatit, 
		text = "Conjugate", foreground = "blue", background = "grey")
	conjugate.grid(row = 4, column = 1)

	instructions = tk.Label(text = "Please input verb then select whether it is an -at, -et, or -it verb.")
	instructions.config(font = ("avenir next medium", 12),
		borderwidth = 2, state = "disabled", height = 1, width = 45)
	instructions.grid(row = 16, column = 1)

	sentence = tk.Text()
	sentence.config(font = ("avenir next medium", 12), height = 1, width = 22)
	sentence.grid(row = 17, column = 1)

	darkm = tk.Checkbutton()
	darkm.config(command = darkmode)
	darkm.grid(row = 19)

	nbutton.after(True, nbutton.destroy)
	vbutton.after(True, vbutton.destroy)
	nbuttonlable.after(vbutton == "True", nbuttonlable.destroy)
	vbuttonlable.after(vbutton == "True", vbuttonlable.destroy)
	nounverb.after(vbutton == "True", nounverb.destroy)
	vbutton.after(vbutton == True, panel.destroy)
	vbutton.after(vbutton == True, nouninfo.destroy)
	vbutton.after(vbutton == True, verbinfo.destroy)
#function for noun GUI
def noun(*args):
	title = tk.Label(text = "Latin Noun Conjugator")
	title.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a", width = 27)
	title.grid(row = 0, column = 1, columnspan = 2)

	enternbelow = tk.Label(text = "Enter Noun Below")
	enternbelow.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a", width = 15)
	enternbelow.grid(row = 1, column = 1)

	noun = tk.Entry()
	noun.config()
	noun.grid(row = 2, column = 1)
	#function for the actual conjugation
	def noun1(*args):
		#example noun 1 puella
		#singluar
		v1 = noun.get()
		v2 = noun.get()[0:-1] + "ae"
		v3 = noun.get()[0:-1] + "ae"
		v4 = noun.get()[0:-1] + "am"
		v5 = noun.get()
		v6 = noun.get()
		#plural
		v11 = noun.get()[0:-1] + "ae"
		v21 = noun.get()[0:-1] + "arum"
		v31 = noun.get()[0:-1] + "is"
		v41 = noun.get()[0:-1] + "as"
		v51 = noun.get()[0:-1] + "is"
		v61 = noun.get()[0:-1] + "ae"
		
		#print verbs into GUI
		output1.insert(tk.END, "1.  " + v1 + "    " + "2.  " + v11)
		output2.insert(tk.END, "1.  " + v2 + "    " + "2.  " + v21)
		output3.insert(tk.END, "1.  " + v3 + "    " + "2.  " + v31)
		output4.insert(tk.END, "1.  " + v4 + "    " + "2.  " + v41)
		output5.insert(tk.END, "1.  " + v5 + "    " + "2.  " + v5)
		output6.insert(tk.END, "1.  " + v6 + "    " + "2.  " + v61)
		sentence.insert(tk.END, "Sample Sentence: Illa" + " " + v1 + " " + "est" + ".")
		info.insert(tk.END, "Gender: Feminine")
	def noun2(*args):
		#example noun 2 servus
		#singluar
		v1 = noun.get()
		v2 = noun.get()[0:-1]
		v3 = noun.get()[0:-2] + "o"
		v4 = noun.get()[0:-2] + "um"
		v5 = noun.get()[0:-2] + "o"
		v6 = noun.get()[0:-2] + "e"
		#plural
		v11 = noun.get()[0:-2] + "i"
		v21 = noun.get()[0:-2] + "orum"
		v31 = noun.get()[0:-2] + "is"
		v41 = noun.get()[0:-2] + "os"
		v51 = noun.get()[0:-2] + "is"
		v61 = noun.get()[0:-2] + "i"
		
		#print verbs into GUI
		output1.insert(tk.END, "1.  " + v1 + "    " + "2.  " + v11)
		output2.insert(tk.END, "1.  " + v2 + "    " + "2.  " + v21)
		output3.insert(tk.END, "1.  " + v3 + "    " + "2.  " + v31)
		output4.insert(tk.END, "1.  " + v4 + "    " + "2.  " + v41)
		output5.insert(tk.END, "1.  " + v5 + "    " + "2.  " + v5)
		output6.insert(tk.END, "1.  " + v6 + "    " + "2.  " + v61)
		sentence.insert(tk.END, "Sample Sentence: Ille" + " " + v1 + " " + "est" + ".")
		info.insert(tk.END, "Gender: Masculine")
	def noun3(*args):
		#example noun 3 civis
		#singluar
		v1 = noun.get()
		v2 = noun.get()
		v3 = noun.get()[0:-1]
		v4 = noun.get()[0:-2] + "em"
		v5 = noun.get()[0:-2] + "e"
		v6 = noun.get()
		#plural
		v11 = noun.get()[0:-2] + "es"
		v21 = noun.get()[0:-2] + "ium"
		v31 = noun.get()[0:-2] + "ibus"
		v41 = noun.get()[0:-2] + "es"
		v51 = noun.get()[0:-2] + "ibus"
		v61 = noun.get()[0:-2] + "es"
		
		#print verbs into GUI
		output1.insert(tk.END, "1.  " + v1 + "    " + "2.  " + v11)
		output2.insert(tk.END, "1.  " + v2 + "    " + "2.  " + v21)
		output3.insert(tk.END, "1.  " + v3 + "    " + "2.  " + v31)
		output4.insert(tk.END, "1.  " + v4 + "    " + "2.  " + v41)
		output5.insert(tk.END, "1.  " + v5 + "    " + "2.  " + v5)
		output6.insert(tk.END, "1.  " + v6 + "    " + "2.  " + v61)
		sentence.insert(tk.END, "Sample Sentence: Ille/Illa" + " " + v1 + " " + "est" + ".")
		info.insert(tk.END, "Gender: Masculine/Feminine")
	def darkmode(*args):
		label1.config(fg = "#FFFFFF", bg = "#36424d")
		label2.config(fg = "#FFFFFF", bg = "#36424d")
		label3.config(fg = "#FFFFFF", bg = "#36424d")
		label4.config(fg = "#FFFFFF", bg = "#36424d")
		label5.config(fg = "#FFFFFF", bg = "#36424d")
		label6.config(fg = "#FFFFFF", bg = "#36424d")
		output1.config(fg = "#FFFFFF", bg = "#36424d")
		output2.config(fg = "#FFFFFF", bg = "#36424d")
		output3.config(fg = "#FFFFFF", bg = "#36424d")
		output4.config(fg = "#FFFFFF", bg = "#36424d")
		output5.config(fg = "#FFFFFF", bg = "#36424d")
		output6.config(fg = "#FFFFFF", bg = "#36424d")
		enternbelow.config(fg = "#FFFFFF", bg = "#36424d")
		noun.config(fg = "#FFFFFF", bg = "#36424d")
		instructions.config(fg = "#FFFFFF", bg = "#36424d")
		sentence.config(fg = "#FFFFFF", bg = "#36424d")
		info.config(fg = "#FFFFFF", bg = "#36424d")
		buttona.config(fg = "#36424d", bg = "#FFFFFF")
		buttonus.config(fg = "#36424d", bg = "#FFFFFF")
		darkm.config(fg = "#FFFFFF", bg = "#36424d")
		buttonis.config(fg = "#36424d", bg = "#FFFFFF")
		root.config(background = "grey")
			
	#GUI that will appear after choosing verb GUI
	label1 = tk.Label(text = "Nominative")
	label2 = tk.Label(text = "Genitive")
	label3 = tk.Label(text = "Accusative")
	label4 = tk.Label(text = "Dative")
	label5 = tk.Label(text = "Ablative")
	label6 = tk.Label(text = "Vocative")
	label1.config(fg = "#243c6a", bg = "#FFFFFF", font = ("avenir next medium", 12), width = 15)
	label2.config(fg = "#243c6a", bg = "#FFFFFF", font = ("avenir next medium", 12), width = 15)
	label3.config(fg = "#243c6a", bg = "#FFFFFF", font = ("avenir next medium", 12), width = 15)
	label4.config(fg = "#243c6a", bg = "#FFFFFF", font = ("avenir next medium", 12), width = 15)
	label5.config(fg = "#243c6a", bg = "#FFFFFF", font = ("avenir next medium", 12), width = 15)
	label6.config(fg = "#243c6a", bg = "#FFFFFF", font = ("avenir next medium", 12), width = 15)
	label1.grid(row = 7)
	label2.grid(row = 8)
	label3.grid(row = 9)
	label4.grid(row = 10)
	label5.grid(row = 11)
	label6.grid(row = 12)

	presenttitle = tk.Label(text = "1. Singluar      2.Plural")
	presenttitle.config(font = ("avenir next medium", 15), bg = "#243c6a", fg = "#FFFFFF", height = 1, width = 40)
	presenttitle.grid(row = 13, column = 1, columnspan = 3)
	
	#output boxes where conjugated forms appear
	output1 = tk.Text()
	output2 = tk.Text()
	output3 = tk.Text()
	output4 = tk.Text()
	output5 = tk.Text()
	output6 = tk.Text()
	output1.config(font = ("avenir next medium", 15),height = 1, width = 50)
	output2.config(font = ("avenir next medium", 15),height = 1, width = 50)
	output3.config(font = ("avenir next medium", 15),height = 1, width = 50)
	output4.config(font = ("avenir next medium", 15),height = 1, width = 50)
	output5.config(font = ("avenir next medium", 15),height = 1, width = 50)
	output6.config(font = ("avenir next medium", 15),height = 1, width = 50)
	output1.grid(row = 7, column = 1)
	output2.grid(row = 8, column = 1)
	output3.grid(row = 9, column = 1)
	output4.grid(row = 10, column = 1)
	output5.grid(row = 11, column = 1)
	output6.grid(row = 12, column = 1)

	buttona = tk.Button()
	buttona.config(height = 2, width = 7, command = noun1, 
		text = "Noun 1", foreground = "blue", background = "grey")
	buttona.grid(row = 14, column = 0)

	buttonus = tk.Button()
	buttonus.config(height = 2, width = 7, command = noun2, 
		text = "Noun 2", foreground = "blue", background = "grey")
	buttonus.grid(row = 14, column = 1)

	buttonis = tk.Button()
	buttonis.config(height = 2, width = 7, command = noun3, 
		text = "Noun 3", foreground = "blue", background = "grey")
	buttonis.grid(row = 14, column = 2)

	instructions = tk.Label(text = "Please input nominative noun then click the conjugate button")
	instructions.config(font = ("avenir next medium", 12),
		borderwidth = 2, state = "disabled", height = 1, width = 45)
	instructions.grid(row = 16, column = 1)

	sentence = tk.Text()
	sentence.config(font = ("avenir next medium", 12), height = 1, width = 25)
	sentence.grid(row = 17, column = 1)

	info = tk.Text()
	info.config(font = ("avenir next medium", 12), height = 1, width = 25)
	info.grid(row = 18, column = 1)

	darkm = tk.Checkbutton()
	darkm.config(command = darkmode)
	darkm.grid(row = 19)

	nbutton.after(True, nbutton.destroy)
	vbutton.after(True, vbutton.destroy)
	nbuttonlable.after(vbutton == "True", nbuttonlable.destroy)
	vbuttonlable.after(vbutton == "True", vbuttonlable.destroy)
	nounverb.after(vbutton == "True", nounverb.destroy)
	vbutton.after(vbutton == True, panel.destroy)

	nbutton.after(True, vbutton.destroy)
	vbutton.after(True, vbutton.destroy)
	nbuttonlable.after(vbutton == "True", nbuttonlable.destroy)
	vbuttonlable.after(vbutton == "True", vbuttonlable.destroy)
	nounverb.after(vbutton == "True", nounverb.destroy)
	nbutton.after(vbutton == True, nouninfo.destroy)
	nbutton.after(vbutton == True, verbinfo.destroy)
#asking before closing program
def on_closing():
	print("closing")
	if messagebox.askokcancel("Quit", "Do you want to quit?"):

		root.destroy()


#GUI of main page
root = tk.Tk()
root.geometry("700x500")
root.Title = "Latin Word Conjugator"

nounverb = tk.Label(text = "Noun or Verb?")
nounverb.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a", height = 1, width = 40)
nounverb.grid(rowspan = 2, columnspan = 2)

nbuttonlable = tk.Label(text = "Noun")
nbuttonlable.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
nbuttonlable.grid(row = 6, column = 0)

nbutton = tk.Button()
nbutton.config(bg = "#243c6a", command = noun, fg = "#FFFFFF", 
	text = "Noun")
nbutton.grid(row = 7, column = 0)

vbuttonlable = tk.Label(text = "Verb")
vbuttonlable.config(font = ("avenir next medium", 25), fg = "#FFFFFF", bg = "#243c6a")
vbuttonlable.grid(row = 6, column = 1)

vbutton = tk.Button()
vbutton.config(bg = "#243c6a", command = cverb, fg = "#FFFFFF", 
	text = "Verb")
vbutton.grid(row = 7, column = 1)

nouninfo = tk.Text()
nouninfo.config(font = ("avenir next medium", 12), height = 1, width = 22)
nouninfo.grid(row = 8)
nouninfo.insert(tk.END, "Eg. Villa, Foro, Gladius, Puella.")

verbinfo = tk.Text()
verbinfo.config(font = ("avenir next medium", 12), height = 1, width = 22)
verbinfo.grid(row = 8, column = 1)
verbinfo.insert(tk.END, "Eg. Docet, Pugnat, Legit, Esse.")

img = tk.PhotoImage(file = "julius.png")
panel = tk.Label(root, image = img)
panel.grid(row = 9, column = 0, columnspan = 2)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
print("DONE")

