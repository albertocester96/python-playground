
tipo_calcolo = input("Che tipo di operazione vuoi fare? Somma(1) - sottrazione(2) - moltiplicazione(3) - divisione(4) ")

# tipologie = {"sommare" : 1, "sottrarre": 2, "moltiplicare": 3, "dividere": 4}
dizionarioOperazioni = {1: "sommare", 2: "sottrarre", 3: "moltiplicare", 4: "dividere"}

def check_iniziale (operazione):

    while True:
        valore_ini= input("Qual è il primo valore che vuoi " + operazione + "?: ")
    
        return valore_ini
        
    
def check_finale(operazione):

    while True:
        valore_fin= input("Qual è il secondo valore che vuoi " + operazione + "?: ")
    
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
   
def calcolo(dizionario, tipo_calcolo):
    operazione  = dizionario[int(tipo_calcolo)]
    
    valore_iniziale = check_iniziale(operazione)
    check_null(valore_iniziale)
    valore_finale = check_finale(operazione)
    check_null(valore_finale)

    if (valore_iniziale.isnumeric() & valore_finale.isnumeric()):
        if (int(tipo_calcolo) == 1):
            risultato = int(valore_iniziale) + int(valore_finale)
    
        print(f"Il risultato della {operazione} è: {risultato}")
    else:
        print("regno e'")

def calcolo2 (operazione, tipo_calcolo):

    try: 
        if int(tipo_calcolo) == int(operazione[1]):
            valore_iniziale = check_iniziale(operazione)
            check_null(valore_iniziale)
            valore_finale = check_finale(operazione)
            check_null(valore_finale)

            if (valore_iniziale.isnumeric() & valore_finale.isnumeric()):
                risultato = int(valore_iniziale) + int(valore_finale)
                print(f"Il risultato della somma è: ", risultato)

        elif int(tipo_calcolo) == int(tipologie["sottrarre"]):
            valore_iniziale = check_iniziale("sottrarre")
            check_null(valore_iniziale)
            valore_finale = check_finale("sottrarre")
            check_null(valore_finale)

            if (valore_iniziale.isnumeric() & valore_finale.isnumeric()):
                risultato = int(valore_iniziale) - int(valore_finale)
                print(f"Il risultato della sottrazione è: ", risultato)

        elif int(tipo_calcolo) == int(tipologie["moltiplicare"]):
            valore_iniziale = check_iniziale("moltiplicare")
            check_null(valore_iniziale)
            valore_finale = check_finale("moltiplicare")
            check_null(valore_finale)

            if (valore_iniziale.isnumeric() & valore_finale.isnumeric()):
                risultato = int(valore_iniziale) * int(valore_finale)
                print(f"Il risultato della moltiplicazione è: ", risultato)

    except ValueError:

        try_int = int(tipo_calcolo)

        if int(try_int) == ValueError:
            print("Il valore non")
        else: 
            print("Non hai inserito nessun valore")  


calcolo(dizionarioOperazioni, tipo_calcolo)
