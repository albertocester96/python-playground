#Questo script ha l'obiettivo di analizzare i dati CSV per fare delle somme, medie o ricercare valori specifici


#import libraies
import pandas as pd
from icecream import ic
import math 
import sys

file_name = sys.argv[1]

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
df['strumento'] = df['strumento'].apply(lambda words: "".join(words[:words.index("Energia")])) #estrai le parole dall'indice 0 a la parola "Energia"


#trova valore strumento maggiore
valore_maggiore = df['percentuale'].max()
index = df['percentuale'].idxmax()
strumento_maggiore = df.at[index, 'strumento']

#notifica valori a 0
valori_nulli = df[df["valore"]==0]
index_null = valori_nulli.index
strumenti_nulli = df.loc[index_null, 'strumento']

#print
print("L'azienda nel periodo dal " + data_inizio + " al " + data_fine + " ha consumato " + str(consumo_totale) +  " kWh")
print("Le presse del reparto stampaggio nello stesso periodo hanno consumato " + str(somma_presse) + " kWh")
print("Il consumo maggiore e dato da " + strumento_maggiore + "con il " + str(valore_maggiore) +  " percentuale sul totale")

if not valori_nulli.empty: #check if valori nulli is empty
    for strumento in strumenti_nulli:
        print("ATTENZIONE!: esistono dei valori a 0 da controllare. Sono i seguenti: " + strumento)
    
ic(df.sort_values(by="valore", ascending=False))

