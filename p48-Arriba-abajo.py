# Imprime números de 1 a n o de n a 1 según lo decida el usuario

import os

while True:
    os.system("cls")
    print("[1] Imprimir de 1 a n")
    print("[2] Imprimir de n a 1")
    print("[3] Salir...")
    op=int(input("Elige?"))
    if op==1:
        print("Imprimiendo números de 1 a n.")
        n = int(input("Hasta donde? "))
        for x in range(1,n+1):
            print(x, end=" ")
    elif op==2:
        print("Imprimiendo números de n a 1.")
        n = int(input("Desde donde? "))
        for x in range(n,0,-1):
            print(x, end=" ")
    elif op==3:
        break
    else:
        print("\nOpción inválida.")

    input("\n< Presiona cualquier tecla para continuar. >")
print("\nProceso terminado...")
