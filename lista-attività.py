def check_empty(lista):
    if not lista:
        print ("La tua lista è vuota")
     
def aggiungi_attività(lista):
    attività_utente= input("Quale attività vuoi ricordare?: ")

    if attività_utente != "": 
        lista.append(attività_utente)
        print("La tua lista è: ", lista)

    else:
        print("Non hai inserito nessuna attività, prova a scrivere qualcosa")
        aggiungi_attività(lista)
        
    return lista

def rimuovi_attività (lista):
    check_empty(lista)
    attività_da_rimuovere = input ("Quale attività vuoi rimuovere?: ")
    lista.remove(attività_da_rimuovere)
    print("Hai rimosso l'attività: "+ attività_da_rimuovere, ". La tua lista è " + lista)
    
    if not check_empty(lista):
        print(lista)

def domanda(lista):
    
    aggiungi_attività(lista)
    
    altro = input("Vuoi aggiungere altro? [Enter: si/no:]: ")
       
    if altro.lower() == "si":
        check_empty(lista)
        domanda(lista)
    else: 
        print("La tua lista è: ", lista)
        rimuovi = input(". Vuoi rimuovere qualche attività?[si/no] ")
            
        if rimuovi.lower() == "si":
            rimuovi_attività(lista)
        elif rimuovi.lower() == "no":
            exit
    
    

lista_attività = [] 
domanda(lista_attività)