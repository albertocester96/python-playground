import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 
from icecream import ic

#color palette
color_palette = {
    "button_bg": "white",
    "button_fg": "black",
    "primary": "red",
    "secondary": "#F6A884"
}

def carica_file():
    file_path = filedialog.askopenfile()
    if file_path:
        print("File selezioanto: ", file_path)
    else:
        print("Nessun file selezionato")

#creare finestra principale
window = tk.Tk()

#crea frame ttk con un tema
frame = ttk.Frame(window)
frame.pack()

#definizione oggetto style
style = ttk.Style()

#crea stili
style.configure("TButton", background= "white")

#root parameters
window.title("CSV reader")
window.geometry("1280x720")
window.config(background="white")

#crea struttura

#crea testo
#label= tk.Label(frame, text="Clicca il pulsante per cercare il file csv", fg=color_palette["button_fg"], bg= color_palette["button_bg"])

#crea bottone carica file
File_button = ttk.Button(frame, text="Carica file", command= carica_file,style="TButton")


#crea bottone esegui 

#esegui bottoni
#label.pack()
File_button.pack()


#esegui applicazione
window.mainloop()