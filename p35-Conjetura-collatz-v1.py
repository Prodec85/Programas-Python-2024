# Calcula e imprie los numeros de la conjetura de Collatz
import os
while(True):
        
    os.system("cls")
    num = int(input("Dame un número positivo"))

    while num!= 1: # Al llegar a 1 salir
        print(num,end=" ")
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    print(num,end=' ')
    if input("\n\nDeseas continuar? (S/N)  ").upper().startswith("N"): break
print("\nProceso terminado")