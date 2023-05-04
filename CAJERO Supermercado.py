#CAJERO AUTOMATICO

"""
Alumnos:
Est. Melvin Josué Pereira Amaya SMIS010221
Est. Melvin Adiel Vásquez Mejía SMIS 001021
Est. Melvin Josué Pérez García SMIS007021

"""

res = "no"
contador = 0
Lcod = []
Lnom = []
Lcant =[]
Ltotal = []
Lproduc = []

while True:
   cod = input("Ingrese el codigo del producto:- ")
   nom = input("Ingrese el nombre del producto:- ")
   cant = int(input("Ingrese la cantidad del producto:- "))
   pre = float(input("Ingrese el precio del porducto:- "))
   total = cant*pre
   Ncod = "--",cod,"-"
   Nnom = "----",nom,"----"
   Ncant = "---",cant,"---"
   Ntotal = "-------",total,"-------"
   Lcod.append(cod)
   Lnom.append(nom)
   Lcant.append(cant)
   Ltotal.append(total)
   ress = input("Deseas agregar otro producto?:- ")
   contador = contador + 1
   Nproduc = "producto",contador
   Lproduc.append(Nproduc)
   if(ress == res):
       totalF = sum(Ltotal)
       print("-----------------------FACTURA---------------------------")
       for Lprodu,Lco,Lno,Lcan,Ltota in zip(Lproduc,Lcod,Lnom,Lcant,Ltotal):
           print(f'|{Lprodu}|CODIGO:|{Lco}|NOMBRE:|{Lno}|CANTIDAD:|{Lcan}|TOTAL:|{Ltota}|')
           
       print("----------------------TOTAL A PAGAR---------------------")
       print("----------------------", totalF,"-----------------------")    
       print("-------------------------------------------------------------------------")
       print("----------------------FORMAS DE PAGO--------------------")
       print("OPCION 1------------------EFECTIVO----------------------")
       print("OPCION 2------------------TARGETA-----------------------")
       pago = int(input("Elige una opcion:- "))
       if (pago == 1):
           if (totalF >50.00 and totalF <100.00):
               des = totalF * 0.10
               NtotalF = totalF - des
               print("Pago realizado con exito se Cobro ", NtotalF, "Con un descuento de ", des)
               break
           elif (totalF > 100.00):
               des = totalF * 0.30
               NtotalF = totalF - des
               print("Pago realizado con exito se Cobro ", NtotalF, "Con un descuento de ", des)
               break
           else:
               print("Pago realizado con exito se Cobro ", totalF, "No aplica a descuento")
       elif(pago == 2):
           if (totalF >50.00 and totalF <100.00):
               des = totalF * 0.20
               NtotalF = totalF - des
               print("Pago realizado con exito se Cobro ", NtotalF, "Con un descuento de ", des)
               break
           elif (totalF > 100.00):
               des = totalF * 0.40
               NtotalF = totalF - des
               print("Pago realizado con exito se Cobro ", NtotalF, "Con un descuento de ", des)
               break
           else:
               print("Pago realizado con exito se Cobro ", totalF, "No aplica a descuento")
               break
                   