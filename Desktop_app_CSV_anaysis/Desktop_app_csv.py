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

#comunicazione con "back-end"
def communication(path):
    df = pd.read_csv(path, sep=";")
    df.to_csv("Desktop_app_CSV_anaysis/dati.csv", index=False)
    file_to_run = "Desktop_app_CSV_anaysis/CSV_Analysis.py"
    process= subprocess.run(["python3", file_to_run, "Desktop_app_CSV_anaysis/dati.csv"])

    #read consumi
    df_data = pd.read_csv("Desktop_app_CSV_anaysis/Consumi_data.csv") #leggi i consumi passati dal back-end
    label1= tk.Label(window, text=df_data["Consumo Totale"]) #configura testo etichetta
    label1.pack()

#funzione ask apertura file
def carica_file():
    file_path = filedialog.askopenfile()
    if file_path:
        print("File selezionato: ", file_path)
        communication(file_path)
    else:
        print("Nessun file selezionato")
   

#creare finestra principale
window = tk.Tk()

#root parameters
window.title("CSV reader")
window.geometry("400x100")

#crea testo
label= tk.Label(window, text="Clicca il pulsante per cercare il file csv")
#label1 = tk.Label(window, text="")

#crea bottone carica file
File_button = tk.Button(window, text="Carica file", command= carica_file)

#layout bottoni
label.pack()
File_button.pack()



#esegui applicazione
window.mainloop()

