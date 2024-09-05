# Acepta estudiantes en base a sexo, edad y tres calificaciones.
import os; os.system("cls")
print("Aspirantes a la Universidad Kitty Kat S.A.")
nom = input("Nombre:")
sex = input("Sexo (H/M):").upper()
if sex == "H":
    print(f"{nom}, esta universidad es solo para mujers, te sujerimos aplicar a Builder Bob.")
elif sex == "M":
    edad = int(input("Edad:"))
    if edad >= 21:
        c1 = int(input("Calivicacion 1: "))
        c2 = int(input("Calivicacion 2: "))
        c3 = int(input("Calivicacion 3: "))
        pro = (c1+c2+c3)/3
        if pro >=8 and pro <=9.5:
            print(f"{nom}, dado que tiens {edad} años, y tu promedio es de {pro:.2}. Te damos la bienvenida a la Universidad Kitty Kat S.A.")
        elif pro >9.5 and pro <=10:
            print(f"{nom}, tu promedio es {pro:.2}, superando nuestras espectativas, te sujerimos aplicar a una universidad mas avanzada.")
        elif pro >0 and pro <8:
            print(f"{nom}, tu promedio es {pro:.2}, lo cual no cumple con nuestros requisitos, te sujerimos aplicar a una universidad mas patito.")
        else:
          print("Los datos ingresados no son correctos.")
    else:
        edadf = 21 - edad
        print(f"{nom}, tu edad de {edad} años no te permite ingresar a esta universidad, te esperamos en {edadf} años.")
else:
    print("Los datos ingresados no son correctos.")



