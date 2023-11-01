import tkinter as tk
import pandas as pd
import subprocess
from icecream import ic
from tkinter import filedialog 

#creare finestra principale
window = tk.Tk()


#root parameters
window.title("CSV reader")
window.geometry("800x500")
filedialog_called = False

#crea testo
label = tk.Label(window, text="CLICCA IL PULSANTE PER CERCARE IL FILE CSV DA ANALIZZARE",  font=("Helvetiva", 16))


#funzione ask apertura file
def carica_file():
    file_path = filedialog.askopenfile()
    if file_path:
        communication(file_path)    
    else:
        print("Nessun file selezionato")

        

#crea bottone carica file
File_button = tk.Button(window, text="Carica file", command= carica_file)


#layout bottoni
label.pack()
File_button.pack()

#crea box
global textbox 
textbox = tk.Text(window, padx=10, pady=10, width=100, height=10)
textbox.pack()



#comunicazione con "back-end"

def communication(path):
    df = pd.read_csv(path, sep=";")
    df.to_csv("Csv_reader/csv_files/dati.csv", index=False)
    file_to_run = "Csv_reader/reader.py"
    process= subprocess.run(["python3", file_to_run, "Csv_reader/csv_files/dati.csv"])

    #read consumi
    df_data = pd.read_csv("Csv_reader/csv_files/consumi_data.csv") #leggi i consumi passati dal back-end

    #crea variaibili per valore consumi
    data_inizio = df_data["Data inizio"].iloc[0]
    data_fine = df_data["Data fine"].iloc[0]
    consumo_totale = df_data["Consumo Totale"].iloc[0]
    consumo_presse = df_data["Consumo presse"].iloc[0]
    strumento_maggiore = df_data["Strumento maggiore"].iloc[0]
    consumo_maggiore = df_data["Consumo maggiore"].iloc[0]
    valori_nulli = df_data["valori nulli"].iloc[0]

    #delete content on textbox
    textbox.delete("1.0", "end")

    textbox.insert("1.0",
            f"Il consumo totale dell'azienda nel periodo {data_inizio} al {data_fine} è stato di {consumo_totale} kwh \n"
            f"Le presse del reparto stampaggio nello stesso periodo hanno consumato {consumo_presse} kwh \n"
            f"Il consumo maggiore è dato da {strumento_maggiore} con il {consumo_maggiore} % sul totale \n"
        )
    if valori_nulli:
        textbox.insert("end",
            f"ATTENZIONE: Ci sono delle macchine che hanno un valore nullo!: {valori_nulli} "
        )
  

#esegui applicazione
window.mainloop()

