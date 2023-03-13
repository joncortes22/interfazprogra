from tkinter import *

def prueba():
    print("In progress")

def vregistro():
    mregistro = Tk()
    mregistro.geometry("450x300")
    mregistro.title("REGISTRAR")

    """mregistro.columnconfigure(0, weight=2)
    mregistro.rowconfigure(0, weight=1)"""
    mregistro.resizable(0,0)
    
    mregistro.columnconfigure(4, weight=2)
    mregistro.rowconfigure(5, weight=1)

    lbtitle = Label(mregistro, text="REGISTRAR CERRADURAS")
    lbtitle.grid(column=2, row=0, padx=4, pady=5)
    
    
    lbname = Label(mregistro, text="Nombre")
    lbname.grid(column=1, row=1, padx=4, pady=5)
    
    txtname = Entry(mregistro)
    txtname.grid(column=2, row=1, padx=4, pady=5)


    lblestado = Label(mregistro, text="Estado")
    lblestado.grid(column=1, row=2, pady=5)
    estado = StringVar() 
    cb_strings = ['Abierto', 'Cerrado']
    estado.set(cb_strings[0])

    columnf = 2
    for item in cb_strings:
        button = Radiobutton(mregistro, text=item, variable=estado, value=item)
        button.grid(column=columnf, row=2)
        columnf += 1


    lbpin = Label(mregistro, text="PIN")
    lbpin.grid(column=1, row=3, padx=4, pady=5)
    
    lbpin = Entry(mregistro, show="*")
    lbpin.grid(column=2, row=3, padx=4, pady=5)
    """btnacc = Button(mregistro, text ="ABRIR/CERRAR", height=1, width=12)
    btnacc.grid(column=1, row=1, padx=4, pady=5)"""


    mregistro.mainloop()

