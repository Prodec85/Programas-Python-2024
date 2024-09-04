# Calcula el volumen de un cilindro

import os
os.system("cls")

import math as mt

print("Calcula el volumen de un cilindro: \n")
rad = float(input("Cual es el radio? " ))
alt = float(input("Cual es la altura? " ))
vol = mt.pi * rad**2 * alt
print(f"El volumen de el cilindro es: {vol}")