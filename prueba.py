from tkinter import *
from file import prueba
from cerradura import leer as cerradura
def actions(root, file):
    root.destroy()
    match file:
        case 1: prueba()
        case 2: cerradura()

def main():
    root = Tk()
    root.geometry("450x300")
    root.title("Smart Home")
    root.resizable(0,0)


    root.columnconfigure(0, weight=2)
    root.rowconfigure(0, weight=1)

    root.columnconfigure(4, weight=2)
    root.rowconfigure(5, weight=1)

    lbtitle = Label(root, text="MENÚ PRINCIPAL")
    lbtitle.grid(column=2, row=0, padx=4, pady=5)

    btnusr = Button(root, text ="USUARIOS", command=lambda: actions(root, 1), height=1, width=12)
    btnusr.grid(column=1, row=1, padx=4, pady=5)

    btnhab = Button(root, text ="HABITACIONES", command=lambda: actions(root, 1), height=1, width=12)
    btnhab.grid(column=1, row=2, padx=4, pady=5)

    btndisp = Button(root, text ="DISPOSITIVOS", command=lambda: actions(root, 1), height=1, width=12)
    btndisp.grid(column=3, row=1, padx=4, pady=5)

    btncrd = Button(root, text ="CERRADURAS", command=lambda: actions(root, 2), height=1, width=12)
    btncrd.grid(column=3, row=2, padx=4, pady=5)

    btnext = Button(root, text ="SALIR", command=lambda: actions(root, 1), height=1, width=12)
    btnext.grid(column=2, row=3, padx=4, pady=10)

    root.mainloop()

main()