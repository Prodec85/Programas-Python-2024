# El usuario adivina un numero entero entre 1 y 100

import os, random

while True:
    os.system("cls")
    num_secreto = random.randint(1,100)
    intentos = 0
    while True:
        num_ingresado = int(input("Adivina el número secreto (1-100)"))
        intentos +=1
        if num_ingresado == num_secreto:
            print(f"\nFelicidades, adivinaste en {intentos} intentos.")
            break
        elif num_ingresado < num_secreto:
            print ("El número secreto es mayor")
        else:
            print("El número es menor.")
    if input("\n\nDeseas continuar? (S/N)").upper().startswith("N"): break
print("\nProceso terminado.")