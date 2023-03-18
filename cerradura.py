import os, sys, getpass
from tkinter import *
from tkinter import messagebox, ttk

registro = []
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
def escribir():
    titulo = 0
    with open("cerraduras.txt", 'w') as f: #se abre el documento
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

def vaccionar(root):
    def selection_changed(event):
        cerradura = event.widget.get()
        for i in range(0, len(registro), 3):
            if cerradura == registro[i]: 
                if registro[i+1] == '1': 
                    estado.config(text='Abierto')
                    lbpin2.config(text='PIN para Cerrar')
                else: 
                    estado.config(text='Cerrado')
                    lbpin2.config(text='PIN para Abrir')
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
    lbtitle.grid(column=1, row=0, padx=4, pady=5, sticky='w')
    
    
    lbname = Label(maccionar, text="Cerraduras Disponibles")
    lbname.grid(column=1, row=1, padx=4, pady=5, sticky='w')
    
    options = []
    for i in range(0,len(registro),3):
        options.append(registro[i])
  
    # datatype of menu text
    combo = ttk.Combobox(maccionar, values=options, state='readonly')
    combo.bind("<<ComboboxSelected>>", selection_changed)
    combo.configure(width=17)
    combo.grid(column=2,row=1, padx=4, pady=5, sticky='w')

    lblestado = Label(maccionar, text="Estado")
    lblestado.grid(column=1, row=3, padx=4, pady=5, sticky='w')
    
    estado = Label(maccionar, text='')
    estado.grid(column=2, row=3, padx=4, pady=5, sticky='w')
    
    lbpin2 = Label(maccionar, text="PIN")
    lbpin2.grid(column=1, row=4, padx=4, pady=5, sticky='w')
    lbinst = Label(maccionar, text="", font=('Arial',8))
    lbinst.grid(column=2, row=5, pady=5, sticky='nw')
    
    txtpin = Entry(maccionar, show="*")
    txtpin.grid(column=2, row=4, padx=4, pady=5, sticky='w')

    btnacc = Button(maccionar, text ="VERIFICAR", command=lambda: accionar(maccionar, combo.get(), txtpin.get()), height=1, width=12)
    btnacc.grid(column=1, row=5, padx=4, pady=5, sticky='s')

    btnext = Button(maccionar, text ="SALIR", height=1, width=12, command=lambda: mactivo(maccionar))
    btnext.grid(column=2, row=5, padx=4, pady=5, sticky='s')


    maccionar.mainloop()
def accionar(root, nombre, pin):
    try:
        if nombre == '' or pin == '':
            messagebox.showerror(message="INFORMACIÓN INCOMPLETA", title="ERROR")
            vaccionar(root)
        #ELECCIÓN DE CERRADURA
        cerradura = 0
        for i in range(0, len(registro), 3):
            if nombre == registro[i]:
                cerradura = i
                break
        #VERIFICACIÓN DE PIN
        if registro[cerradura+2] == pin: 
            if registro[cerradura+1] == "0": #si la cerradura está cerrada, se abrirá cambiando el valor a 1 y viceversa
                registro[cerradura+1] = "1"
                messagebox.showinfo(message="CERRADURA SE HA ABIERTO", title="ABRIR/CERRAR")
            else: 
                messagebox.showinfo(message="CERRADURA SE HA CERRADO", title="ABRIR/CERRAR")
                registro[cerradura+1] = "0"
        else:
            messagebox.showerror(message="PIN INCORRECTO", title="ERROR")
            vaccionar(root)


        #ESCRITURA EN TXT FILE
        escribir()
        
        vaccionar(root)
    except ValueError:
        vaccionar(root)


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

    btnacc = Button(mregistro, text ="VERIFICAR", command=lambda: registrar(txtname.get(), var.get(), txtpin.get(), mregistro), height=1, width=12)
    btnacc.grid(column=1, row=5, padx=4, pady=5)

    btnext = Button(mregistro, text ="SALIR", height=1, width=12, command=lambda: mactivo(mregistro))
    btnext.grid(column=2, row=5, padx=4, pady=5)


    mregistro.mainloop()
def registrar(nombre, estado, pin, root):
    try:
        if nombre == '' or estado == 'None' or pin == '':
            messagebox.showerror(message="INFORMACIÓN INCOMPLETA", title="ERROR")
            vregistrar(root)

        if not nombre.isalnum():
            messagebox.showerror(message="NOMBRE DEBE SER ALFANUMÉRICO", title="ERROR")
            vregistrar(root)

        repetido = False
        if len(registro) > 0: #si hay datos registrados, se pueden crear nuevos, si no, que se cree el primero
            for i in range(0, len(registro), 3):
                if nombre.lower().strip() == registro[i].lower().strip(): 
                    repetido = True
                    break
                if i>len(registro):break
            if repetido:
                messagebox.showerror(message="NOMBRE EN USO", title="ERROR")
                vregistrar(root)
            else: registro.append(nombre.strip())
        else:
            registro.append(nombre.strip())


        #VALIDACIÓN DE ESTADO
        
        if estado == "Abierto": registro.append("1")
        else: registro.append("0")

        #VALIDACIÓN DE PIN
        
        if len(pin.strip())>=4 and len(pin.strip())<= 6 and pin.isnumeric(): 
            registro.append(pin.strip().strip())
        if not pin.isnumeric():
            messagebox.showerror(message="PIN DEBE SER NUMÉRICO", title="ERROR")
            for i in range(2): del registro[len(registro)-1]
            vregistrar(root)
        if len(pin.strip())<4 or len(pin.strip())> 6:
            messagebox.showerror(message="CANTIDAD DE CARACTERES INVÁLIDOS", title="ERROR")
            for i in range(2): del registro[len(registro)-1]
            vregistrar(root)
            

        #ESCRITURA EN TXT FILE
        escribir()
        messagebox.showinfo(message="INGRESADO CORRECTAMENTE", title="REGISTRO")
        vregistrar(root)
    except ValueError:
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
    lbtitle.grid(column=1, row=0, padx=4, pady=5, sticky='w')
    
    
    lbname = Label(mpin, text="Cerraduras Disponibles")
    lbname.grid(column=1, row=1, padx=4, pady=5, sticky='w')
    
    options = []
    for i in range(0,len(registro),3):
        options.append(registro[i])
  
    # datatype of menu text
    combo = ttk.Combobox(mpin, values=options, state='readonly')
    combo.configure(width=17)
    combo.grid(column=2,row=1, padx=4, pady=5, sticky='w')


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

    btnacc = Button(mpin, text ="VERIFICAR", command=lambda: cambiarPin(mpin, combo.get(), txtpinact.get(), txtnewpin.get()), height=1, width=12)
    btnacc.grid(column=1, row=6, padx=4, pady=5)

    btnext = Button(mpin, text ="SALIR", height=1, width=12, command=lambda: mactivo(mpin))
    btnext.grid(column=2, row=6, padx=4, pady=5)


    mpin.mainloop()
def cambiarPin(root, cerradura, pin, newpin):
    try:
        #VERIFICAR QUE ESTÉ TODA LA INFORMACIÓN, SI NO ES ASÍ SE DA ERROR Y VUELVE A CORRER LA VENTANA
        if cerradura == '' or pin == '' or newpin == '':
            messagebox.showerror(message="INFORMACIÓN INCOMPLETA", title="ERROR")
            vpin(root)

        #BUSCAR EL PIN ACTUAL DENTRO DEL REGISTRO
        for i in range(0, len(registro), 3):
            if (cerradura == registro[i]):
                oldpin = registro[i+2] #se busca el PIN de la cerradura que se desea modificar para posteriormente verificar que el usuario conoce el PIN actual
                break

        #VERIFICACIÓN DEL PIN ACTUAL CON EL INGRESADO
        if oldpin != pin: 
            messagebox.showerror(message="PIN ACTUAL INCORRECTO", title="ERROR")
            vpin(root)
                        
        #INGRESO DE NUEVO PIN
        #VERIFICAR POSIBLES ERRORES
        if newpin == oldpin:
            messagebox.showerror(message="NUEVO PIN ES IGUAL AL ACTUAL", title="ERROR")
            vpin(root)
        if not newpin.strip().isnumeric():
            messagebox.showerror(message="PIN DEBE SER NUMÉRICO", title="ERROR")
            vpin(root)
        
        #VERIFICAR QUE EL PIN CUMPLA LOS REQUERIMIENTOS, DE SER ASÍ SE MODIFICA LA LISTA REGISTRO
        if len(newpin.strip())>=4 and len(newpin.strip())<= 6: 
            for i in range(0, len(registro), 3): #se procede a cambiar el PIN en la lista para posteriormente hacer la modificación del cerraduras.txt
                if (cerradura.strip() == registro[i]):
                    registro[i+2] = newpin.strip() #se intercambia el anterior PIN por el nuevo
        else:
            messagebox.showerror(message="PIN DEBE SER DE 4 A 6 CARACTERES", title="ERROR")
            vpin(root)
            

        #ESCRITURA EN TXT FILE
        escribir()
        messagebox.showinfo(message="PIN MODIFICADO EXITOSAMENTE", title="MODIFICAR PIN")
        vpin(root)
    except ValueError:
        vpin(root)

leer()