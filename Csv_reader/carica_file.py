'''
La funzione carica_file da la possibilità all'utente di aprire una finestra di dialogo per scegliere il file tramite 'filedialog' da tkinter.
Se il path viene scelto correttamente, la funzione 'communication' viene eseguita
'''


from tkinter import filedialog 

from main_front import communication

#funzione ask apertura file
def carica_file():
    file_path = filedialog.askopenfile()
    if file_path:
        print("File selezionato: ", file_path)
        communication(file_path)
    else:
        print("Nessun file selezionato")