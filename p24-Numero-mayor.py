# Determina cual es el numero mayor de tres numeros enteros dados.
import os; os.system("cls")

print("Determina cual es el numero mayor de tres numeros enteros dados.")
n1 = int(input("Dame el primer numero.  "))
n2 = int(input("Dame el segundo numero. "))
n3 = int(input("Dame el tercer numero.  "))

if n1 > n2 and n1 > n3:
    print(f"{n1} es el mayor de los tres numeros dados.")
elif n2 > n1 and n2>n3:
    print(f"{n2} es el mayor de los tres numeros dados.")
else:
    print(f"{n3} es el mayor de los tres numeros dados.")

