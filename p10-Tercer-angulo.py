# Calcula el tercer angulo de un triangulo

import os
os.system("cls")

print("Calcula el tercer angulo de un triangulo: \n")
a1 = float(input("Dame el primer angulo. " ))
a2 = float(input("Dame el segundo angulo. " ))
a3 = 180 - (a1 + a2)
print(f"El tercer angulo es: {a3}°")