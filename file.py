from tkinter import *

def prueba():
    print("No recuerdo")
def ventmenu():

    root = Tk()
    root.geometry("450x300")
    root.title("prueba")


    root.columnconfigure(0, weight=2)
    root.rowconfigure(0, weight=1)

    root.columnconfigure(4, weight=2)
    root.rowconfigure(5, weight=1)

    lbtitle = Label(root, text="MENÚ PRINCIPAL")
    lbtitle.grid(column=2, row=0, padx=4, pady=5)

    btnusr = Button(root, text ="ABRIR/CERRAR", command = prueba, height=1, width=12)
    btnusr.grid(column=1, row=1, padx=4, pady=5)

    btnhab = Button(root, text ="REGISTRAR", command = prueba, height=1, width=12)
    btnhab.grid(column=1, row=2, padx=4, pady=5)

    btndisp = Button(root, text ="CAMBIAR PIN", command = prueba, height=1, width=12)
    btndisp.grid(column=3, row=1, padx=4, pady=5)

    btncrd = Button(root, text ="SALIR", command = prueba, height=1, width=12)
    btncrd.grid(column=3, row=2, padx=4, pady=5)

    root.mainloop()



