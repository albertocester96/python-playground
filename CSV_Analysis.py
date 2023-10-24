#Questo script ha l'obiettivo di analizzare i dati CSV per fare delle somme, medie o ricercare valori specifici


import pandas as pd
from icecream import ic
import math 

df = pd.read_csv("files/dolphin_insight_23102023_1756.csv", sep=";")

header = df.columns #header del file
ic(header)

presse = df['strumento'].str.contains("Pressa",case= False)
valori_presse = df.loc[presse]

ic(valori_presse)

valori_presse['valore']= valori_presse['valore'].str.replace(',', '.')

media_presse = valori_presse['valore'].astype(float).sum()
media_presse= math.ceil(media_presse)
ic(media_presse)