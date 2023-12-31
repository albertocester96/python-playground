#Questo script ha l'obiettivo di analizzare i dati CSV per fare delle somme, medie o ricercare valori specifici


#import libraies
import pandas as pd
from icecream import ic
import math 
import sys
import subprocess

file_name = sys.argv[1]

#df = pd.read_csv("Desktop_app_CSV_anaysis/files/dolphin_insight_23102023_1756.csv",  sep=";")
df = pd.read_csv(file_name)

header = df.columns #header del file

#cambio "," su valori numerici con "." Converti in float e applica arrotondamento
df['valore']= df['valore'].str.replace(",",".").astype(float).apply(math.ceil) 

#inizializzazione e filtri
data_inizio= df.at[0, 'data inizio']
data_fine= df.at[0, 'data_fine']
ls_presse = df['strumento'].str.contains("Pressa",case= False) #filtro per parola "Pressa"
ls_espansori = df['strumento'].str.contains("Espansori", case= False)#filtro per parola "Espansori"


presse = df.loc[ls_presse] 
espansori = df.loc[ls_espansori]

#calcola i vari consumi
consumo_totale = df['valore'].astype(float).apply(math.ceil).sum() #somma valori nella colonna 'valore' per restituite somma: consumo totale periodo
somma_presse = presse['valore'].astype(float).apply(math.ceil).sum() #somma valori presse e arrotonda per eccesso

#aggiungi e calcola la colonna %
df['percentuale'] =  df['valore'].astype(float)/ consumo_totale * 100
df['percentuale'] = df['percentuale'].apply(lambda x: round(x, 1))


#extract strumento 
df['strumento'] = df['strumento'].apply(lambda words: "".join(words[:words.index(" Energia")])) #estrai le parole dall'indice 0 a la parola "Energia"


#trova valore strumento maggiore

valore_maggiore = df['percentuale'].max()
valore_maggiore_perc = df['percentuale'].apply(lambda x: "{:.0f}%".format(x))


ic(valore_maggiore)
index = df['percentuale'].idxmax()
strumento_maggiore = df.at[index, 'strumento']

#notifica valori a 0
valori_nulli = df[df["valore"]==0]
index_null = valori_nulli.index
strumenti_nulli = df.loc[index_null, 'strumento']

if not valori_nulli.empty: #check if valori nulli is empty
    for strumento in strumenti_nulli:
        strumenti_nulli  = strumento
    
#dati da passare 
dati_da_passare = {
    "Data inizio": data_inizio,
    "Data fine": data_fine,
    "Consumo Totale": consumo_totale,
    "Consumo presse": somma_presse,
    "Strumento maggiore": strumento_maggiore,
    "Consumo maggiore": valore_maggiore,
    "valori nulli": strumento
}

index = ["dd/mm/yyyy 00:00"]

#comunicazione con Desktop_app
df_data = pd.DataFrame(dati_da_passare, index= index)
ic()
df_data.to_csv("Csv_reader/csv_files/consumi_data.csv", index=False)


ic(df.sort_values(by="valore", ascending=False))

