# Divide un numero entero de 3 cifras en Centenas, Decenas y Unidades
import os
os.system("cls")

print("Divide un numero entero de 3 cifras en Centenas, Decenas y Unidades \n")
n = int(input("Dame un numero entero de 3 cifras.   "))

c = n  // 100
d = (n - (c*100)) //10
u = (n - (c*100) - (d * 10) )


print("El numero original es: ", n )
print("Centenas :  ", c )
print("Decenas  :  ", d )
print("Unidades :  ", u )
