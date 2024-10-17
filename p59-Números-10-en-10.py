# Imprime los números de 1 a n de 10 en 10.
import os;
while True:
    os.system("cls")
    n = int(input("Hasta que número deseas llegar? "))
    for x in range(1,n+1,10):
        print(x, end=" ")



    if input("\nDeseas continuar (S/N)").upper().startswith("N"):break
print("\nProceso terminado")