# Imprime y suma los múltiplos m entre 1 y n.

import os; os.system("cls")

n = int(input("Desde 1 hasta? "))
m = int(input("Múltiplos de? "))
c = s = 0
for i in range(1, n+1):
    if i % m==0:
        print(i, end=" ")
        c = c+1
        s = s+i
print(f"\nLos múltiplos de {m} fueron {c} y su suma es {s}.")
