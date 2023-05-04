"""
Alumnos:
Est. Melvin Josué Pereira Amaya SMIS010221
Est. Melvin Adiel Vásquez Mejía SMIS 001021
Est. Melvin Josué Pérez García SMIS007021

"""


from operator import index
from tkinter import N
from turtle import st

lisid = ["123244"]
lisnombre = ["gola"]
lisautorlibro = ["que"]
liseditorial = ["tal"]
listock = ["esta"]
lisprecio = ["amigo"]

class guardar:
    def __init__(self,id,nombre,autor,editorial,stock,precio):
        self.id = id
        self.nombre = nombre
        self.autor = autor
        self.editorial = editorial
        self.stock = stock
        self.precio = precio

        lisid.append(id)
        lisnombre.append(nombre)
        lisautorlibro.append(autor)
        liseditorial.append(editorial)
        listock.append(stock)
        lisprecio.append(precio)
    
    def mostrar(self):
        print("---------------------------------------------")
        print("Se guardaron estos datos:")
        print("id del libro: ",self.id)
        print("nombre del libro: ",self.nombre)
        print("autor del libro: ",self.autor)
        print("editorial del libro: ",self.editorial)
        print("Stock del libro: ",self.stock)
        print("Precio del libro: ",self.precio)

class verlibros:
    def ver():
         for i in range(0,len(lisid)):
            print("id del libro: ",lisid[i])
            print("nombre del libro: ",lisnombre[i])
            print("autor del libro: ",lisautorlibro[i])
            print("editorial del libro: ",liseditorial[i])
            print("Stock del libro: ",listock[i])
            print("Precio del libro: ",lisprecio[i])
            print("---------------------------------------------")


class modificar:
    def __init__(self,id,nombre,autor,editorial,stock,precio,indexx):
        self.id = id
        self.nombre = nombre
        self.autor = autor
        self.editorial = editorial
        self.stock = stock
        self.precio = precio
        self.index = indexx

        lisid[indexx] = id
        lisnombre[indexx] = nombre
        lisautorlibro[indexx] = autor
        liseditorial[indexx] = editorial
        listock[indexx] = stock
        lisprecio[indexx] = precio
    
    def mostrar(self):
        print("Se modifico estos datos:")
        print("id del libro: ",self.id)
        print("nombre del libro: ",self.nombre)
        print("autor del libro: ",self.autor)
        print("editorial del libro: ",self.editorial)
        print("Stock del libro: ",self.stock)
        print("Precio del libro: ",self.precio)

enid = ""
nombrelibro = ""
autorlibro = ""
editoriallbro = ""
enstock = ""
preciolibro = ""


ciclo = "si"
while ciclo == "si":
    print("--------------------------------------Menú--------------------------------------")
    print("1- Añadir libro  2- Lista de libros existentes 3- Buscar libro 4- Editar libro")
    print("--------------------------------------------------------------------------------")
    opcion = input("->")
    tipo = opcion.isnumeric()

    if tipo == True:
        num = int(opcion)
        
        if num == 1:

            enid = input("Ingrese el id del libro: ")
            nombrelibro = input("Ingrese el nombre del libro: ").lower()
            autorlibro = input("Ingrese el autor del libro: ").lower()
            editoriallbro = input("Ingrese la editorial del libro: ").lower()
            enstock = input("Ingrese el stock del libro: ")
            preciolibro = input("Ingrese el precio del libro: ")

            if enid !=" " and nombrelibro !=" " and autorlibro !=" " and editoriallbro !=" " and enstock !=" " and preciolibro !=" ":
                libros = guardar(enid,nombrelibro,autorlibro,editoriallbro,enstock,preciolibro)
                libros.mostrar()
            else:
                print("Llene los campos...")
            
        elif num == 2:

            verlibros.ver()

        elif num == 3:
            bus = input("Ingrese el nombre del libro a buscar: ").lower()
            if bus != "":
                try:
                    indice = lisnombre.index(bus)
                    print(" ")
                    print("---------------------------------------------")
                    print("id del libro: ",lisid[indice])
                    print("nombre del libro: ",lisnombre[indice])
                    print("autor del libro: ",lisautorlibro[indice])
                    print("editorial del libro: ",liseditorial[indice])
                    print("Stock del libro: ",listock[indice])
                    print("Precio del libro: ",lisprecio[indice])
                    print("---------------------------------------------")
                except:
                    print("No se encontro el libro")

            else:
                print("Llene los campos...")

        elif num == 4:

            edit = input("Ingrese el nombre del libro a editar: ").lower()
            if edit != "":
                try:
                    indice = lisnombre.index(edit)
                    print(" ")
                    print("---------------------------------------------")
                    enid = input("Ingrese el id del libro: ")
                    nombrelibro = input("Ingrese el nombre del libro: ").lower()
                    autorlibro = input("Ingrese el autor del libro: ").lower()
                    editoriallbro = input("Ingrese la editorial del libro: ").lower()
                    enstock = input("Ingrese el stock del libro: ")
                    preciolibro = input("Ingrese el precio del libro: ")
                    print("---------------------------------------------")
                except:
                    print("No se encontro el libro")

            else:
                print("Llene los campos...")

            if enid !="4 " and nombrelibro !=" " and autorlibro !=" " and editoriallbro !=" " and enstock !=" " and preciolibro !=" ":
                modi = modificar(enid,nombrelibro,autorlibro,editoriallbro,enstock,preciolibro,indice)
                modi.mostrar()
            else:
                print("Llene los campos...")
        
        else:
            print("Opcion invalida.") 


    else:
        print("Opcion invalida.")
    

    while True:

        ciclo = input("Desea continuar? ").lower()
    
        if ciclo == "no" or ciclo == "si":
             break
        else:
            print("Respuesta desconocida, porfavor responda si o no...")   