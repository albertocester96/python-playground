import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 
from icecream import ic
import pandas as pd
import subprocess

#color palette
color_palette = {
    "button_bg": "white",
    "button_fg": "black",
    "primary": "red",
    "secondary": "#F6A884"
}

#crea il dataframe dei valori all'interno del csv
def crea_dataframe(path):
    df = pd.read_csv(path, sep=";")
    df.to_csv("dati.csv", index=False)
    file_to_run = "CSV_Analysis.py"
    process= subprocess.run(["python3", file_to_run, "dati.csv"])


#funzione ask apertura file
def carica_file():
    file_path = filedialog.askopenfile()
    if file_path:
        print("File selezioanto: ", file_path)
        crea_dataframe(file_path)
    else:
        print("Nessun file selezionato")

#creare finestra principale
window = tk.Tk()

'''
crea frame ttk con un tema
frame = ttk.Frame(window)
frame.pack()

definizione oggetto style
style = ttk.Style()

crea stili
style.configure("TButton", background= "white")
'''

#root parameters
window.title("CSV reader")
window.geometry("400x50")
#window.config(background="white")

#crea testo
label= tk.Label(window, text="Clicca il pulsante per cercare il file csv")

#crea bottone carica file
File_button = tk.Button(window, text="Carica file", command= carica_file)



#esegui bottoni
label.pack()
File_button.pack()


#esegui applicazione
window.mainloop()

