import tkinter as tk
from icecream import ic

#inizializza finestra
window = tk.Tk()
window.title("Converter")
window.geometry("500x200")

euro_value = 1
dollar_value = 2
yen_value = 3
pound_value = 4

currencies = {
    "euro": euro_value,
    "dollar": dollar_value,
    "yen": yen_value,
    "pound": pound_value
}

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
                new_value = input_value * input_value/currency_value #formula di conversione
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

