"""
Alumnos:
Est. Melvin Josué Pereira Amaya SMIS010221
Est. Melvin Adiel Vásquez Mejía SMIS 001021
Est. Melvin Josué Pérez García SMIS007021

"""

print("Cada numero ingresado se sumara y al final se mostrara el resultado de la suma total.")
print("para detener el programa ingrese 0")
print("--------------------------------------------------------------------------------------")
num = 1
suma=0 
while num != 0:
    entrada = input("Ingrese un numero: ")
    tipo = entrada.isnumeric()

    if tipo == True:
        num = int(entrada)
        suma = suma + num
    else:
        print("No es un entero.")
        
print("La suma total de los numeros es: ",suma)