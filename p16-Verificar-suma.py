# Verifica si la suma de dos numeros es igual a un tercero

import os; os.system("cls")

print("Verifica si la suma de dos numeros es igual a un tercero.")

n1 = int(input("Dame el primer numero."))
n2 = int(input("Dame el segundo numero."))
n3 = int(input("Dame el tercer numero."))

if n1 + n2 == n3:
    print("\nSon iguales")
else:
    print("\nSon diferentes")

print("\nProceso terminado...")