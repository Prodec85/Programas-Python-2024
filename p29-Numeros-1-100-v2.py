#  Imprime numeros del 1 al n usando while.
import os; os.system("cls")


print("\nImrime numeros del 1 al 100 usando while\n")

c = 0
n = int(input("Hasta donde deseas llegar?"))

while c<= n:
    print(c, end=" ")
    c = c + 1
print("\nCiclo terminado.")