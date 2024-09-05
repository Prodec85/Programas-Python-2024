#  Imprime numeros del 1 al n, en incrementos de p usando while.
import os; os.system("cls")


print("\nImrime numeros del 1 al 100 usando while\n")

c = 0
n = int(input("Hasta donde deseas llegar?"))
p = int(input("En incrementos de ?"))


while c<= n:
    print(c, end=" ")
    c = c + p
print("\nCiclo terminado.")