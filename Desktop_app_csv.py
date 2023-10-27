import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 
from icecream import ic
import pandas as pd
import subprocess
import json


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

#root parameters
window.title("CSV reader")
window.geometry("400x100")

#leggi dati json 
with open("risultati.json", "r") as file:
    dati_da_passare = json.load(file)


#crea testo
label= tk.Label(window, text="Clicca il pulsante per cercare il file csv")
label1 = tk.Label(window, text=dati_da_passare["Consumo Totale"])

#crea bottone carica file
File_button = tk.Button(window, text="Carica file", command= carica_file)

#layout bottoni
label.pack()
File_button.pack()
label1.pack()


#esegui applicazione
window.mainloop()

