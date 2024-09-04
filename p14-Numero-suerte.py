# Calcula tu numero de suerte basado en el año de nacimiento
import os
os.system("cls")

print("Calcula tu numero de la suerte en base el año de tu nacimiento\n")
n = int(input("Dame el año en que daciste a 4 digitos.   "))

m = n // 1000
c = (n - (m*1000))// 100
d = (n - (m*1000) - (c*100)) //10
u = (n - (m*1000)-(c*100) - (d * 10) )

s = m+c+d+u




print("Naciste en el año: ", n )
print(f"Tu numero de la suerte es: {s}")
