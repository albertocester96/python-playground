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


#creare finestra principale
window = tk.Tk()

#root parameters
window.title("CSV reader")
window.geometry("1280x720")

#comunicazione con "back-end"
def communication(path):
    df = pd.read_csv(path, sep=";")
    df.to_csv("Desktop_app_CSV_anaysis/dati.csv", index=False)
    file_to_run = "Desktop_app_CSV_anaysis/CSV_Analysis.py"
    process= subprocess.run(["python3", file_to_run, "Desktop_app_CSV_anaysis/dati.csv"])

    #read consumi
    df_data = pd.read_csv("Desktop_app_CSV_anaysis/Consumi_data.csv") #leggi i consumi passati dal back-end

    #crea variaibili per valore consumi
    data_inizio = df_data["Data inizio"].iloc[0]
    data_fine = df_data["Data fine"].iloc[0]
    consumo_totale = df_data["Consumo Totale"].iloc[0]
    consumo_presse = df_data["Consumo presse"].iloc[0]
    strumento_maggiore = df_data["Strumento maggiore"].iloc[0]
    consumo_maggiore = df_data["Consumo maggiore"].iloc[0]
    valori_nulli = df_data["valori nulli"].iloc[0]

    
    #crea etichette consumi
    label1= tk.Label(window, text=f"Il consumo totale dell'azienda nel periodo {data_inizio} al {data_fine} è stato di {consumo_totale} kwh") 
    label2= tk.Label(window, text=f"Le presse del reparto stampaggio nello stesso periodo hanno consumato {consumo_presse} kwh")
    label3= tk.Label(window, text=f"Il consumo maggiore è dato da {strumento_maggiore} con il {consumo_maggiore} % sul totale")
    if valori_nulli:
        label4= tk.Label(window,text= f"ATTENZIONE: Ci sono delle macchine che hanno un valore nullo!: {valori_nulli} ")

    #layout etichette
    label1.pack()
    label2.pack()
    label3.pack()
    label4.pack()
    
#funzione ask apertura file
def carica_file():
    file_path = filedialog.askopenfile()
    if file_path:
        print("File selezionato: ", file_path)
        communication(file_path)
    else:
        print("Nessun file selezionato")
   

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

