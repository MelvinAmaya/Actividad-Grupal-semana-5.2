"""
Alumnos:
Est. Melvin Josué Pereira Amaya SMIS010221
Est. Melvin Adiel Vásquez Mejía SMIS 001021
Est. Melvin Josué Pérez García SMIS007021

"""
ciclo = "si"
while ciclo == "si":
    cadena = input("Ingrese una letra: ").lower()
    tipo = cadena.isalpha()
    longitud = len(cadena)

    if tipo == True:
        
        if longitud == 1:
            
            if cadena == "a" or cadena == "e" or cadena == "i" or cadena == "o" or cadena == "u":
                print("La letra "+cadena.upper()+" es una vocal...")
            else:
                print("La letra "+cadena.upper()+" es una consonante...")

        else:
            print("Tiene que ingresar solo una letra...")

    else:
        print("Tiene que ingresar una letra...")


    while True:

        ciclo = input("Desea continuar? ").lower()
    
        if ciclo == "no" or ciclo == "si":
             break
        else:
            print("Respuesta desconocida, porfavor responda si o no...")    