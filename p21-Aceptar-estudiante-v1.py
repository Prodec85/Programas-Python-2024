# Aceptar un estudiante en base a su edad y dos calificaciones
# >=18  c1>=8 y c2>=8

import os; os.system("cls")
print("Universidad BJU")
print("Aceptar un estudiante en base a su edad y dos calificaciones:\n")

nombre = input("Dame el nombre.")
edad = int(input("Dame la edad."))

if edad < 18:
    print("\nSolo aceptamos mayores de edad")
else:
    print("Dame 2 calificaciones separadas por enter")
    c1, c2 = int(input()), int(input())
    if c1<8 or c2<8:
        print("\nSolo aceptamos con calificaciones mayores o iguales a 8")
    else:
        print(f"{nombre}, bienvenido a la Universidad, tu edad de {edad} años y tus calificaciones {c1}, {c2} lo permiten.")
    
print("\nGracias por usar este programa...")