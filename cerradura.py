import os, sys, getpass
from tkinter import *


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

def menu(registro):
    ventmenu()
    while True:
        try:
            os.system('clear' if os.name == 'posix' else 'cls')
            print("""
---MENÚ CERRADURAS---\n
|1-Abrir/Cerrar        |
|2-Registrar           |
|3-Cambiar PIN         |
|4-Salir               |
            """)
            if len(registro) == 0:
                opcion= int(input("No hay cerraduras registradas, ingrese para seguir | Opción: "))
                match opcion:
                    case 2: registrar(registro)
                    case 4: return
                    case _: opcion = 1
            else:
                opcion = int(input("Opción: "))
                match opcion:
                    case 1: accionar(registro)
                    case 2: registrar(registro)
                    case 3: cambiarPin(registro)
                    case 4: return
                    case _: opcion = 1
        except ValueError:
            opcion = 1

def leer():
    #Esta función lee los contenidos del documento "cerraduras.txt", que es donde se almacena la información
    registro = [] #se define la lista "registro", que manejará toda la información que necesitemos
    if (os.path.exists("cerraduras.txt") == False): #en caso de que el documento no esté creado, la función open con el comando w, crea el documento
        fp = open("cerraduras.txt", "w")
        menu(registro)
    else:
        with open("cerraduras.txt", "r") as fp: #a raíz de que el documento guarda los identificadores "nombre" y "PIN", hay que guardar los valores de por medio
            numLinea = [1] #este array empezará a guardar valores en 2, lo que obtendrá los valores de las cerraduras (recordando que las lineas de txt también se leen desde 0)
            for i, linea in enumerate(fp):
                if i in numLinea: #se lee de linea por medio empezando en 1
                    registro.append(linea.strip())
                    numLinea.append(i+2)
            menu(registro)


def accionar(registro):
    os.system('clear' if os.name == 'posix' else 'cls')
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
                if select.lower().strip() == 's': menu(registro)
                if int(select.strip()) > len(nombres): accionar(registro)
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
                elif resp == 2: accionar(registro) #Si es no, se abre el menú
                else: print("Opción no valida") #Cualquier otra opción dará error
            print("Prueba")
        except ValueError:
            accionar(registro)


def registrar(registro):
    os.system('clear' if os.name == 'posix' else 'cls')
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("--REGISTRO DE CERRADURA--\n")

        repetido = False
        if len(registro) > 0: #si hay datos registrados, se pueden crear nuevos, si no, que se cree el primero
            nombre = input("Nombre: ")
            for i in range(len(registro)):
                if nombre.lower().strip() == registro[i].lower().strip(): 
                    repetido = True
                    break
                i+=3
                if i>len(registro):break
            if repetido:
                intento = 0
                print("Este nombre ya existe")
                while True: #Después de haber guardado la cerradura, se pregunta cuál es la siguiente acción
                    intento = int(input("¿Desea volver a intentar? 1-Si 2-No | Resp: "))
                    if intento == 1: registrar(registro) #Si la respuesta es sí, vuelve a comenzar el proceso de registro
                    elif intento == 2: return #Si es no, se abre el menú
                    else: print("Opción no valida\n") #Cualquier otra opción dará error
            else: registro.append(nombre.strip())
        else:
            nombre = input("Nombre: ")
            registro.append(nombre.strip())


        #VALIDACIÓN DE ESTADO
        estado = "inactive"
        while estado != "1" or estado != "0": #el estado tiene que ser tiene que ser 1 o 2, de lo contrario no podrá continuar
            estado = input("Estado 1-Abierto 0-Cerrado: ")
            if estado == "1" or estado == "0": 
                registro.append(estado)
                break
            else:
                print("Opción no valida")

        #VALIDACIÓN DE PIN
        
        while True: #el estado tiene que ser tiene que ser 1 o 2, de lo contrario no podrá continuar
            pin = getpass.getpass("PIN numeral(entre 4 y 6 números): ")
            if len(pin.strip())>=4 and len(pin.strip())<= 6: 
                registro.append(pin.strip())
                break
            else:
                print("Opción no valida\n")

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
        while True: #Después de haber guardado la cerradura, se pregunta cuál es la siguiente acción
            resp = int(input("\n¿Desea guardar otra cerradura? 1-Si 2-No | Resp: "))
            if resp == 1: break #Si la respuesta es sí, vuelve a comenzar el proceso de registro
            elif resp == 2: return #Si es no, se abre el menú
            else: print("Opción no valida") #Cualquier otra opción dará error


def cambiarPin(registro):
    os.system('clear' if os.name == 'posix' else 'cls')
    
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("--CAMBIO DE PIN--\n")
        print("CERRADURAS DISPONIBLES:\n")

        num = 1 #esta variable simplemente enumera las cerraduras
        dato = 0 #esta variable salta de un nombre de cerradura a otra
        nombres = [] #aquí se almacenan únicamente los nombres de las cerraduras para posteriormente usarlas para modificar el PIN de una cerradura específica
        #MUESTRA DE CERRADURAS
        for i in range(len(registro)):
            print(f"{num}- Nombre: {registro[dato]}")
            nombres.append(registro[dato])
            dato += 3
            num += 1
            if dato == len(registro): break
        print("\n")
        #ELECCIÓN DE CERRADURA
        select = input("Ingrese el # de la cerradura a modificar o 'S' para salir: ")
        if select.lower().strip() == 's': return
        if int(select.strip()) > len(nombres): cambiarPin(registro)
        else:
            for i in range(len(registro)):
                if (nombres[int(select.strip())-1] == registro[i]):
                    oldpin = registro[i+2] #se busca el PIN de la cerradura que se desea modificar para posteriormente verificar que el usuario conoce el PIN actual
                    break

        #VERIFICACIÓN DE PIN
        while True: 
            opt = 0
            pin = getpass.getpass("\nIngrese el PIN actual: ")
            if oldpin == pin: break
            else:
                print("PIN incorrecto\n")
                while True:
                    opt = int(input("¿Desea volver a intentar? 1-Si 2-No: ")) #la respuesta debe de ser 1 o 2
                    if opt != 1 and opt != 2: print("Opción no valida\n")
                    if opt == 1: break 
                    elif opt == 2: cambiarPin(registro)
                        
        #INGRESO DE NUEVO PIN
        
        
        while True: 
            newpin = getpass.getpass("\nIngrese el nuevo PIN numeral(entre 4 y 6 números): ") #se hace la misma validación de PIN que en el registro
            if newpin == oldpin:
                while True:
                    opt = int(input("PIN ingresado es igual al actual ¿Desea volver a intentar? 1-Si 2-No: ")) #la respuesta debe de ser 1 o 2
                    if opt != 1 and opt != 2: print("Opción no valida\n")
                    if opt == 1: break 
                    elif opt == 2: return
                if opt == 1: continue
            if len(newpin.strip())>=4 and len(newpin.strip())<= 6: 
                for i in range(len(registro)): #se procede a cambiar el PIN en la lista para posteriormente hacer la modificación del cerraduras.txt
                    if (nombres[int(select.strip())-1] == registro[i]):
                        registro[i+2] = newpin.strip() #se intercambia el anterior PIN por el nuevo
                        print("PIN modificado existosamente")
                        break
                break
            else:
                print("PIN no válido")
            

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
            elif resp == 2: return #Si es no, se abre el menú
            else: print("Opción no válida\n") #Cualquier otra opción dará error

