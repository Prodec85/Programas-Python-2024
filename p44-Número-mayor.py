# Calcula el número mayor en una serie de números dados por el usuario

import os

while True:
    os.system("cls")
    nm = 0
    n = 0
    while True:
        n = int(input("Introduzsca el numero deseado o 0 para terminar. "))
        if n != 0:
            if n>nm:
                nm=n
        else:
            print(f"El número más grande introducido fue: {nm}")
            break
    if input("Deseas continuar (S/N)").upper().startswith("N"):break
print("\nProceso terminado")