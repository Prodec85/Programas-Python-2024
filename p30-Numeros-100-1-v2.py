#  Imprime numeros del n al 1 usando while.
import os; os.system("cls")


print("\nImrime numeros del 100 al 1 usando while\n")
n = int(input("Hasta donde deseas iniciar?"))

c = n


while c>= 1:
    print(c, end=" ")
    c = c - 1
print("\nCiclo terminado.")