# Calcula la hipotenusa de un triangulo rectangulo
import os
os.system("cls")

import math as mt

print("Calcula el area de un circulo : \n")
alt = float(input("Cual es la altura? " ))
bas = float(input("Cual es la base? " ))
hip = mt.sqrt(alt**2 + bas**2)
print(f"La hipotenusa del triangulo es: {hip}")