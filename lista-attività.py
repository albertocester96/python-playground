def aggiungi_attività(attività, lista):
    lista.append(attività)
    return lista

def domanda():
    lista_attività = []
    attività_utente= input("Quali attività vuoi ricordare?: ")

    if attività_utente != "": 
        aggiungi_attività(attività_utente, lista_attività)
        print(lista_attività)
        altro = input("Vuoi aggiungere altro?: ")

        if altro.lower() == "si":
            domanda()
        else: 
            exit
    else:
        print("Non hai indicato nessun valore, riprova")
        domanda()
    return attività_utente
    
domanda()
