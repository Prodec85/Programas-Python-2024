# Calcular la paga de un trabajador considerando las horas extras que trabajo
import os; os.system("cls")
print("Calcular la pabga de un trabajador considerano las horas extras que trabajo")

nombre = input("Dame tu nombre: ")
horas = int(input("Horas trabajadas: "))
paga = float(input("Paga x hora: "))
tasa = 0.03
pagan = pagae = pagab = hextra = 0

if horas > 40:
    hextra = horas - 40
    pagan = 40 * paga
    pagae = hextra * paga * 2
    pagab = pagan + pagae
else:
    pagab = horas * paga

impuesto = pagab * tasa
paganeta = pagab - impuesto

print(f"\nEl trabajadro {nombre}, trabajo {horas} horas, a una paga de ${paga:,.2f} x hora.")
print(f"\nHoras extra   :{hextra}, Paga normal: ${pagan:,.2f}. Paga extra: ${pagae:,.2f} ")
print(f"\nPaga bruta    :${pagab:,.2f}")
print(f"\nImpuesto      :${impuesto:,.2f}")
print(f"\nPaga Neta     :${paganeta:,.2f}")
