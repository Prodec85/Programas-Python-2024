#  Imprime numeros del n al 1 en decrementos p usando while.
import os; os.system("cls")


n = int(input("Hasta donde deseas iniciar?"))
p = int(input("Decrementos de ?"))

c = n


while c>= 1:
    print(c, end=" ")
    c = c - p
print("\nCiclo terminado.")