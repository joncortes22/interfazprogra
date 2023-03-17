import os, sys, getpass
from tkinter import *
from tkinter import messagebox, ttk

registro = []
combostate = ''
def ventmenu(tipo):

    mcerraduras = Tk()
    mcerraduras.geometry("450x300")
    mcerraduras.title("MENÚ CERRADURAS")

    mcerraduras.columnconfigure(0, weight=2)
    mcerraduras.rowconfigure(0, weight=1)
    mcerraduras.resizable(0,0)
    
    mcerraduras.columnconfigure(4, weight=2)
    mcerraduras.rowconfigure(5, weight=1)

    lbtitle = Label(mcerraduras, text="MENÚ PRINCIPAL", font='bold')
    lbtitle.grid(column=2, row=0, padx=4, pady=5)

    if tipo == 1:
        btnregis = Button(mcerraduras, text ="REGISTRAR", command=lambda:vregistrar(mcerraduras), height=1, width=13)
        btnregis.grid(column=1, row=2, padx=4, pady=5)

        btnsalir = Button(mcerraduras, text ="SALIR", command=lambda: exit(), height=1, width=13)
        btnsalir.grid(column=3, row=2, padx=4, pady=5)
    else:
        btnacc = Button(mcerraduras, text ="ABRIR/CERRAR", command=lambda:vaccionar(mcerraduras), height=1, width=13)
        btnacc.grid(column=1, row=1, padx=4, pady=5)

        btnregis = Button(mcerraduras, text ="REGISTRAR", command=lambda:vregistrar(mcerraduras), height=1, width=13)
        btnregis.grid(column=1, row=2, padx=4, pady=5)

        btnpin = Button(mcerraduras, text ="MODIFICAR PIN", command=lambda:vpin(mcerraduras), height=1, width=13)
        btnpin.grid(column=3, row=1, padx=4, pady=5)

        btnsalir = Button(mcerraduras, text ="SALIR", command=lambda:exit(), height=1, width=13)
        btnsalir.grid(column=3, row=2, padx=4, pady=5)

    mcerraduras.mainloop()
def mactivo(root):
    root.destroy()
    ventmenu(2)

def leer():
    #Esta función lee los contenidos del documento "cerraduras.txt", que es donde se almacena la información
    if (os.path.exists("cerraduras.txt") == False): #en caso de que el documento no esté creado, la función open con el comando w, crea el documento
        fp = open("cerraduras.txt", "w")
        ventmenu(1)
    else:
        with open("cerraduras.txt", "r") as fp: #a raíz de que el documento guarda los identificadores "nombre" y "PIN", hay que guardar los valores de por medio
            numLinea = [1] #este array empezará a guardar valores en 2, lo que obtendrá los valores de las cerraduras (recordando que las lineas de txt también se leen desde 0)
            for i, linea in enumerate(fp):
                if i in numLinea: #se lee de linea por medio empezando en 1
                    registro.append(linea.strip())
                    numLinea.append(i+2)
            if len(registro)==0: ventmenu(1)
            else: ventmenu(2)



def vaccionar(root):
    def selection_changed(event):
        cerradura = event.widget.get()
        for i in range(0, len(registro), 3):
            if cerradura == registro[i]: 
                if registro[i+1] == '1': 
                    estado.config(text='Abierto')
                    lbinst.config(text='*ingrese para cerrar')
                else: 
                    estado.config(text='Cerrado')
                    lbinst.config(text='*ingrese para abrir')
                break

    root.destroy()
    maccionar = Tk()
    maccionar.geometry("450x300")
    maccionar.title("ACCIONAR")

    """maccionar.columnconfigure(0, weight=2)
    maccionar.rowconfigure(0, weight=1)"""
    maccionar.resizable(0,0)
    
    maccionar.columnconfigure(0, weight=1)
    maccionar.rowconfigure(0, weight=1)
    maccionar.resizable(0,0)
    
    maccionar.columnconfigure(4, weight=2)
    maccionar.rowconfigure(6, weight=1)

    lbtitle = Label(maccionar, text="ABRIR/CERRAR", font=('bold'))
    lbtitle.grid(column=2, row=0, padx=4, pady=5, sticky='w')
    
    
    lbname = Label(maccionar, text="Cerraduras Disponibles")
    lbname.grid(column=1, row=1, padx=4, pady=5, sticky='w')
    
    options = []
    for i in range(0,len(registro),3):
        options.append(registro[i])
  
    # datatype of menu text
    combo = ttk.Combobox(maccionar, values=options, state='readonly')
    combo.bind("<<ComboboxSelected>>", selection_changed)
    combo.configure(width=13)
    combo.grid(column=2,row=1, padx=4, pady=5, sticky='w')

    lblestado = Label(maccionar, text="Estado")
    lblestado.grid(column=1, row=3, padx=4, pady=5, sticky='w')
    
    estado = Label(maccionar, text=combostate)
    estado.grid(column=2, row=3, padx=4, pady=5, sticky='w')
    
    lbpin2 = Label(maccionar, text="PIN")
    lbpin2.grid(column=1, row=4, padx=4, pady=5, sticky='w')
    lbinst = Label(maccionar, text="", font=('Arial',8))
    lbinst.grid(column=2, row=5, pady=5, sticky='nw')
    
    txtnewpin = Entry(maccionar, show="*")
    txtnewpin.grid(column=2, row=4, padx=4, pady=5, sticky='w')

    btnacc = Button(maccionar, text ="VERIFICAR", command=lambda: cambiarPin(maccionar, clicked.get(), txtpinact.get(), txtnewpin.get()), height=1, width=12)
    btnacc.grid(column=1, row=6, padx=4, pady=5)

    btnext = Button(maccionar, text ="SALIR", height=1, width=12, command=lambda: mactivo(maccionar))
    btnext.grid(column=2, row=6, padx=4, pady=5)


    maccionar.mainloop()

def accionar():
    while True:
        try:
            os.system('clear' if os.name == 'posix' else 'cls')
            print("--ABRIR / CERRAR--\n")
            print("CERRADURAS DISPONIBLES:\n")

            num = 1 #esta variable simplemente enumera las cerraduras
            dato = 0 #esta variable salta de un nombre de cerradura a otra
            nombres = [] #aquí se almacenan únicamente los nombres de las cerraduras para posteriormente usarlas para modificar el PIN de una cerradura específica

            #MUESTRA DE CERRADURAS
            for i in range(len(registro)):
                print(f"{num}- Nombre: {registro[dato]}")
                if registro[dato+1] == '0':
                    print("Estado: Cerrado")
                else: 
                    print("Estado: Abierto")
                nombres.append(registro[dato])
                dato += 3
                num += 1
                if dato == len(registro): break
            print("\n")


            #ELECCIÓN DE CERRADURA
            while True:
                select = input("Ingrese el # de la cerradura a modificar o 'S' para salir: ")
                if select.lower().strip() == 's': ventmenu(2)
                if int(select.strip()) > len(nombres): accionar()
                else:
                    find = False
                    for i in range(len(registro)):
                        if find: break
                        if nombres[int(select.strip())-1] == registro[i]:
                            find = True
                            cerradura = i
                            desc = 0
                            while True: #el while se repetirá hasta que se ingrese una opcion correcta
                                if registro[i+1] == "0":
                                    desc = int(input("La cerradura se encuentra cerrada, desea abrirla? 1-Si 2-No: "))
                                elif registro[i+1] == "1":
                                    desc = int(input("La cerradura se encuentra abierta, desea cerrala? 1-Si 2-No: "))
                                if desc != 1 and desc !=2: print("Opción inválida\n")
                                if desc == 1: break
                                elif desc == 2: return
                    break
                    
                            
            #VERIFICACIÓN DE PIN
            while True: 
                pin = getpass.getpass("Ingrese el PIN de la cerradura: ") 
                if registro[cerradura+2] == pin: 
                    if registro[cerradura+1] == "0": #si la cerradura está cerrada, se abrirá cambiando el valor a 1 y viceversa
                        registro[cerradura+1] = "1"
                        os.system('clear' if os.name == 'posix' else 'cls')
                        print("La cerradura se ha abierto")
                    else: 
                        registro[cerradura+1] = "0"
                        os.system('clear' if os.name == 'posix' else 'cls')
                        print("La cerradura se ha cerrado")
                    break
                else:
                    print("PIN inválido\n")
                    while True: #el while se repetirá hasta que se ingrese una opcion correcta
                        opt = int(input("¿Desea volver a intentar? 1-Si 2-No: ")) #la respuesta debe de ser 1 o 2
                        if opt != 1 and opt != 2: print("Opción no valida\n")
                        if opt == 1: break 
                        elif opt == 2: return


            #ESCRITURA EN TXT FILE
            titulo = 0 #variable que decidirá qué tipo de dato se escribirá en el .txt
            with open("cerraduras.txt", "w") as f: #se abre el documento
                for i in range(len(registro)):
                    if titulo == 0: #si el titulo es 0, se escribirá "Nombre" y su dato
                        f.write("Nombre:\n")
                        f.write(registro[i]) 
                        titulo += 1 #Se aumenta en 1 el titulo para que la siguiente escritura sea para el estado
                    elif titulo == 1: #si el titulo es 1, se escribirá "Estado"y su dato
                        f.write("Estado:\n")
                        f.write(registro[i]) 
                        titulo +=1 #Se aumenta en 1 el titulo para que la siguiente escritura sea para el PIN
                    elif titulo == 2: #si el titulo es 1, se escribirá "PIN" y su dato
                        f.write("PIN:\n")
                        f.write(registro[i]) 
                        titulo = 0 #Se devuelve la variable a 0 para que la próxima escritura sea de un Nombre de Cerradura
                    f.write("\n")
            print("\n")
            while True: #Después de haber guardado la cerradura, se pregunta cuál es la siguiente acción
                resp = int(input("¿Desea modificar otra cerradura? 1-Si 2-No | Resp: "))
                if resp == 1: break #Si la respuesta es sí, vuelve a comenzar el proceso de registro
                elif resp == 2: accionar() #Si es no, se abre el menú
                else: print("Opción no valida") #Cualquier otra opción dará error
            print("Prueba")
        except ValueError:
            accionar()

def verificar(nombre, estado,pin, root):
    datos = [nombre,estado,pin]
    registrar(datos, root)

def vregistrar(root):
    root.destroy()
    mregistro = Tk()
    mregistro.geometry("450x300")
    mregistro.title("REGISTRAR")

    """mregistro.columnconfigure(0, weight=2)
    mregistro.rowconfigure(0, weight=1)"""
    mregistro.resizable(0,0)
    
    mregistro.columnconfigure(0, weight=1)
    mregistro.rowconfigure(0, weight=1)
    mregistro.resizable(0,0)
    
    mregistro.columnconfigure(4, weight=2)
    mregistro.rowconfigure(5, weight=1)

    lbtitle = Label(mregistro, text="REGISTRAR CERRADURAS", font=('bold'))
    lbtitle.grid(column=2, row=0, padx=4, pady=5, sticky='w')
    
    
    lbname = Label(mregistro, text="Nombre")
    lbname.grid(column=1, row=1, padx=4, pady=5, sticky='w')
    
    txtname = Entry(mregistro)
    txtname.grid(column=2, row=1, padx=4, pady=5, sticky='w')


    lblestado = Label(mregistro, text="Estado")
    lblestado.grid(column=1, row=2, pady=5, padx=4, sticky='w')
  

    #acomodo
    var = StringVar()
    R1 = Radiobutton(mregistro, text="Abierto", variable=var, value="Abierto")
    R1.grid(column=2, row=2, sticky='w')

    R2 = Radiobutton(mregistro, text="Cerrado", variable=var, value="Cerrado")
    R2.grid(column=2, row=3, sticky='w')
    var.set(None)


    lbpin = Label(mregistro, text="PIN")
    lbpin.grid(column=1, row=4, padx=4, pady=5, sticky='w')
    
    txtpin = Entry(mregistro, show="*")
    txtpin.grid(column=2, row=4, padx=4, pady=5, sticky='w')
    
    lbinst = Label(mregistro, text="*numérico de 4 a 6 dígitos", font=('Arial',8))
    lbinst.grid(column=2, row=5, pady=5, sticky='nw')

    btnacc = Button(mregistro, text ="VERIFICAR", command=lambda: verificar(txtname.get(), var.get(), txtpin.get(), mregistro), height=1, width=12)
    btnacc.grid(column=1, row=5, padx=4, pady=5)

    btnext = Button(mregistro, text ="SALIR", height=1, width=12, command=lambda: mactivo(mregistro))
    btnext.grid(column=2, row=5, padx=4, pady=5)


    mregistro.mainloop()

def registrar(datos, root):
    
    if datos[0] == '' or datos[1] == 'None' or datos[2] == '':
        messagebox.showerror(message="INFORMACIÓN INCOMPLETA", title="ERROR")
        vregistrar(root)

    repetido = False
    if len(registro) > 0: #si hay datos registrados, se pueden crear nuevos, si no, que se cree el primero
        for i in range(0, len(registro), 3):
            if datos[0].lower().strip() == registro[i].lower().strip(): 
                repetido = True
                break
            if i>len(registro):break
        if repetido:
            messagebox.showerror(message="NOMBRE EN USO", title="ERROR")
            vregistrar(root)
        else: registro.append(datos[0].strip())
    else:
        registro.append(datos[0].strip())


    #VALIDACIÓN DE ESTADO
    if datos[1] == 'None':
        messagebox.showerror(message="ESTADO SIN ELEGIR", title="ERROR")
        vregistrar(root)
    else:
        if datos[1] == "Abierto": registro.append("1")
        else: registro.append("0")

    #VALIDACIÓN DE PIN
    
    if len(datos[2].strip())>=4 and len(datos[2].strip())<= 6 and datos[2].isnumeric(): 
        registro.append(datos[2].strip().strip())
    if not datos[2].isnumeric():
        messagebox.showerror(message="PIN DEBE SER NUMÉRICO", title="ERROR")
        for i in range(2): del registro[len(registro)-1]
        vregistrar(root)
    if len(datos[2].strip())<4 or len(datos[2].strip())> 6:
        messagebox.showerror(message="CANTIDAD DE CARACTERES INVÁLIDOS", title="ERROR")
        for i in range(2): del registro[len(registro)-1]
        vregistrar(root)
        

    titulo = 0 #variable que decidirá qué tipo de dato se escribirá en el .txt
    #ESCRITURA EN TXT FILE
    with open("cerraduras.txt", "a") as f: #se abre el documento
        for i in range(3):
            if titulo == 0: #si el titulo es 0, se escribirá "Nombre" y su dato
                f.write("Nombre:\n")
                f.write(registro[len(registro)-3]) #El ante-penúltimo dato de la lista siempre será un nombre de cerradura, por lo que se utiliza ese valor para escribirlo en el .txt
                titulo += 1 #Se aumenta en 1 el titulo para que la siguiente escritura sea para el estado
            elif titulo == 1: #si el titulo es 1, se escribirá "PIN" y su dato
                f.write("Estado:\n")
                f.write(registro[len(registro)-2]) #El penúltimo dato de la lista siempre será un estado de cerradura, por lo que se utiliza ese valor para escribirlo en el .txt
                titulo +=1 #Se aumenta en 1 el titulo para que la siguiente escritura sea para el PIN
            elif titulo == 2: #si el titulo es 1, se escribirá "PIN" y su dato
                f.write("PIN:\n")
                f.write(registro[len(registro)-1]) #El último dato de la lista siempre será un PIN de cerradura, por lo que se utiliza ese valor para escribirlo en el .txt
                titulo = 0 #Se devuelve la variable a 0 para que la próxima escritura sea de un Nombre de Cerradura
            f.write("\n")
        messagebox.showinfo(message="INGRESADO CORRECTAMENTE", title="REGISTRO")
    vregistrar(root)

def vpin(root):
    root.destroy()
    mpin = Tk()
    mpin.geometry("450x300")
    mpin.title("MODIFICAR PIN")

    """mpin.columnconfigure(0, weight=2)
    mpin.rowconfigure(0, weight=1)"""
    mpin.resizable(0,0)
    
    mpin.columnconfigure(0, weight=1)
    mpin.rowconfigure(0, weight=1)
    mpin.resizable(0,0)
    
    mpin.columnconfigure(4, weight=2)
    mpin.rowconfigure(6, weight=1)

    lbtitle = Label(mpin, text="MODIFICAR PIN", font=('bold'))
    lbtitle.grid(column=2, row=0, padx=4, pady=5, sticky='w')
    
    
    lbname = Label(mpin, text="Cerraduras Disponibles")
    lbname.grid(column=1, row=1, padx=4, pady=5, sticky='w')
    
    options = []
    for i in range(0,len(registro),3):
        options.append(registro[i])
  
    # datatype of menu text
    clicked = StringVar()
    clicked.set('')
    drop = OptionMenu(mpin, clicked, *options )
    drop.configure(width=13)
    drop.grid(column=2,row=1, padx=4, pady=5, sticky='w')


    lbpin1 = Label(mpin, text="PIN Actual")
    lbpin1.grid(column=1, row=3, padx=4, pady=5, sticky='w')
    
    txtpinact = Entry(mpin, show="*")
    txtpinact.grid(column=2, row=3, padx=4, pady=5, sticky='w')
    
    lbpin2 = Label(mpin, text="Nuevo PIN")
    lbpin2.grid(column=1, row=4, padx=4, pady=5, sticky='w')
    lbinst = Label(mpin, text="*numérico de 4 a 6 dígitos", font=('Arial',8))
    lbinst.grid(column=2, row=5, pady=5, sticky='nw')
    
    txtnewpin = Entry(mpin, show="*")
    txtnewpin.grid(column=2, row=4, padx=4, pady=5, sticky='w')

    btnacc = Button(mpin, text ="VERIFICAR", command=lambda: cambiarPin(mpin, clicked.get(), txtpinact.get(), txtnewpin.get()), height=1, width=12)
    btnacc.grid(column=1, row=6, padx=4, pady=5)

    btnext = Button(mpin, text ="SALIR", height=1, width=12, command=lambda: mactivo(mpin))
    btnext.grid(column=2, row=6, padx=4, pady=5)


    mpin.mainloop()
def cambiarPin(root, cerradura, pin, newpin):
    
    if cerradura == '' or pin == '' or newpin == '':
        messagebox.showerror(message="INFORMACIÓN INCOMPLETA", title="ERROR")
        vpin(root)

    
    for i in range(0, len(registro), 3):
        if (cerradura == registro[i]):
            oldpin = registro[i+2] #se busca el PIN de la cerradura que se desea modificar para posteriormente verificar que el usuario conoce el PIN actual
            break

    #VERIFICACIÓN DE PIN
    
    if oldpin != pin: 
        messagebox.showerror(message="PIN ACTUAL INCORRECTO", title="ERROR")
        vpin(root)
                    
    #INGRESO DE NUEVO PIN
    

    if newpin == oldpin:
        messagebox.showerror(message="NUEVO PIN ES IGUAL AL ACTUAL", title="ERROR")
        vpin(root)
    if not newpin.strip().isnumeric():
        messagebox.showerror(message="PIN DEBE SER NUMÉRICO", title="ERROR")
        vpin(root)
    if len(newpin.strip())>=4 and len(newpin.strip())<= 6: 
        for i in range(0, len(registro), 3): #se procede a cambiar el PIN en la lista para posteriormente hacer la modificación del cerraduras.txt
            if (cerradura.strip() == registro[i]):
                registro[i+2] = newpin.strip() #se intercambia el anterior PIN por el nuevo
                messagebox.showinfo(message="PIN MODIFICADO EXITOSAMENTE", title="MODIFICAR PIN")
    else:
        messagebox.showerror(message="PIN DEBE SER DE 4 A 6 CARACTERES", title="ERROR")
        vpin(root)
        

    #ESCRITURA EN TXT FILE
    titulo = 0 #variable que decidirá qué tipo de dato se escribirá en el .txt
    with open("cerraduras.txt", "w") as f: #se abre el documento
        for i in range(len(registro)):
            if titulo == 0: #si el titulo es 0, se escribirá "Nombre" y su dato
                f.write("Nombre:\n")
                f.write(registro[i]) 
                titulo += 1 #Se aumenta en 1 el titulo para que la siguiente escritura sea para el estado
            elif titulo == 1: #si el titulo es 1, se escribirá "Estado"y su dato
                f.write("Estado:\n")
                f.write(registro[i]) 
                titulo +=1 #Se aumenta en 1 el titulo para que la siguiente escritura sea para el PIN
            elif titulo == 2: #si el titulo es 1, se escribirá "PIN" y su dato
                f.write("PIN:\n")
                f.write(registro[i]) 
                titulo = 0 #Se devuelve la variable a 0 para que la próxima escritura sea de un Nombre de Cerradura
            f.write("\n")
    vpin(root)

leer()