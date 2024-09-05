# Calcula el promedio de 5 calificaciones y da el resultado.
import os; os.system("cls")

print("Calcula el promedio de 5 calificaciones y da el resultado.")
c1 = int(input("Dame la calificacion 1.  "))
c2 = int(input("Dame la calificacion 2.  "))
c3 = int(input("Dame la calificacion 3.  "))
c4 = int(input("Dame la calificacion 4.  "))
c5 = int(input("Dame la calificacion 5.  "))
pro = (c1+c2+c3+c4+c5)/5
if pro >0 and pro <6:
    print(f"Tus calificaciones son:\nCal 1: {c1}\nCal 2: {c2}\nCal 3: {c3}\nCal 4: {c4}\nCal 5: {c5}")
    print(f"Dado tu promedio de {pro}, Quedas reprobado")
elif pro >=6 and pro <7:
    print(f"Tus calificaciones son:\nCal 1: {c1}\nCal 2: {c2}\nCal 3: {c3}\nCal 4: {c4}\nCal 5: {c5}")
    print(f"Dado tu promedio de {pro}, Pasas de panzazo")
elif pro >=7 and pro <8:
    print(f"Tus calificaciones son:\nCal 1: {c1}\nCal 2: {c2}\nCal 3: {c3}\nCal 4: {c4}\nCal 5: {c5}")
    print(f"Dado tu promedio de {pro}, Muy bien, puedes mejorar.")
elif pro >=8 and pro <9:
    print(f"Tus calificaciones son:\nCal 1: {c1}\nCal 2: {c2}\nCal 3: {c3}\nCal 4: {c4}\nCal 5: {c5}")
    print(f"Dado tu promedio de {pro}, Excelente sigue asi.")
elif pro >=9 and pro <=10:
    print(f"Tus calificaciones son:\nCal 1: {c1}\nCal 2: {c2}\nCal 3: {c3}\nCal 4: {c4}\nCal 5: {c5}")
    print(f"Dado tu promedio de {pro}, Perfecto, tu esfuerzo valio la pena.")
else:
    print("ERROR EN CAPTURA DE DATOS.")
