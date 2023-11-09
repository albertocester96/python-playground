import tkinter as tk
from icecream import ic

from http_request import get_response
from utilities import try_float

#init window and frame
window = tk.Tk()
window.title("Converter")
window.geometry("500x200")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

#create entry form
entry = tk.Entry(window)
entry.grid(column=0, row=1)

#create label 
input_value = tk.Label(window, text="Input value", font=("helvetiva", 16), justify= "left")
input_value.grid(column=0,row=0)

l_result = tk.Label(window, text="")
l_result.grid(column=2, row=0, rowspan= 2)

#get json file from http request
currencies = get_response()
curr_list = currencies["rates"]


#chose currency
menu_list = tk.Listbox(window, height=10, border=1, selectmode=tk.SINGLE) #create menu
menu_list.grid(column= 0, row=1)

for curr in curr_list:
      menu_list.insert(tk.END, curr) #insert currency name at the end every cicle



def get_selection():

    cur_selection = menu_list.curselection()

    if cur_selection:
        index = cur_selection[0]
        selection = menu_list.get(index)
        print(selection)
        
        return selection
    else: 
         print("non ci sono elementi selezionati")

#converts input value to new value based on exchange rate from  json file 
def Converter(currency_value,input_value):
        input_value = str(input_value.get())
        
        float_value = try_float(input_value) #check if float

        if float_value: 
                input_value = float(input_value)
                ic(input_value)
                new_value = input_value * currency_value #converion formula
                return new_value 
        else:
            l_result.config(text="Non hai inserito un valore valido da convertire! \n Prova ad inserire un numero o cambiare la virgola con un punto")


#show result of the conversion
def show_result():

    result = Converter(curr_list[get_selection()],entry)
    l_result.config(text=result)

#create button "convert"
converter_button = tk.Button(window, text="Converti", command=show_result)
converter_button.grid(column=1, row=0, rowspan=2)


window.mainloop()

