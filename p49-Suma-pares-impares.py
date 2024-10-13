# Imprime números pares de n a 2 y números de 1 a n, y la suma de ambos casos.
import os

while True:
    os.system("cls")
    print("[1] Imprimir números pares de n a 2 y su suma.")
    print("[2] Imprimir números impares de 1 a n.")
    print("[3] Salir...")
    op=int(input("Elige?"))
    if op==1:
        s = 0
        print("Imprimiendo números pares de n a 2.")
        n = int(input("Desde donde? "))
        n = n if n%2==0 else n-1
        for x in range(n,1,-2):
            print(x, end=" ")
            s = s + x
        print("\nLa suma de números pares es: " + str(s))
    elif op==2:
        s = 0
        print("Imprimiendo números impares de 1 a n y su suma.")
        n = int(input("Hasta donde? "))
        n = n if n%2!=0 else n-1
        for x in range(1,n+1,2):
            print(x, end=" ")
            s = s + x
        print("\nLa suma de números pares es: " + str(s))
    elif op==3:
        break
    else:
        print("\nOpción inválida.")

    input("\n< Presiona cualquier tecla para continuar. >")
print("\nProceso terminado...")
