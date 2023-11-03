import tkinter as tk
from icecream import ic

from http_request import get_response
from utilities import is_float

#init window
window = tk.Tk()
window.title("Converter")
window.geometry("500x200")


#create entry form
entry = tk.Entry(window)
entry.pack()

#get json file from http request
currencies = get_response()
curr_list = currencies["rates"]




#chose currency
menu_list = tk.Listbox(window, height=3, border=1, selectmode=tk.SINGLE) #create menu

for curr in curr_list:
      menu_list.insert(tk.END, curr) #insert currency name at the end every cicle

menu_list.pack()

def get_selection():

    cur_selection = menu_list.curselection()

    if cur_selection:
        index = cur_selection[0]
        selection = menu_list.get(index)
        print(selection)
    else: 
         print("non ci sono elementi selezionati")

get_selection()

#converts input value to new value based on exchange rate from  json file 
def Converter(currency_value,input_value):
        input_value = str(input_value.get())
        
        float_value = is_float(input_value) #check if float

        if float_value: 
                input_value = float(input_value)
                ic(input_value)
                new_value = input_value * currency_value #converion formula
                return new_value 
        else:
            l_result.config(text="Non hai inserito un valore valido da convertire! \n Prova ad inserire un numero o cambiare la virgola con un punto")


#show result of the conversion
def show_result():
    result = Converter(currencies["dollar"],entry)
    l_result.config(text=result)

#create button "convert"
converter_button = tk.Button(window, text="Converti", command=show_result)
converter_button.pack()

#create label 
l_result = tk.Label(window, text="")
l_result.pack()

window.mainloop()

