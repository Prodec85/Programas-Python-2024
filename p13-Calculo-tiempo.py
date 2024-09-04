# Calcula dias, minutos y segudos de horas
import os
os.system("cls")
h = int(input("Dame las horas."))
d = h / 24
m = h * 60
s = 60*m*h

print(f"{h} horas equivalen a:\n")
print(f"{d} Dias")
print(f"{m} Minutos")
print(f"{s} Segundos")