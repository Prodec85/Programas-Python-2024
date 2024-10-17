# Imprime la secuencia de números mostrando el número de renglones que el usurario desee.
import os;
while True:
    os.system("cls")
    n = int(input("Cuantos renglones deseas?"))
    for i in range(1, n+1):
        for i in range(1,i+1):
            print(i, end="")
        print()
    if input("\nDeseas continuar (S/N)").upper().startswith("N"):break
print("\nProceso terminado")
