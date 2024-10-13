# Suna n números introducidos por el usuario.

import os
os.system("cls")
suma = 0
n = int(input("Cuantas calificaciones? "))
for i in range(1, n+1):
    print(f"Calificación {i} ? ", end="")
    x = float(input())
    suma = suma + x
print(f"\nLa suma es: {suma}")
print(f"\nEl promedio es: {suma / n}")

