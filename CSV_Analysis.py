#Questo script ha l'obiettivo di analizzare i dati CSV per fare delle somme, medie o ricercare valori specifici


import pandas as pd
from icecream import ic 

df = pd.read_csv("files/dolphin_insight_23102023_1756.csv", sep=";")

header = df.columns #header del file

colonna_strumento = df['valore']
lista_presse=[]

for riga in df.loc[df['strumento'].str.contains('Pressa', case=False)['strumeto']]:
    lista_presse.append(riga)
    

ic(lista_presse)