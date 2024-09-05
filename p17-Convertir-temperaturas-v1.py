# Convertir temperaturas de celcius a farenheit y viceversa

import os; os.system("cls")

print("Convertir temperaturas de celcius a farenheit.")

print(" [ 1 ] Convertir Celcius a Farenheit")
print(" [ 2 ] Convertir Farenheit a Celcius")
op = int(input("Elige."))

if op == 1:
    print("Convirtiendo de °F a °C")
    temp = float(input("Dame los grados Farenheit:  "))
    res = (temp - 32) * 5/9
    print(f"{temp} °F equivale a {res}°C")
else:
    print("Convirtiendo de °C a °F")
    temp = float(input("Dame los grados Celcius:  "))
    res = (temp * 9/5) + 32
    print(f"{temp}°C equivale a {res}°F")





