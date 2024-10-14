# Imprime un cuadrado de un caracter determinado
import os
os.system("cls")

r = int(input("Cuantos renglones quieres? "))
#c = int(input("Cuantas columnas quieres? "))
car = input("Qúe caracter quieres? ")


for i in range(1, r+1):
    for j in range(1,i+1):
        print(car, end="")
    print()