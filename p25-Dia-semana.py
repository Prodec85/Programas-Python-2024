# Dado un numero entre 1 y 7, determinca a que dia corresponde.
import os; os.system("cls")
print("Dado un numero entre 1 y 7, determinca a que dia corresponde.")
n1 = int(input("\nDame un numero enterno entre 1 y 7.  "))

if n1 == 1:
    print(f"El numero {n1} corresponde a domingo.")
elif n1 == 2:
    print(f"El numero {n1} corresponde a lunes.")
elif n1 == 3:
    print(f"El numero {n1} corresponde a martes.")
elif n1 == 4:
    print(f"El numero {n1} corresponde a miercoles.")
elif n1 == 5:
    print(f"El numero {n1} corresponde a jueves.")
elif n1 == 6:
    print(f"El numero {n1} corresponde a viernes.")
elif n1 == 7:
    print(f"El numero {n1} corresponde a sabado.")
else:
    print("ERROR: El numero dado esta fuera del rango.")


