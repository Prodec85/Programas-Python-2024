# Calcula la suma de números introducidos hasta llegar a 200

import os

while True:
    os.system("cls")
    tci = int(input("\nDame la primer temperatura en °C. "))
    tcf = int(input("Dame la última temperatura en °C. "))
    tfi = (tci*(9/5)+32)
    tff = (tcf*(9/5)+32)
    print(f"\n{tci}°C inical = {tfi:.2f}°F")
    print(f"{tcf}°C final = {tff:.2f}°F")
    while tff >= tfi:
        print(f"{tfi:.2f}°F")
        tfi +=1
    if input("Deseas continuar (S/N)").upper().startswith("N"):break
print("\nProceso terminado")