# Eleva un número base a su exponente

import os; os.system("cls")

base = int(input("Cuál es la base?"))
exp = int(input("Cuál es el exponente?"))
#print(f"La base es {base} elevado a la {exp} es {base ** exp}")
p = 1
for i in range(exp):
    p=p*base
print(f"\nLa base es {base} elevado a la {exp} es {base ** exp}")

p = 1
for _ in range(exp):
    p=p*base
print(f"\nLa base es {base} elevado a la {exp} es {base ** exp}")

