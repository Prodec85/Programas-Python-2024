# Imprime la secuencia de números mostrando el número de renglones que el usurario desee.
import os;
while True:
    os.system("cls")
    s = 0
    a = 0
    n = int(input("Cuantos términos deseas?   "))
    for i in range(1, n+1):
        a=(1/i)
        s=s+a
        print(f" {"1/" if i != 1 else ""}{i}{"!" if i != 1 else ""}{" +" if i != n else ""}", end=" ")
    print(f"\n La suma es: {s}")
    if input("\nDeseas continuar (S/N)").upper().startswith("N"):break
print("\nProceso terminado")
