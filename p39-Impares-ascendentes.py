# Imprime números impares de forma ascendente de 1 a n.

import os

while(True):
    os.system("cls")
    nf = int(input("Hasta que número impar deseas llegar?  "))
    
    s = 0
    n = 1
    while n<=nf:
        print(f"{n}")
        s = s+n
        n+=2
    print(f"La suma de los números impares es: {s}")
    if input("Deseas continuar (S/N)").upper().startswith("N"):break
print("\nProceso terminado")