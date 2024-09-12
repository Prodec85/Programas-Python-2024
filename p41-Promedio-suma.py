# Calcula la suma y promedio de números introducidos

import os

while True:
    os.system("cls")
    s = 0
    nn = 0
    while True:
        n = int(input("Introduzsca el numero deseado o 0 para terminar. "))
        s = s+n
        print(f"{n}")
        if n == 0:
            pro = s/nn
            print(f"Introdugiste {nn} números, la sume de los cuales es: {s} y su promedio es: {pro}")
            break
        else:
            nn+=1
    if input("Deseas continuar (S/N)").upper().startswith("N"):break
print("\nProceso terminado")