import sys

tipo_calcolo = input("Che tipo di operazione vuoi fare? Somma(1) - sottrazione(2) - moltiplicazione(3) - divisione(4) ")

tipologie = {"sommare" : 1, "sottrarre": 2, "moltiplicare": 3, "dividere": 4}

def check_iniziale (chiave):

    while True:
        valore_ini= input("Qual è il primo valore che vuoi " + chiave + "?: ")
    
        return valore_ini
        
    
def check_finale(chiave):

    while True:
        valore_fin= input("Qual è il secondo valore che vuoi " + chiave + "?: ")
    
        return valore_fin

        
def check_null(valore):

    if valore== "":
        try: 
            print("Non hai inserito nessun valore") 
            exit_program()
        except ValueError:
            print("Il valore inserito non è valido")
            exit_program()
        return False
    
def exit_program():
    print("Sto uscendo dal programma...")
    exit()
   
try: 
    if int(tipo_calcolo) == int(tipologie["sommare"]):
        valore_iniziale = check_iniziale("sommare")
        check_null(valore_iniziale)
        valore_finale = check_finale("sommare")
        check_null(valore_finale)

        if (valore_iniziale.isnumeric() & valore_finale.isnumeric()):
            risultato = int(valore_iniziale) + int(valore_finale)
            print(f"Il risultato della somma è: ", risultato)

    elif int(tipo_calcolo) == int(tipologie["sottrarre"]):
        check_iniziale()

except ValueError:

    try_int = int(tipo_calcolo)

    if int(try_int) == ValueError:
        print("Il valore non")
    else: 
        print("Non hai inserito nessun valore")  