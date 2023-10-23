
tipo_calcolo = input("Che tipo di operazione vuoi fare? Somma(1) - sottrazione(2) - moltiplicazione(3) - divisione(4) ")

dizionarioOperazioni = {1: "somma", 2: "sottrazione", 3: "moltiplicazione", 4: "divisione"}

def check_iniziale (operazione):

    while True:
        valore_ini= input("Qual è il primo valore per cui fare la " + operazione + "?: ")
    
        return valore_ini
        
    
def check_finale(operazione):

    while True:
        valore_fin= input("Qual è il secondo valore per cui fare la " + operazione + "?: ")
    
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
            
        elif (int(tipo_calcolo) == 2):
            risultato = int(valore_iniziale) - int(valore_finale)

        elif (int(tipo_calcolo) == 3):
            risultato = int(valore_iniziale) * int(valore_finale)

        elif (int(tipo_calcolo) == 4):
            risultato = int(valore_iniziale) / int(valore_finale)
            
    
        print(f"Il risultato della {operazione} è: {risultato}")

    else:
        print("Il calcolo non è andato a buon fine")


if not tipo_calcolo.isnumeric() or int(tipo_calcolo) > 4:
            print("Hai inserito un valore non supportato, riprova")

else: 
    calcolo(dizionarioOperazioni, tipo_calcolo)

