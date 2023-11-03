import tkinter as tk
from icecream import ic

from http_request import get_response

#inizializza finestra
window = tk.Tk()
window.title("Converter")
window.geometry("500x200")


currencies = []

ic(get_response)

#crea entry form
entry = tk.Entry(window)
entry.pack()

#converti il valore inserito con la valuta scelta
def Converter(currency_value,input_value):
        input_value = str(input_value.get())
        
        float_value = is_float(input_value) #check se il valore è float

        if float_value: 
                input_value = float(input_value)
                ic(input_value)
                new_value = input_value * currency_value #formula di conversione
                return new_value 
        else:
            l_result.config(text="Non hai inserito un valore valido da convertire! \n Prova ad inserire un numero o cambiare la virgola con un punto")

#verifica se il valore è float
def is_float(value):
    try:
        value = float(value)
        return value
    except:
        return False

#mostra il risultato della conversione
def show_result():
    result = Converter(currencies["dollar"],entry)
    l_result.config(text=result)

#crea bottone per conversione
converter_button = tk.Button(window, text="Converti", command=show_result)
converter_button.pack()

#crea label vuota per risultati
l_result = tk.Label(window, text="")
l_result.pack()

window.mainloop()

