# Define si los numeros dados son consecutivos
import os; os.system("cls")
print("Determinar si los tres numeros enteros dados son consecutivos.")
n1 = int(input("Dame el primer numero.  "))
n2 = int(input("Dame el segundo numero. "))
n3 = int(input("Dame el tercer numero.  "))


if n1 == n2-1 and n1 == n3-2:
    print(f"\nLos numeros dados son: {n1}, {n2} y {n3} y son consecutivos.")
else:
    print("\nERROR: Los numeros dados no son consecutivos.")
