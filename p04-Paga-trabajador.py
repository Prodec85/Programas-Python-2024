#- p04-Paga-trabajador - Calcuala la paga de un trabajador
print("Calculando la paga de un trabajador  :\n")
nombre = input("Dame tu nombre? ")
horas = int(input("Horas?"))
paga = float(input("Paga x hora?"))
tasa = 0.03

pagabruta= horas * paga
impuesto=pagabruta*tasa
paganeta=pagabruta-impuesto

print(f"El trabajador {nombre}, trabajo {horas} horas, a una paga de ${paga}, con una tasa de ${tasa} ")
print(f"Paga Bruta: ${pagabruta:,.2f}")
print(f"Impuesto:   ${impuesto:,.2f}")
print(f"Paga neta:  ${paganeta:,.2f}")