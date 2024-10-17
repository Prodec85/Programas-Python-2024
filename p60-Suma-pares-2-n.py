# Imprime los números de 1 a n de 10 en 10.
import os;
while True:
    os.system("cls")
    s = 0
    n = int(input("Hasta que número deseas llegar? "))
    n = n if n%2==0 else n-1
    for x in range(2,n+1,2):
        s = s+x
        print(x, end=" ")
    print(f"\nLa suma es = {s}")
    if input("\nDeseas continuar (S/N)").upper().startswith("N"):break
print("\nProceso terminado")