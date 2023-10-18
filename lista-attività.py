def aggiungi_attività(attività, lista):
    lista.append(attività)
    return lista

def domanda(lista):
    
    attività_utente= input("Quale attività vuoi ricordare?: ")

    if attività_utente != "": 
        aggiungi_attività(attività_utente, lista)
        print(lista)
        altro = input("Vuoi aggiungere altro? [Enter: si/no:]: ")
       
        if altro.lower() == "si":
            domanda(lista)
        else: 
            exit
    else:
        print("Non hai indicato nessun valore, riprova")
        domanda(lista)
    return lista

lista_attività = [] 
domanda(lista_attività)