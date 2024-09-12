# Calcula la suma de números introducidos hasta llegar a 200

import os

while True:
    os.system("cls")
    s = 0
    nn = 1
    while True:
        n = int(input("Introduzsca el numero deseado. "))
        s = s+n
        print(f"{n}")
        if s >= 200:
            print(f"Introdugiste {nn} números, la sume de los cuales es: {s}")
            break
        else:
            nn+=1
    if input("Deseas continuar (S/N)").upper().startswith("N"):break
print("\nProceso terminado")