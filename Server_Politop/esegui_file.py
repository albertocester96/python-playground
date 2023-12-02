
import pandas as pd
import subprocess

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
    consumo_compressori = df_data["Consumo compressori"].iloc[0]

    data_to_send = {
        "data_inizio": str(data_inizio),
        "data_fine": str(data_fine),
        "consumo_totale": float(consumo_totale),
        "consumo_presse": int(consumo_presse),
        "strumento_maggiore": str(strumento_maggiore),
        "consumo_maggiore": float(consumo_maggiore),
        "valori_nulli": str(valori_nulli),
        "consumo_compressori": float(consumo_compressori)
    }

    return data_to_send