#Questo script ha l'obiettivo di analizzare i dati CSV per fare delle somme, medie o ricercare valori specifici


import pandas as pd
from icecream import ic
import math 

df = pd.read_csv("files/dolphin_insight_23102023_1756.csv", sep=";")

header = df.columns #header del file

df['valore']= df['valore'].str.replace(",",".").astype(float).apply(math.ceil) #cambio "," su valori numerici con "." Converti in float e applica arrotondamento

data_inizio= df.at[0, 'data inizio']
data_fine= df.at[0, 'data_fine']
ls_presse = df['strumento'].str.contains("Pressa",case= False) #filtro per parola "Pressa"
ls_espansori = df['strumento'].str.contains("Espansori", case= False)#filtro per parola "Espansori"


presse = df.loc[ls_presse] 
espansori = df.loc[ls_espansori]

ic(presse)
ic(df)

consumo_totale = df['valore'].astype(float).apply(math.ceil).sum() #somma valori nella colonna 'valore' per restituite somma: consumo totale periodo
somma_presse = presse['valore'].astype(float).apply(math.ceil).sum() #somma valori presse e arrotonda per eccesso

print("L'azienda nel periodo dal " + data_inizio + " al " + data_fine + "ha consumato " + str(consumo_totale) +  " kWh")
print("Le presse del reparto stampaggio nello stesso periodo hanno consumato " + str(somma_presse) + " kWh")

