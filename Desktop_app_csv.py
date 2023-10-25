import tkinter as tk
from tkinter import filedialog 

def carica_file():
    file_path = filedialog.askopenfile()
    if file_path:
        print("File selezioanto: ", file_path)
    else:
        print("Nessun file selezionato")

#creare finestra principale
window = tk.Tk()

#root parameters
window.title("CSV reader")
window.geometry("1280x720")
window.config(background="white")


#crea bottone carica file
File_button = tk.Button(window, text="Carica file", command= carica_file())


#crea bottone esegui 

#esegui bottoni
File_button.pack()


#esegui applicazione
window.mainloop()